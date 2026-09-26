# Obsidian integration

This document defines how repository notes are delivered to a local Obsidian Vault.

## Design

The repository (`main` on GitHub) is the versioned source of truth. Files under `obsidian/` are ordinary tracked Markdown files. A local Vault holds a working copy that can be edited in Obsidian; edits travel back through a dedicated branch.

```text
GitHub main ── git pull ──▶ obsidian/*.md ── sync_obsidian.py ──▶ Vault/<target>/
Vault/<target>/ ── push_obsidian.py ──▶ obsidian-edits ── validation ──▶ main
```

Every note has three versions: the repository file, the Vault file, and the *base* — the content both had at the last sync. Base hashes are stored per clone in `.git/obsidian-sync-state.json` (never committed). Comparing with the base shows who changed a note:

| Repository | Vault | Result of `sync_obsidian.py` | Result of `push_obsidian.py` |
|---|---|---|---|
| changed | untouched | Vault updated | — |
| untouched | changed / new / deleted | left alone, reported as pending | sent |
| changed | changed | **conflict**: Vault kept, repository copy saved as `<name> (версия из репозитория).md` | skipped until resolved |
| deleted | untouched | removed from Vault | — |

A conflict is resolved by moving what you need into the main note and deleting the `(версия из репозитория)` copy; the next push sends the result.

The sync runs only on the configured branch (`main`). Topic branches are older snapshots of the notes, and mirroring them would roll the Vault back.

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

Everyday command:

```bash
make pull            # = python3 scripts/pull.py
```

It runs three steps: send Obsidian edits (`push_obsidian.py`) → `git pull` → refresh the Vault (`sync_obsidian.py`). A plain `git pull` on `main` is also safe: the `post-merge` hook refreshes the Vault without touching notes edited in Obsidian.

### Sending edits

```bash
make push-notes      # = python3 scripts/push_obsidian.py
make push-notes-dry  # preview only
```

`push_obsidian.py`:

1. fetches `origin/main`;
2. applies notes added, edited or deleted in the Vault in a temporary worktree (your checkout and current branch are untouched);
3. runs `scripts/validate_repository.py`;
4. commits and force-pushes the result to `obsidian-edits`;
5. if validation passed, pushes the same commit to `main` (fast-forward) and fast-forwards the local `main`.

If validation fails, `main` is not changed and the edits stay in `obsidian-edits` until fixed. If `main` moved on GitHub in the meantime, the edits are rebuilt on top of it automatically. `--no-merge` stops after step 4.

## Manual commands

```bash
make notes           # repository -> Vault
make notes-dry
make push-notes      # Vault -> obsidian-edits -> main
```

Equivalent commands:

```bash
python3 scripts/sync_obsidian.py [--dry-run] [--any-branch]
python3 scripts/push_obsidian.py [--dry-run] [--no-merge] [-m "message"]
```

A one-off Vault can be supplied without creating a config:

```bash
python3 scripts/sync_obsidian.py --vault "/path/to/Vault"
```

Optional keys in `.obsidian-sync`: `branch` (default `main`), `edits_branch` (default `obsidian-edits`), `remote` (default `origin`).

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

```text
one time:  python3 scripts/setup_obsidian.py --vault "/path/to/Vault"

normally:  edit notes in Obsidian
           make pull            # sends your edits, pulls, refreshes the Vault

result:    Vault/<target>/ mirrors main; your edits reach main via obsidian-edits
```

If the Vault is unavailable, the sync is skipped and Git continues normally.
