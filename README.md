<div align="center">

# Machine Learning Course

### A reproducible learning repository built around `mlcourse.ai`

[![Notebooks CI](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml)
[![Repository Quality](https://github.com/JSwhiz/mlcourse/actions/workflows/repository-quality.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/repository-quality.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Course](https://img.shields.io/badge/course-mlcourse.ai-111827)](https://mlcourse.ai/)

**Notebooks · experiments · Russian knowledge notes · CI-verified results**

[Progress](#progress) · [Topic 01](./topic01_pandas_data_analysis) · [Knowledge base](#knowledge-base--obsidian) · [Quick start](#quick-start) · [Workflow](./CONTRIBUTING.md)

</div>

---

## About

This repository is my personal workspace for the **mlcourse.ai** curriculum. Each topic combines three layers:

```text
course material
      ↓
executable notebook practice
      ↓
Russian long-term knowledge notes in Obsidian
```

The goal is not to accumulate notebooks. The goal is to build a learning trail that is **executable, reviewable and useful later**:

> **question → experiment → result → interpretation → reusable knowledge**

Every published notebook is expected to run top-to-bottom in a clean GitHub Actions environment. Repository structure and relative documentation links are checked separately by CI.

## Progress

| # | Topic | Status | Practice | Knowledge |
|---:|---|:---:|---|---|
| 01 | NumPy, Pandas & exploratory data analysis | ✅ Completed | [`Topic 01`](./topic01_pandas_data_analysis) | [`Knowledge map`](./obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Overview.md) |
| 02 | Data visualization | ⚪ Planned | — | — |
| 03 | Classification, decision trees & k-NN | ⚪ Planned | — | — |
| 04 | Linear models | ⚪ Planned | — | — |
| 05 | Ensembles & random forests | ⚪ Planned | — | — |
| 06 | Feature engineering | ⚪ Planned | — | — |
| 07 | Unsupervised learning | ⚪ Planned | — | — |
| 08 | Time series fundamentals | ⚪ Planned | — | — |

### Topic 01 at a glance

Topic 01 already contains three real notebooks:

- [`01_adult_pandas_analysis.ipynb`](./topic01_pandas_data_analysis/notebooks/01_adult_pandas_analysis.ipynb) — full UCI Adult Pandas analysis;
- [`02_numpy_foundations.ipynb`](./topic01_pandas_data_analysis/notebooks/02_numpy_foundations.ipynb) — arrays, masks, broadcasting, axes and vectorization;
- [`03_titanic_mini_eda.ipynb`](./topic01_pandas_data_analysis/notebooks/03_titanic_mini_eda.ipynb) — filtering, missing values, grouping, derived features and EDA.

The topic README also contains clickable visual notebook previews.

## Reproducibility

Two independent GitHub Actions workflows protect the repository.

### Notebooks CI

[`Notebooks CI`](./.github/workflows/notebooks-ci.yml) discovers `topic*/notebooks/*.ipynb`, installs a clean Python environment and executes every notebook from top to bottom.

If one code cell raises an error, the workflow fails. Successful runs upload the executed notebooks as a short-lived Actions artifact.

### Repository Quality

[`Repository Quality`](./.github/workflows/repository-quality.yml) validates:

- topic directories follow the expected structure;
- each topic has a README and notebook directory;
- notebook files are valid nbformat 4 JSON;
- important relative Markdown links resolve inside the repository;
- the Obsidian course index exists.

Local equivalent:

```bash
make check
```

## Knowledge base / Obsidian

The versioned knowledge layer lives under [`obsidian/`](./obsidian). All personal notes intended for the Vault are written in **Russian**.

```text
GitHub / notebooks                     Obsidian / knowledge
──────────────────────────────────     ──────────────────────────────────
reproducible exercises                 concepts in my own words
code and outputs                       mental models and explanations
CI verification             ↔          wikilinks between ideas
version history                         long-term revision notes
```

Main entry points:

- [`ML Course` index](./obsidian/00%20-%20Index/ML%20Course.md)
- [`Topic 01 — knowledge map`](./obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Overview.md)
- [`Topic 01 — detailed Russian summary`](./obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Подробная%20выжимка.md)
- [`Pandas quick reference`](./obsidian/03%20-%20Cheatsheets/Pandas%20-%20Quick%20Reference.md)
- [`Obsidian integration guide`](./docs/OBSIDIAN.md)

### One-time local setup

Configure a Vault once:

```bash
python3 scripts/setup_obsidian.py --vault "/path/to/your/Vault"
```

The personal path is stored in the gitignored `.obsidian-sync` file.

After setup, normal pulls/checkouts can refresh the Vault through repository hooks. You can also run the sync explicitly:

```bash
make notes
```

Preview without copying:

```bash
make notes-dry
```

**No Vault configured = no external side effects.** The sync exits safely without creating or copying anything outside the repository. Machines that do not use Obsidian can also exclude the `obsidian/` tree with sparse-checkout; see [`docs/OBSIDIAN.md`](./docs/OBSIDIAN.md).

## Quick start

Clone and create a virtual environment:

```bash
git clone https://github.com/JSwhiz/mlcourse.git
cd mlcourse
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the local learning environment:

```bash
make install
```

Run structural checks:

```bash
make check
```

Execute every notebook locally:

```bash
make notebooks
```

Start JupyterLab:

```bash
jupyter lab
```

## Repository structure

```text
mlcourse/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   ├── notebooks-ci.yml
│   │   └── repository-quality.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── .githooks/                 # local Obsidian sync hooks
├── docs/
│   └── OBSIDIAN.md
├── obsidian/                  # Russian long-term knowledge notes
├── scripts/
│   ├── pull.py
│   ├── setup_obsidian.py
│   ├── sync_obsidian.py
│   └── validate_repository.py
├── topic01_pandas_data_analysis/
│   ├── images/previews/
│   ├── notebooks/
│   └── README.md
├── .editorconfig
├── .gitignore
├── ATTRIBUTION.md
├── CONTRIBUTING.md
├── Makefile
├── requirements.txt
├── requirements-ci.txt
└── README.md
```

Future topics follow the same contract:

```text
topicXX_name/
├── notebooks/      # executable practice
├── data/           # only publishable data when needed
├── images/         # plots / visual previews
└── README.md       # English navigation and topic summary
```

Corresponding long-term notes live under `obsidian/01 - Topics/` and are written in Russian.

## Branching model

One course topic = one dedicated branch:

```text
topicXX-short-topic-name
```

Typical lifecycle:

```text
main
  ↓
create topic branch
  ↓
issues → notebooks → notes → README
  ↓
Notebook CI + Repository Quality
  ↓
pull request
  ↓
merge into main
```

Topic branches are intentionally kept after merge as a readable development history. Repository-wide maintenance can use branches such as `chore-*` and `docs-*`.

The complete definition of done is documented in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Design principles

- **Executable over decorative** — a green notebook badge means the code actually ran.
- **Understand before copying** — every important result should be explainable.
- **No hidden local state** — avoid absolute paths and undocumented environment assumptions.
- **Separate practice from memory** — notebooks show how; Obsidian notes preserve why.
- **Prefer evidence over claims** — descriptive analysis does not become causality by wording.
- **Keep navigation first-class** — every topic should be easy to enter from README, notebooks and notes.
- **Automate repetitive checks** — humans should spend time learning, not checking folder names.

## Attribution

This project builds on the public **mlcourse.ai** curriculum. Original course materials remain the work of their respective authors and contributors. Course-derived tasks retain their applicable attribution and license notices.

See [`ATTRIBUTION.md`](./ATTRIBUTION.md) for details.

---

<div align="center">

### Learn by building, executing, validating, linking and explaining.

[`Topic 01`](./topic01_pandas_data_analysis) · [`Obsidian`](./obsidian/00%20-%20Index/ML%20Course.md) · [`Contributing`](./CONTRIBUTING.md) · [`github.com/JSwhiz`](https://github.com/JSwhiz)

</div>
