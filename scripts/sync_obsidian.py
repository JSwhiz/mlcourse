#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync Markdown notes from this repository into an Obsidian vault."
    )
    parser.add_argument(
        "--vault",
        required=True,
        help="Path to the Obsidian vault root.",
    )
    parser.add_argument(
        "--target",
        default="ML Course",
        help="Destination folder inside the vault (default: ML Course).",
    )
    parser.add_argument(
        "--source",
        default="obsidian",
        help="Source notes directory in the repository (default: obsidian).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without writing files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    source_root = (repo_root / args.source).resolve()
    vault_root = Path(args.vault).expanduser().resolve()
    target_root = vault_root / args.target

    if not source_root.exists():
        raise SystemExit(f"Source directory not found: {source_root}")

    if not vault_root.exists():
        raise SystemExit(f"Vault directory not found: {vault_root}")

    markdown_files = sorted(source_root.rglob("*.md"))
    if not markdown_files:
        raise SystemExit(f"No Markdown files found in: {source_root}")

    copied = 0
    for source_file in markdown_files:
        relative_path = source_file.relative_to(source_root)
        destination = target_root / relative_path

        action = "COPY" if not args.dry_run else "DRY-RUN"
        print(f"[{action}] {relative_path} -> {destination}")

        if args.dry_run:
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, destination)
        copied += 1

    if args.dry_run:
        print(f"\n{len(markdown_files)} Markdown file(s) would be synced.")
    else:
        print(f"\nSynced {copied} Markdown file(s) to: {target_root}")


if __name__ == "__main__":
    main()
