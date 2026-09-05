#!/usr/bin/env python3
"""Repository checks used locally and in CI."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
TOPIC_RE = re.compile(r"^topic(\d{2})_.+")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IMAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_topics() -> None:
    topics = sorted(p for p in ROOT.iterdir() if p.is_dir() and TOPIC_RE.match(p.name))
    if not topics:
        fail("No topic directories found")

    for topic in topics:
        match = TOPIC_RE.match(topic.name)
        assert match is not None
        number = match.group(1)
        readme = topic / "README.md"
        notebooks = topic / "notebooks"
        images = topic / "images" / "previews"
        if not readme.exists(): fail(f"{topic.name}: README.md is missing")
        if not notebooks.exists(): fail(f"{topic.name}: notebooks/ is missing")
        notebook_files = sorted(notebooks.glob("*.ipynb"))
        if not notebook_files: fail(f"{topic.name}: no notebooks found")
        for notebook in notebook_files:
            try: payload = json.loads(notebook.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc: fail(f"{notebook.relative_to(ROOT)} is not valid notebook JSON: {exc}")
            if payload.get("nbformat") != 4: fail(f"{notebook.relative_to(ROOT)}: expected nbformat 4")
            if not isinstance(payload.get("cells"), list): fail(f"{notebook.relative_to(ROOT)}: cells must be a list")

        if not images.exists(): fail(f"{topic.name}: images/previews/ is missing")
        preview_files = sorted(p for p in images.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg"})
        if not preview_files: fail(f"{topic.name}: no preview images found")
        if not IMAGE_LINK_RE.search(readme.read_text(encoding="utf-8")): fail(f"{topic.name}: README.md does not embed a preview image")

        notes = list((ROOT / "obsidian" / "01 - Topics").glob(f"Topic {number} -*/*Подробная выжимка.md"))
        if len(notes) != 1: fail(f"{topic.name}: expected exactly one Obsidian detailed summary, found {len(notes)}")
        if len(notes[0].read_text(encoding="utf-8").strip()) < 1500: fail(f"{notes[0].relative_to(ROOT)}: detailed summary is unexpectedly short")


def validate_relative_markdown_links() -> None:
    markdown_files = [ROOT / "README.md", *ROOT.glob("topic*/README.md"), *(ROOT / "docs").glob("*.md")]
    for md in markdown_files:
        if not md.exists(): continue
        text = md.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_RE.findall(text) + IMAGE_LINK_RE.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")): continue
            candidate = (md.parent / unquote(target)).resolve()
            try: candidate.relative_to(ROOT.resolve())
            except ValueError: fail(f"{md.relative_to(ROOT)} links outside repository: {target}")
            if not candidate.exists(): fail(f"Broken relative link in {md.relative_to(ROOT)}: {target}")


def validate_obsidian() -> None:
    index = ROOT / "obsidian" / "00 - Index" / "ML Course.md"
    if not index.exists(): fail("Obsidian course index is missing")
    text = index.read_text(encoding="utf-8")
    for number in range(1, 11):
        if f"Topic {number:02d}" not in text: fail(f"Obsidian index does not mention Topic {number:02d}")


def main() -> int:
    validate_topics(); validate_relative_markdown_links(); validate_obsidian()
    print("Repository validation passed.")
    return 0


if __name__ == "__main__": sys.exit(main())
