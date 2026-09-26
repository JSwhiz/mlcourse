#!/usr/bin/env python3
"""Obsidian vault -> repository: send notes edited in Obsidian back to GitHub.

1. fetch <remote>/<branch> (default origin/main);
2. in a temporary worktree based on it, apply notes that were added, edited or
   deleted in the vault since the last sync (your current checkout is not touched);
3. run scripts/validate_repository.py;
4. commit and push to the edits branch (default: obsidian-edits);
5. if validation passed, fast-forward <branch> to the same commit and push it.

Notes changed on both sides (conflicts) are skipped until resolved.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from obsidian_common import (
    CONFLICT, DELETED_IN_VAULT, LABELS, LOCAL_PENDING, REPO_ROOT, current_branch, git,
    load_settings, load_state, plan, save_state,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send notes edited in Obsidian back to the repository.")
    parser.add_argument("--vault", help="Override the configured Obsidian vault path.")
    parser.add_argument("--target", help="Override the destination folder inside the vault.")
    parser.add_argument("--dry-run", action="store_true", help="Only show what would be sent.")
    parser.add_argument("--no-merge", action="store_true", help="Push to the edits branch only, do not update main.")
    parser.add_argument("-m", "--message", help="Commit message.")
    return parser.parse_args()


def attempt(args: argparse.Namespace, s, worktree: Path) -> str:
    base = f"{s.remote}/{s.branch}"
    git("fetch", "--quiet", s.remote, s.branch)
    git("worktree", "add", "--quiet", "--detach", str(worktree), base)

    state = load_state(s)
    items = plan(worktree / s.source, s.target_root, state)
    todo = [it for it in items if it.status in LOCAL_PENDING]
    conflicts = [it for it in items if it.status == CONFLICT]

    for it in conflicts:
        print(f"[obsidian] пропуск, КОНФЛИКТ: {it.rel} — сначала запусти sync_obsidian.py и разреши его.")
    if not todo:
        print("[obsidian] нечего отправлять: правок в Obsidian нет.")
        return "done"
    for it in todo:
        print(f"[{'DRY-RUN' if args.dry_run else 'PUSH'}] {LABELS[it.status]}: {it.rel}")
    if args.dry_run:
        return "done"

    for it in todo:
        dest = worktree / s.source / it.rel
        if it.status == DELETED_IN_VAULT:
            git("rm", "--quiet", "--", str(dest.relative_to(worktree)), cwd=worktree)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(it.vault, dest)
    git("add", "--all", "--", s.source, cwd=worktree)

    check = subprocess.run([sys.executable, "scripts/validate_repository.py"], cwd=worktree,
                           text=True, capture_output=True)
    valid = check.returncode == 0

    names = ", ".join(Path(it.rel).stem for it in todo[:3]) + (" …" if len(todo) > 3 else "")
    message = args.message or f"notes: правки из Obsidian ({len(todo)}): {names}"
    body = "\n".join(f"- {LABELS[it.status]}: {it.rel}" for it in todo)
    git("commit", "--quiet", "-m", message, "-m", body, cwd=worktree)
    git("push", "--quiet", "--force", s.remote, f"HEAD:refs/heads/{s.edits_branch}", cwd=worktree)
    print(f"[obsidian] отправлено в ветку {s.edits_branch}.")

    if not valid:
        print("[obsidian] проверка репозитория НЕ прошла, в main не сливаю:")
        print((check.stdout + check.stderr).strip())
        print(f"[obsidian] исправь заметку и запусти снова; правки пока лежат в {s.edits_branch}.")
        return "invalid"
    if args.no_merge:
        print(f"[obsidian] --no-merge: {s.branch} не трогаю.")
        return "done"

    pushed = subprocess.run(["git", "push", "--quiet", s.remote, f"HEAD:refs/heads/{s.branch}"],
                            cwd=worktree, text=True, capture_output=True)
    if pushed.returncode != 0:
        return "retry"  # someone updated main meanwhile: rebuild on top of it

    for it in todo:
        if it.status == DELETED_IN_VAULT:
            state.files.pop(it.rel, None)
        else:
            state.files[it.rel] = it.vault_hash
    save_state(state)
    print(f"[obsidian] слито в {s.branch}, заметок: {len(todo)}.")

    if current_branch() == s.branch:
        merged = subprocess.run(["git", "merge", "--ff-only", "--quiet", f"{s.remote}/{s.branch}"],
                                cwd=REPO_ROOT, text=True, capture_output=True)
        if merged.returncode != 0:
            print(f"[obsidian] локальный {s.branch} не обновлён автоматически, сделай git pull.")
    return "done"


def main() -> int:
    args = parse_args()
    s = load_settings(vault=args.vault, target=args.target)
    if s.vault is None or not s.vault.is_dir() or not s.target_root.is_dir():
        print("[obsidian] хранилище не настроено или не найдено — отправлять нечего.")
        return 0

    for _ in range(3):
        tmp = Path(tempfile.mkdtemp(prefix="mlcourse-notes-"))
        worktree = tmp / "worktree"
        try:
            result = attempt(args, s, worktree)
        except subprocess.CalledProcessError as exc:
            print(f"[obsidian] ошибка git: {' '.join(exc.cmd)}\n{(exc.stderr or '').strip()}")
            return 1
        finally:
            git("worktree", "remove", "--force", str(worktree), check=False)
            shutil.rmtree(tmp, ignore_errors=True)
        if result != "retry":
            return 0 if result == "done" else 1
        print(f"[obsidian] {s.branch} изменился на GitHub, пересобираю поверх свежей версии…")
    print(f"[obsidian] не удалось обновить {s.branch}; правки в ветке {s.edits_branch}, запусти позже.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
