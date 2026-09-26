#!/usr/bin/env python3
"""Shared logic for the two-way Obsidian sync.

Model
-----
Three versions of every note are compared:

* ``repo``  – the file under ``obsidian/`` in a Git tree;
* ``vault`` – the copy inside the Obsidian vault;
* ``base``  – the content both sides had at the last successful sync.

``base`` hashes live in ``.git/obsidian-sync-state.json``: per clone, never
committed. Comparing against ``base`` tells *who* changed a note, so the sync can
update untouched notes, keep local edits, and detect real conflicts instead of
silently overwriting anything.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_NAME = ".obsidian-sync"
STATE_NAME = "obsidian-sync-state.json"
CONFLICT_MARK = " (версия из репозитория)"

DEFAULTS = {
    "target": "ML Course",
    "source": "obsidian",
    "branch": "main",
    "edits_branch": "obsidian-edits",
    "remote": "origin",
}

# Plan statuses
IN_SYNC = "in-sync"
NEW_IN_REPO = "new-in-repo"            # sync: copy to vault
REPO_CHANGED = "repo-changed"          # sync: update vault
DELETED_IN_REPO = "deleted-in-repo"    # sync: remove from vault
NEW_IN_VAULT = "new-in-vault"          # push: add to repo
VAULT_CHANGED = "vault-changed"        # push: update repo
DELETED_IN_VAULT = "deleted-in-vault"  # push: remove from repo
CONFLICT = "conflict"                  # both changed: keep vault, save repo copy
GONE = "gone"                          # absent everywhere: forget

LOCAL_PENDING = {NEW_IN_VAULT, VAULT_CHANGED, DELETED_IN_VAULT}


def nfc(text: str) -> str:
    # macOS may store Cyrillic file names decomposed (NFD); Git uses NFC.
    return unicodedata.normalize("NFC", text)


def git(*args: str, cwd: Path = REPO_ROOT, check: bool = True) -> str:
    result = subprocess.run(["git", *args], cwd=cwd, text=True, capture_output=True)
    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, result.args, result.stdout, result.stderr)
    return (result.stdout or "").strip()


def current_branch(cwd: Path = REPO_ROOT) -> str:
    return git("rev-parse", "--abbrev-ref", "HEAD", cwd=cwd, check=False) or "HEAD"


def expand(value: str) -> Path:
    return Path(os.path.expandvars(value)).expanduser().resolve()


@dataclass
class Settings:
    vault: Path | None
    target: str
    source: str
    branch: str
    edits_branch: str
    remote: str

    @property
    def target_root(self) -> Path | None:
        return self.vault / self.target if self.vault else None

    @property
    def source_root(self) -> Path:
        return REPO_ROOT / self.source


def load_settings(**overrides: str | None) -> Settings:
    """Precedence: command line > MLCOURSE_OBSIDIAN_VAULT > .obsidian-sync > defaults."""
    config: dict[str, str] = dict(DEFAULTS)
    path = REPO_ROOT / CONFIG_NAME
    if path.exists():
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip().strip('"').strip("'")
    if os.getenv("MLCOURSE_OBSIDIAN_VAULT"):
        config["vault"] = os.environ["MLCOURSE_OBSIDIAN_VAULT"]
    for key, value in overrides.items():
        if value:
            config[key] = value
    vault = expand(config["vault"]) if config.get("vault") else None
    return Settings(
        vault=vault,
        target=config["target"],
        source=config["source"],
        branch=config["branch"],
        edits_branch=config["edits_branch"],
        remote=config["remote"],
    )


# ---------------------------------------------------------------- state


def _state_path() -> Path:
    return Path(git("rev-parse", "--absolute-git-dir")) / STATE_NAME


@dataclass
class State:
    target: str = ""
    files: dict[str, str] = field(default_factory=dict)       # rel -> base hash
    conflicts: dict[str, str] = field(default_factory=dict)   # rel -> repo hash saved as conflict copy


def load_state(settings: Settings) -> State:
    path = _state_path()
    if not path.exists():
        return State(target=str(settings.target_root))
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("target") != str(settings.target_root):
        # Vault/target changed: old base hashes say nothing about the new location.
        return State(target=str(settings.target_root))
    return State(target=data["target"], files=data.get("files", {}), conflicts=data.get("conflicts", {}))


def save_state(state: State) -> None:
    payload = {"target": state.target, "files": dict(sorted(state.files.items())),
               "conflicts": dict(sorted(state.conflicts.items()))}
    _state_path().write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- scanning


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_note(rel: Path) -> bool:
    if rel.suffix.lower() != ".md":
        return False
    if any(part.startswith(".") for part in rel.parts):
        return False
    return CONFLICT_MARK not in rel.stem


def scan(root: Path) -> dict[str, Path]:
    if not root.exists():
        return {}
    notes: dict[str, Path] = {}
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if path.is_file() and is_note(rel):
            notes[nfc(rel.as_posix())] = path
    return notes


def conflict_copy(path: Path) -> Path:
    return path.with_name(f"{path.stem}{CONFLICT_MARK}{path.suffix}")


# ---------------------------------------------------------------- planning


@dataclass
class Item:
    rel: str
    status: str
    repo: Path | None
    vault: Path | None
    repo_hash: str | None
    vault_hash: str | None


def plan(repo_root: Path, vault_root: Path, state: State) -> list[Item]:
    repo_files = scan(repo_root)
    vault_files = scan(vault_root)

    # A conflict is resolved when the user deleted the "(версия из репозитория)" copy
    # while the repository still holds that same version: the vault note then counts
    # as an edit made on top of it.
    for rel, repo_hash in list(state.conflicts.items()):
        vault_path = vault_files.get(rel) or (vault_root / rel)
        if conflict_copy(vault_path).exists():
            continue
        if rel in repo_files and digest(repo_files[rel]) == repo_hash:
            state.files[rel] = repo_hash
        del state.conflicts[rel]

    items: list[Item] = []
    for rel in sorted(set(repo_files) | set(vault_files) | set(state.files)):
        r_path, v_path = repo_files.get(rel), vault_files.get(rel)
        r = digest(r_path) if r_path else None
        v = digest(v_path) if v_path else None
        b = state.files.get(rel)

        if r is None and v is None:
            status = GONE
        elif r == v:
            status = IN_SYNC
        elif v is None:
            status = DELETED_IN_VAULT if b == r else NEW_IN_REPO
        elif r is None:
            status = DELETED_IN_REPO if b == v else NEW_IN_VAULT
        elif v == b:
            status = REPO_CHANGED
        elif r == b:
            status = VAULT_CHANGED
        else:
            status = CONFLICT
        items.append(Item(rel, status, r_path, v_path, r, v))
    return items


LABELS = {
    NEW_IN_REPO: "новая из репозитория",
    REPO_CHANGED: "обновлена из репозитория",
    DELETED_IN_REPO: "удалена в репозитории",
    NEW_IN_VAULT: "новая в Obsidian",
    VAULT_CHANGED: "изменена в Obsidian",
    DELETED_IN_VAULT: "удалена в Obsidian",
    CONFLICT: "КОНФЛИКТ",
}
