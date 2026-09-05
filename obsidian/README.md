# Obsidian knowledge workflow

This directory is the Markdown knowledge layer for the course. GitHub remains the source of truth; Obsidian receives a local mirror of these notes when a Vault is configured.

> Full installation, hooks, sparse-checkout and troubleshooting: [`docs/OBSIDIAN.md`](../docs/OBSIDIAN.md).

## Philosophy

The same topic has two complementary views:

- **GitHub topic folder** — code, notebooks and reproducible experiments;
- **Obsidian notes** — concepts, explanations, questions, connections and takeaways.

## Vault layout

```text
ML Course/
├── 00 - Index/
│   └── ML Course.md
├── 01 - Topics/
│   └── Topic 01 - Pandas and Data Analysis/
├── 02 - Concepts/
├── 03 - Cheatsheets/
└── 99 - Inbox/
```

## One-time local setup

```bash
python3 scripts/setup_obsidian.py --vault "$HOME/path/to/YourVault"
```

This creates the gitignored local file `.obsidian-sync` and enables the repository hooks.

After setup, a normal merge/fast-forward:

```bash
git pull
```

will automatically refresh the notes in the configured Vault. Branch checkout also refreshes them so Obsidian follows the active topic branch.

For `pull.rebase=true`, use:

```bash
make pull
```

## No Vault configured = no side effects

This is intentional and important. If there is no local Vault path:

- nothing is copied;
- no external directory is created;
- Git operations continue normally;
- sync exits successfully as a no-op.

The personal Vault path is never committed to GitHub.

## Optional: do not check out notes locally

`obsidian/` is tracked by default because the knowledge base belongs to the project. A machine that does not use Obsidian may optionally exclude it with Git sparse-checkout. See [`docs/OBSIDIAN.md`](../docs/OBSIDIAN.md#optional-checkout-without-obsidian-notes).

## Note rules

Each permanent note should use YAML frontmatter and stay atomic:

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

Use `[[wikilinks]]`, keep explanations in your own words, link back to relevant notebooks, keep unresolved points under `# Questions`, and finish mature notes with `# Takeaways`.
