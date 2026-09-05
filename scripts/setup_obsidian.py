#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Configure local Obsidian sync for mlcourse.")
    parser.add_argument("--vault", help="Path to your existing Obsidian vault.")
    parser.add_argument("--target", default="ML Course", help="Folder created inside the vault.")
    parser.add_argument(
        "--hooks-only",
        action="store_true",
        help="Enable repository Git hooks without creating a Vault config.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    config_path = repo_root / ".obsidian-sync"

    subprocess.run(
        ["git", "config", "core.hooksPath", ".githooks"],
        cwd=repo_root,
        check=True,
    )
    print("Configured Git hooks: .githooks")

    if args.hooks_only or not args.vault:
        print("No Vault path supplied. Automatic sync remains disabled and git operations stay unaffected.")
        print("Configure later with: python3 scripts/setup_obsidian.py --vault '/path/to/Vault'")
        return 0

    vault = Path(args.vault).expanduser().resolve()
    if not vault.exists() or not vault.is_dir():
        raise SystemExit(f"Vault directory does not exist: {vault}")

    config_path.write_text(
        f"vault={vault}\ntarget={args.target}\nsource=obsidian\n",
        encoding="utf-8",
    )
    print(f"Created local config: {config_path}")

    subprocess.run(
        ["python3", str(repo_root / "scripts" / "sync_obsidian.py")],
        cwd=repo_root,
        check=True,
    )
    print("Setup complete. Future merge-based git pulls and branch checkouts will sync notes automatically.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
