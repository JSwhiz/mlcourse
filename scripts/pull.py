#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    subprocess.run(["git", "pull"], cwd=repo_root, check=True)
    # Explicit sync also covers pull.rebase=true, where post-merge may not run.
    subprocess.run(["python3", str(repo_root / "scripts" / "sync_obsidian.py")], cwd=repo_root, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
