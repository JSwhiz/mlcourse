#!/usr/bin/env python3
"""Lightweight repository checks used locally and in CI."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPIC_RE = re.compile(r"^topic\d{2}_.+")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_topics() -> None:
    topics = sorted(p for p in ROOT.iterdir() if p.is_dir() and TOPIC_RE.match(p.name))
    if not topics:
        fail("No topic directories found")

    for topic in topics:
        readme = topic / "README.md"
        notebooks = topic / "notebooks"
        if not readme.exists():
            fail(f"{topic.name}: README.md is missing")
        if not notebooks.exists():
            fail(f"{topic.name}: notebooks/ is missing")

        notebook_files = sorted(notebooks.glob("*.ipynb"))
        if not notebook_files:
            fail(f"{topic.name}: no notebooks found")

        for notebook in notebook_files:
            try:
                payload = json.loads(notebook.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                fail(f"{notebook.relative_to(ROOT)} is not valid notebook JSON: {exc}")
            if payload.get("nbformat") != 4:
                fail(f"{notebook.relative_to(ROOT)}: expected nbformat 4")
            if not isinstance(payload.get("cells"), list):
                fail(f"{notebook.relative_to(ROOT)}: cells must be a list")


def validate_relative_markdown_links() -> None:
    markdown_files = [ROOT / "README.md"]
    markdown_files.extend(ROOT.glob("topic*/README.md"))
    markdown_files.extend((ROOT / "docs").glob("*.md"))

    for md in markdown_files:
        if not md.exists():
            continue
        text = md.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_RE.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            decoded = target.replace("%20", " ")
            candidate = (md.parent / decoded).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"{md.relative_to(ROOT)} links outside repository: {target}")
            if not candidate.exists():
                fail(f"Broken relative link in {md.relative_to(ROOT)}: {target}")


def validate_obsidian() -> None:
    index = ROOT / "obsidian" / "00 - Index" / "ML Course.md"
    if not index.exists():
        fail("Obsidian course index is missing")


def main() -> int:
    validate_topics()
    validate_relative_markdown_links()
    validate_obsidian()
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
