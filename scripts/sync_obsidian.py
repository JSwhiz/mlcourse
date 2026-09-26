#!/usr/bin/env python3
"""Repository -> Obsidian vault. Never overwrites or deletes a note edited in Obsidian.

* untouched notes are updated / added / removed to match the repository;
* notes edited in Obsidian are left alone and reported as "waiting to be sent"
  (send them with scripts/push_obsidian.py);
* if both sides changed, the vault note is kept and the repository version is
  saved next to it as "<name> (версия из репозитория).md".

Runs only on the configured branch (default: main). Topic branches are older
snapshots of the notes; mirroring them would make the vault go back in time.
Missing config / vault is a successful no-op so Git hooks never block git.
"""

from __future__ import annotations

import argparse
import shutil

from obsidian_common import (
    CONFLICT, CONFLICT_MARK, DELETED_IN_REPO, GONE, IN_SYNC, LABELS, LOCAL_PENDING,
    NEW_IN_REPO, REPO_CHANGED, conflict_copy, current_branch, load_settings, load_state, plan,
    save_state,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync repository notes into an Obsidian vault safely.")
    parser.add_argument("--vault", help="Override the configured Obsidian vault path.")
    parser.add_argument("--target", help="Override the destination folder inside the vault.")
    parser.add_argument("--source", help="Override the repository notes directory.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files.")
    parser.add_argument("--quiet", action="store_true", help="Only print changes and warnings.")
    parser.add_argument("--any-branch", action="store_true", help="Sync even when not on the configured branch.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    s = load_settings(vault=args.vault, target=args.target, source=args.source)
    say = (lambda *_: None) if args.quiet else print

    if s.vault is None:
        say("[obsidian] пропуск: хранилище не настроено (.obsidian-sync или MLCOURSE_OBSIDIAN_VAULT).")
        return 0
    if not s.vault.is_dir():
        say(f"[obsidian] пропуск: хранилище не найдено: {s.vault}")
        return 0
    if not s.source_root.is_dir():
        say(f"[obsidian] пропуск: в этой ветке нет папки {s.source}/")
        return 0
    branch = current_branch()
    if branch != s.branch and not args.any_branch:
        say(f"[obsidian] пропуск: ветка «{branch}», синхронизация идёт только с «{s.branch}».")
        return 0

    state = load_state(s)
    target = s.target_root
    assert target is not None
    items = plan(s.source_root, target, state)
    tag = "DRY-RUN" if args.dry_run else "SYNC"
    changed = pending = conflicts = 0

    for it in items:
        dest = target / it.rel
        if it.status in (NEW_IN_REPO, REPO_CHANGED):
            print(f"[{tag}] {LABELS[it.status]}: {it.rel}")
            if not args.dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(it.repo, dest)
                state.files[it.rel] = it.repo_hash
            changed += 1
        elif it.status == DELETED_IN_REPO:
            print(f"[{tag}] {LABELS[it.status]}: {it.rel}")
            if not args.dry_run:
                it.vault.unlink()
                state.files.pop(it.rel, None)
                folder = it.vault.parent
                while folder != target and folder.is_dir() and not any(folder.iterdir()):
                    folder.rmdir()
                    folder = folder.parent
            changed += 1
        elif it.status == IN_SYNC:
            state.files[it.rel] = it.repo_hash
        elif it.status == GONE:
            state.files.pop(it.rel, None)
        elif it.status in LOCAL_PENDING:
            print(f"[obsidian] {LABELS[it.status]}, ждёт отправки: {it.rel}")
            pending += 1
        elif it.status == CONFLICT:
            copy = conflict_copy(it.vault)
            print(f"[obsidian] КОНФЛИКТ: {it.rel} изменена и в Obsidian, и в репозитории.")
            print(f"           Твоя версия не тронута. Версия из репозитория: «{copy.name}».")
            print(f"           Перенеси нужное в основную заметку и удали копию{CONFLICT_MARK}.")
            if not args.dry_run:
                shutil.copy2(it.repo, copy)
                state.conflicts[it.rel] = it.repo_hash
            conflicts += 1

    if not args.dry_run:
        save_state(state)
    summary = f"[obsidian] {'будет изменено' if args.dry_run else 'обновлено'}: {changed}"
    if pending:
        summary += f"; ждут отправки: {pending} (python3 scripts/push_obsidian.py)"
    if conflicts:
        summary += f"; конфликтов: {conflicts}"
    if changed or pending or conflicts or not args.quiet:
        print(f"{summary} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
