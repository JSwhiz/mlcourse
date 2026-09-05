# Obsidian knowledge workflow

This directory contains Markdown notes designed to be reusable inside an Obsidian vault.

## Philosophy

GitHub is the source of truth for code, notebooks, datasets, and version history.
Obsidian is the knowledge layer for concepts, summaries, links, questions, and long-term recall.

The same topic should therefore have two complementary views:

- **GitHub topic folder** — code, notebooks, reproducible experiments;
- **Obsidian topic notes** — concepts, explanations, connections, takeaways.

## Suggested vault layout

```text
ML Course/
├── 00 - Index/
│   └── ML Course.md
├── 01 - Topics/
│   └── Topic 01 - Pandas and Data Analysis/
│       ├── Topic 01 - Overview.md
│       ├── Pandas - Series and DataFrame.md
│       ├── Pandas - Indexing and Filtering.md
│       └── Pandas - GroupBy and Aggregations.md
├── 02 - Concepts/
├── 03 - Cheatsheets/
└── 99 - Inbox/
```

## Note rules

Each note should contain YAML frontmatter:

```yaml
---
type: concept
topic: topic01
course: mlcourse.ai
status: learning
tags:
  - machine-learning
  - pandas
---
```

Recommended conventions:

- one concept per note;
- use Obsidian links such as `[[Pandas - GroupBy and Aggregations]]`;
- link back to the relevant GitHub notebook;
- keep conclusions in your own words;
- use `# Questions` for unclear points;
- use `# Takeaways` for final conclusions;
- avoid copying the course text verbatim.

## Syncing into Obsidian

A browser download cannot safely choose an arbitrary folder inside your local Obsidian vault. Browsers intentionally restrict this.

The reliable solution is a local sync command. The repository includes `scripts/sync_obsidian.py`, which copies all Markdown files from `obsidian/` into a chosen vault folder while preserving the directory structure.

Example:

```bash
python scripts/sync_obsidian.py \
  --vault "$HOME/Documents/Obsidian/MyVault" \
  --target "ML Course"
```

This produces:

```text
MyVault/
└── ML Course/
    └── ... synced notes ...
```

Run the command again whenever notes change. Existing files with the same relative paths are updated.
