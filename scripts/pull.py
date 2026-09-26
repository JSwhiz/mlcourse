#!/usr/bin/env python3
"""Full round trip: send Obsidian edits -> git pull -> refresh the vault.

Order matters: local edits leave first, so nothing written in Obsidian can be
lost. Even if sending fails (offline, validation), the pull stays safe:
sync_obsidian.py never overwrites notes edited in Obsidian.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    scripts = repo_root / "scripts"

    sent = subprocess.run([sys.executable, str(scripts / "push_obsidian.py")], cwd=repo_root)
    if sent.returncode != 0:
        print("[obsidian] правки не отправлены, но при pull они не пропадут.")

    subprocess.run(["git", "pull"], cwd=repo_root, check=True)
    # Explicit sync also covers pull.rebase=true, where post-merge may not run.
    subprocess.run([sys.executable, str(scripts / "sync_obsidian.py")], cwd=repo_root, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
