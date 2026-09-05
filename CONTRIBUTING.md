# Contributing

This repository is primarily a personal learning workspace, but its structure is intentionally reproducible and reviewable.

## Branches

Course topics are developed in dedicated branches:

```text
topicXX-short-topic-name
```

Examples:

```text
topic01-pandas-data-analysis
topic02-data-visualization
```

Repository-wide maintenance may use conventional branches such as `chore-*` or `docs-*`.

## Topic definition of done

A topic is ready to merge when:

- notebooks execute top-to-bottom in a clean environment;
- Notebook CI is green;
- the topic README reflects the actual state of the topic;
- relevant Russian Obsidian notes are present and linked;
- relative links and repository structure pass Repository Quality CI;
- temporary files, private datasets, local paths and secrets are absent;
- conclusions are written in plain language and do not overclaim what the data proves.

## Notebook rules

- Prefer reproducible cells over hidden notebook state.
- Keep imports near the beginning of the notebook.
- Avoid absolute local paths.
- Use relative repository paths or a documented public fallback.
- Preserve useful outputs when they improve GitHub preview quality.
- Do not commit very large outputs, credentials, tokens, personal data or restricted datasets.
- Prefer vectorized NumPy/Pandas operations over row-by-row Python loops when appropriate.

## Obsidian notes

Anything under `obsidian/` is part of the long-term knowledge base and should be written in Russian.

Use atomic notes for reusable concepts and a topic summary for the complete mental model. Prefer `[[wikilinks]]` between related ideas.

## Commits

Keep commit messages short and descriptive. Examples:

```text
feat: add topic 02 visualization practice
docs: expand pandas aggregation notes
ci: validate notebook execution
fix: remove absolute dataset path
```

## Pull requests

Before merging:

```bash
make check
```

For a full local notebook execution check:

```bash
make notebooks
```

The pull request should explain what changed, how it was verified, and whether any Obsidian notes were added or updated.
