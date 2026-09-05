# Obsidian integration

This document defines how repository notes are delivered to a local Obsidian Vault.

## Design

The repository is the versioned source of truth. Files under `obsidian/` are ordinary tracked Markdown files. A local Vault is only a destination copy used by Obsidian.

```text
GitHub branch -> git checkout / git pull -> obsidian/*.md -> local sync -> Obsidian Vault/ML Course/
```

The integration is **opt-in per computer**. The repository never stores a personal Vault path.

## Safety rule

If `.obsidian-sync` does not exist, `MLCOURSE_OBSIDIAN_VAULT` is not set, or the configured Vault path does not exist, synchronization is a successful no-op:

- nothing is copied anywhere;
- no directory outside the repository is created;
- `git pull` and `git checkout` are not blocked;
- the repository remains usable without Obsidian.

`.obsidian-sync` is listed in `.gitignore` and must never be committed.

## One-time setup

After cloning the repository, run:

```bash
python3 scripts/setup_obsidian.py --vault "$HOME/path/to/YourVault"
```

The setup script does two local-only things:

1. creates `.obsidian-sync` with the Vault path;
2. configures this clone to use versioned hooks from `.githooks/`.

Example local config:

```text
vault=/Users/me/Documents/Obsidian/MyVault
target=ML Course
source=obsidian
```

You can also configure only the hooks and leave sync disabled:

```bash
python3 scripts/setup_obsidian.py --hooks-only
```

## What happens after setup

For the normal merge/fast-forward workflow:

```bash
git pull
```

Git runs `.githooks/post-merge`, which calls `scripts/sync_obsidian.py`. Switching branches runs `.githooks/post-checkout` and refreshes the Vault from the newly checked-out branch.

For repositories configured with `pull.rebase=true`, use the repository shortcut below because Git's `post-merge` hook is not the reliable completion point for a rebase pull:

```bash
make pull
```

or:

```bash
python3 scripts/pull.py
```

That command performs `git pull` and then explicitly runs the note sync.

## Manual commands

```bash
make notes
make notes-dry
```

Equivalent commands:

```bash
python3 scripts/sync_obsidian.py
python3 scripts/sync_obsidian.py --dry-run
```

A one-off Vault can be supplied without creating a config:

```bash
python3 scripts/sync_obsidian.py --vault "/path/to/Vault"
```

## Environment variable

Instead of `.obsidian-sync`, a machine can set:

```bash
export MLCOURSE_OBSIDIAN_VAULT="$HOME/Documents/Obsidian/MyVault"
```

Command-line `--vault` has highest priority, then `MLCOURSE_OBSIDIAN_VAULT`, then `.obsidian-sync`.

## Optional checkout without Obsidian notes

By default, `obsidian/` is part of the topic branch and is pulled like normal source files. This is intentional: GitHub should always contain the knowledge layer.

On a machine that does not need notes locally, Git sparse-checkout can exclude that directory. This is an advanced, per-clone choice:

```bash
git sparse-checkout init --no-cone
printf '/*\n!/obsidian/\n' > .git/info/sparse-checkout
git read-tree -mu HEAD
```

Restore the full working tree with:

```bash
git sparse-checkout disable
```

Important: sparse-checkout only changes which tracked files appear in that local working tree. It does not remove notes from GitHub or from the branch.

## Recommended workflow

For a personal Mac with Obsidian configured:

```text
one time:  python3 scripts/setup_obsidian.py --vault "/path/to/Vault"

normally:  git checkout topicXX-...
           git pull
           work / commit / push

result:    current branch notes are mirrored to Vault/ML Course/
```

If the Vault is unavailable, the sync is skipped and Git continues normally.
