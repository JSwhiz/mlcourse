<div align="center">

# Machine Learning Course

### A reproducible learning repository built around `mlcourse.ai`

[![Notebooks CI](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml)
[![Repository Quality](https://github.com/JSwhiz/mlcourse/actions/workflows/repository-quality.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/repository-quality.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Course](https://img.shields.io/badge/course-mlcourse.ai-111827)](https://mlcourse.ai/)

**Notebooks · experiments · Russian knowledge notes · CI-verified results**

[Progress](#progress) · [Topic 01](./topic01_pandas_data_analysis) · [Topic 02](./topic02_data_visualization) · [Knowledge base](#knowledge-base--obsidian) · [Quick start](#quick-start) · [Workflow](./CONTRIBUTING.md)

</div>

---

## About

This repository is my personal workspace for the **mlcourse.ai** curriculum. Each topic combines three connected layers:

```text
course material
      ↓
executable notebook practice
      ↓
Russian long-term knowledge notes in Obsidian
```

The goal is not to accumulate notebooks. The goal is to build a learning trail that is **executable, reviewable and useful later**:

> **question → hypothesis → experiment → result → interpretation → reusable knowledge**

For analytical work I preserve concise reasoning blocks in notebooks: what I want to test, why I choose a method or chart, how I check the result, and what conclusion is justified. Important notebooks are expected to run top-to-bottom in a clean GitHub Actions environment.

## Progress

| # | Topic | Status | Practice | Knowledge |
|---:|---|:---:|---|---|
| 01 | NumPy, Pandas & exploratory data analysis | ✅ Completed | [`Topic 01`](./topic01_pandas_data_analysis) | [`Knowledge map`](./obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Overview.md) |
| 02 | Visual data analysis | ✅ Completed | [`Topic 02`](./topic02_data_visualization) | [`Knowledge map`](./obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Topic%2002%20-%20Обзор.md) |
| 03 | Classification, decision trees & k-NN | ⚪ Planned | — | — |
| 04 | Linear models | ⚪ Planned | — | — |
| 05 | Ensembles & random forests | ⚪ Planned | — | — |
| 06 | Feature engineering | ⚪ Planned | — | — |
| 07 | Unsupervised learning | ⚪ Planned | — | — |
| 08 | Time series fundamentals | ⚪ Planned | — | — |

### Topic 01 at a glance

Topic 01 contains three executable notebooks:

- [`01_adult_pandas_analysis.ipynb`](./topic01_pandas_data_analysis/notebooks/01_adult_pandas_analysis.ipynb) — UCI Adult analysis;
- [`02_numpy_foundations.ipynb`](./topic01_pandas_data_analysis/notebooks/02_numpy_foundations.ipynb) — arrays, masks, broadcasting and vectorization;
- [`03_titanic_mini_eda.ipynb`](./topic01_pandas_data_analysis/notebooks/03_titanic_mini_eda.ipynb) — filtering, missing values, grouping and derived features.

### Topic 02 at a glance

Topic 02 moves from tabular operations to **visual reasoning**. The notebooks are structured around explicit analytical questions instead of collections of unrelated charts:

- [`01_visual_analysis_toolbox.ipynb`](./topic02_data_visualization/notebooks/01_visual_analysis_toolbox.ipynb) — chart selection and core visualization patterns;
- [`02_telecom_churn_visual_eda.ipynb`](./topic02_data_visualization/notebooks/02_telecom_churn_visual_eda.ipynb) — visual EDA on the official telecom churn dataset;
- [`03_cardio_visual_assignment.ipynb`](./topic02_data_visualization/notebooks/03_cardio_visual_assignment.ipynb) — cardiovascular demo assignment on the official 70,000-row dataset.

The key discipline for this topic is:

```text
question → chart → observation → numerical check → careful conclusion
```

The Topic 02 README contains clickable previews derived from values produced by the CI-executed notebooks.

## Reproducibility

Two GitHub Actions workflows protect the repository.

### Notebooks CI

[`Notebooks CI`](./.github/workflows/notebooks-ci.yml) discovers `topic*/notebooks/*.ipynb`, installs a clean Python environment and executes every notebook from top to bottom.

If one code cell raises an error, the workflow fails. Successful runs upload executed notebooks as short-lived Actions artifacts.

### Repository Quality

[`Repository Quality`](./.github/workflows/repository-quality.yml) validates:

- topic directories follow the expected structure;
- each topic has a README and notebook directory;
- notebook files are valid nbformat 4 JSON;
- important relative Markdown links resolve inside the repository;
- the Obsidian course index exists.

Local equivalents:

```bash
make check
make notebooks
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
- [`Topic 01 — detailed summary`](./obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Подробная%20выжимка.md)
- [`Topic 02 — knowledge map`](./obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Topic%2002%20-%20Обзор.md)
- [`Topic 02 — detailed summary`](./obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Topic%2002%20-%20Подробная%20выжимка.md)
- [`Visualization quick reference`](./obsidian/03%20-%20Cheatsheets/Визуализация%20-%20Быстрая%20шпаргалка.md)
- [`Obsidian integration guide`](./docs/OBSIDIAN.md)

### One-time local setup

```bash
python3 scripts/setup_obsidian.py --vault "/path/to/your/Vault"
```

The personal path is stored in the gitignored `.obsidian-sync` file. After setup, normal pulls/checkouts can refresh the Vault through repository hooks.

Explicit sync:

```bash
make notes
```

Preview only:

```bash
make notes-dry
```

**No Vault configured = no external side effects.** The sync exits safely without creating or copying anything outside the repository.

## Quick start

```bash
git clone https://github.com/JSwhiz/mlcourse.git
cd mlcourse
python3 -m venv .venv
source .venv/bin/activate
make install
make check
jupyter lab
```

Windows PowerShell activation:

```powershell
.venv\Scripts\Activate.ps1
```

## Repository structure

```text
mlcourse/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── PULL_REQUEST_TEMPLATE.md
├── .githooks/
├── docs/
├── obsidian/
│   ├── 00 - Index/
│   └── 01 - Topics/
├── scripts/
├── topic01_pandas_data_analysis/
│   ├── images/previews/
│   ├── notebooks/
│   └── README.md
├── topic02_data_visualization/
│   ├── images/previews/
│   ├── notebooks/
│   └── README.md
├── ATTRIBUTION.md
├── CONTRIBUTING.md
├── Makefile
├── requirements.txt
└── README.md
```

Each future topic follows the same contract:

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
issues → notebooks → notes → previews → README
  ↓
Notebooks CI + Repository Quality
  ↓
pull request
  ↓
merge into main
```

Topic branches are intentionally kept after merge as readable development history. Repository-wide maintenance can use `chore-*` and `docs-*` branches.

## Design principles

- **Executable over decorative** — a green notebook badge means the code actually ran.
- **Question before technique** — a chart or method must answer a concrete analytical question.
- **Understand before copying** — every important result should be explainable.
- **No hidden local state** — avoid absolute paths and undocumented environment assumptions.
- **Separate practice from memory** — notebooks show how; Obsidian notes preserve why.
- **Prefer evidence over claims** — descriptive analysis does not become causality by wording.
- **Keep navigation first-class** — every topic should be easy to enter from README, notebooks and notes.
- **Automate repetitive checks** — humans should spend time learning, not checking folder names.

## Attribution

This project builds on the public **mlcourse.ai** curriculum. Original course materials remain the work of their respective authors and contributors. Course-derived tasks retain their applicable attribution and license notices.

See [`ATTRIBUTION.md`](./ATTRIBUTION.md).

---

<div align="center">

### Learn by building, executing, validating, linking and explaining.

[`Topic 01`](./topic01_pandas_data_analysis) · [`Topic 02`](./topic02_data_visualization) · [`Obsidian`](./obsidian/00%20-%20Index/ML%20Course.md) · [`github.com/JSwhiz`](https://github.com/JSwhiz)

</div>
