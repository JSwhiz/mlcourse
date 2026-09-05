#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

CONFIG_NAME = ".obsidian-sync"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync repository Markdown notes into an Obsidian vault."
    )
    parser.add_argument("--vault", help="Override the configured Obsidian vault path.")
    parser.add_argument("--target", help="Override the destination folder inside the vault.")
    parser.add_argument("--source", help="Override the repository notes directory.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files.")
    parser.add_argument("--quiet", action="store_true", help="Only print errors.")
    return parser.parse_args()


def load_config(path: Path) -> dict[str, str]:
    config: dict[str, str] = {}
    if not path.exists():
        return config

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        config[key.strip()] = value.strip().strip('"').strip("'")
    return config


def expand(value: str) -> Path:
    return Path(os.path.expandvars(value)).expanduser().resolve()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    config_path = repo_root / CONFIG_NAME
    config = load_config(config_path)

    vault_value = args.vault or os.getenv("MLCOURSE_OBSIDIAN_VAULT") or config.get("vault")
    target = args.target or config.get("target", "ML Course")
    source = args.source or config.get("source", "obsidian")

    # Deliberately a successful no-op. Git hooks must never break git pull/checkout
    # merely because Obsidian is not configured on this machine.
    if not vault_value:
        if not args.quiet:
            print(
                "[obsidian] skipped: no vault configured. "
                "Create .obsidian-sync or set MLCOURSE_OBSIDIAN_VAULT."
            )
        return 0

    source_root = (repo_root / source).resolve()
    vault_root = expand(vault_value)
    target_root = vault_root / target

    if not source_root.exists():
        if not args.quiet:
            print(f"[obsidian] skipped: source directory is not present in this checkout: {source_root}")
        return 0

    if not vault_root.exists() or not vault_root.is_dir():
        if not args.quiet:
            print(f"[obsidian] skipped: configured vault does not exist: {vault_root}")
        return 0

    markdown_files = sorted(source_root.rglob("*.md"))
    if not markdown_files:
        if not args.quiet:
            print(f"[obsidian] skipped: no Markdown files found in {source_root}")
        return 0

    copied = 0
    unchanged = 0
    for source_file in markdown_files:
        relative_path = source_file.relative_to(source_root)
        destination = target_root / relative_path

        if destination.exists() and destination.read_bytes() == source_file.read_bytes():
            unchanged += 1
            continue

        if not args.quiet:
            action = "DRY-RUN" if args.dry_run else "SYNC"
            print(f"[{action}] {relative_path} -> {destination}")

        if args.dry_run:
            copied += 1
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, destination)
        copied += 1

    if not args.quiet:
        if args.dry_run:
            print(f"[obsidian] {copied} file(s) would change; {unchanged} already current.")
        else:
            print(f"[obsidian] synced {copied} file(s); {unchanged} already current -> {target_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
