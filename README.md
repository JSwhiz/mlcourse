<div align="center">

# Machine Learning Course

### A reproducible, CI-verified learning repository built around `mlcourse.ai`

[![Notebooks CI](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml)
[![Repository Quality](https://github.com/JSwhiz/mlcourse/actions/workflows/repository-quality.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/repository-quality.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Course](https://img.shields.io/badge/mlcourse.ai-Topics%2001–10-111827)](https://mlcourse.ai/)

**10 topics · executable notebooks · Russian Obsidian knowledge base · reproducible validation**

[Course map](#course-map) · [Knowledge base](#knowledge-base--obsidian) · [Reproducibility](#reproducibility) · [Quick start](#quick-start) · [Workflow](./CONTRIBUTING.md)

</div>

---

## About

This repository is my personal implementation of the core `mlcourse.ai` curriculum. I keep three connected layers for every topic:

```text
course concept
      ↓
executable notebook practice
      ↓
Russian long-term notes in Obsidian
```

The learning trail is deliberately explicit:

> **question → hypothesis → method → validation → result → limitation → reusable knowledge**

The goal is not to collect notebooks. The goal is to build material that I can rerun, explain, defend and reuse.

## Course map

| # | Topic | Status | Practice | Russian notes |
|---:|---|:---:|---|---|
| 01 | NumPy, Pandas & exploratory data analysis | ✅ | [`Topic 01`](./topic01_pandas_data_analysis) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Подробная%20выжимка.md) |
| 02 | Visual data analysis | ✅ | [`Topic 02`](./topic02_data_visualization) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Topic%2002%20-%20Подробная%20выжимка.md) |
| 03 | Classification, decision trees & k-NN | ✅ | [`Topic 03`](./topic03_decision_trees_knn) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2003%20-%20Decision%20Trees%20and%20kNN/Topic%2003%20-%20Подробная%20выжимка.md) |
| 04 | Linear models | ✅ | [`Topic 04`](./topic04_linear_models) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2004%20-%20Linear%20Models/Topic%2004%20-%20Подробная%20выжимка.md) |
| 05 | Bagging, random forests & feature importance | ✅ | [`Topic 05`](./topic05_ensembles_random_forests) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2005%20-%20Ensembles%20and%20Random%20Forests/Topic%2005%20-%20Подробная%20выжимка.md) |
| 06 | Feature engineering & feature selection | ✅ | [`Topic 06`](./topic06_feature_engineering_selection) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2006%20-%20Feature%20Engineering%20and%20Selection/Topic%2006%20-%20Подробная%20выжимка.md) |
| 07 | PCA & clustering | ✅ | [`Topic 07`](./topic07_unsupervised_learning) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2007%20-%20Unsupervised%20Learning/Topic%2007%20-%20Подробная%20выжимка.md) |
| 08 | SGD, hashing & online learning | ✅ | [`Topic 08`](./topic08_sgd_hashing_online_learning) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2008%20-%20SGD%20Hashing%20and%20Online%20Learning/Topic%2008%20-%20Подробная%20выжимка.md) |
| 09 | Time series | ✅ | [`Topic 09`](./topic09_time_series) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2009%20-%20Time%20Series/Topic%2009%20-%20Подробная%20выжимка.md) |
| 10 | Gradient boosting | ✅ | [`Topic 10`](./topic10_gradient_boosting) | [`Summary`](./obsidian/01%20-%20Topics/Topic%2010%20-%20Gradient%20Boosting/Topic%2010%20-%20Подробная%20выжимка.md) |

### What the later topics emphasize

- **Topic 03:** fair validation, tree complexity, distance geometry and k-NN scaling.
- **Topic 04:** OLS/logistic regression, regularization, learning curves and coefficient interpretation.
- **Topic 05:** variance reduction, bagging, random forests and cautious feature importance.
- **Topic 06:** leakage-safe feature engineering and selection inside pipelines.
- **Topic 07:** PCA, clustering, geometry and limits of unsupervised interpretation.
- **Topic 08:** incremental SGD, feature hashing, online constraints and drift awareness.
- **Topic 09:** forecasting horizon, lag features, chronological validation and time leakage.
- **Topic 10:** additive boosting, shrinkage, staged validation and comparison with random forests.

## Reproducibility

Two GitHub Actions workflows protect the repository.

### Notebooks CI

[`Notebooks CI`](./.github/workflows/notebooks-ci.yml) discovers `topic*/notebooks/*.ipynb`, creates a clean Python environment and executes every notebook from top to bottom.

A notebook is considered healthy only if its actual code executes successfully. Successful runs also publish executed notebooks as short-lived Actions artifacts.

### Repository Quality

[`Repository Quality`](./.github/workflows/repository-quality.yml) validates topic structure, nbformat JSON, important relative Markdown links and the Obsidian index.

Local equivalents:

```bash
make check
make notebooks
```

## Knowledge base / Obsidian

The versioned knowledge layer lives under [`obsidian/`](./obsidian). Personal notes intended for the Vault are written in **Russian**.

The central entry point is [`ML Course`](./obsidian/00%20-%20Index/ML%20Course.md).

```text
GitHub / notebooks                     Obsidian / knowledge
──────────────────────────────────     ──────────────────────────────────
reproducible experiments               concepts in my own words
code and outputs                       mental models and caveats
CI verification             ↔          wikilinks between topics
version history                        material for long-term review
```

### Obsidian sync

One-time setup:

```bash
python3 scripts/setup_obsidian.py --vault "/path/to/your/Vault"
```

Then:

```bash
make notes
```

Dry run:

```bash
make notes-dry
```

**No Vault configured = no external side effects.** The sync exits safely without copying anything outside the repository.

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

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Repository structure

```text
mlcourse/
├── .github/                      # CI, issue and PR templates
├── .githooks/                    # optional local automation
├── docs/                         # repository documentation
├── obsidian/                     # Russian long-term knowledge base
├── scripts/                      # validation and Obsidian sync tools
├── topic01_pandas_data_analysis/
├── topic02_data_visualization/
├── topic03_decision_trees_knn/
├── topic04_linear_models/
├── topic05_ensembles_random_forests/
├── topic06_feature_engineering_selection/
├── topic07_unsupervised_learning/
├── topic08_sgd_hashing_online_learning/
├── topic09_time_series/
├── topic10_gradient_boosting/
├── CONTRIBUTING.md
├── Makefile
├── requirements.txt
└── README.md
```

Every topic follows the same contract:

```text
topicXX_name/
├── notebooks/      # executable practice
└── README.md       # English navigation and topic summary
```

Long-term notes live under `obsidian/01 - Topics/`.

## Branching model

One course topic = one dedicated branch:

```text
topicXX-short-topic-name
```

Lifecycle:

```text
main
  ↓
topic branch
  ↓
notebooks + notes + README
  ↓
Notebooks CI + Repository Quality
  ↓
PR
  ↓
merge into main
```

Topic branches are intentionally retained after merge as a readable development history. Repository-wide maintenance uses `chore-*` / `docs-*` branches.

## Design principles

- **Executable over decorative** — code must run, not merely look plausible.
- **Question before technique** — every chart/model should answer a concrete question.
- **Validation is part of the model** — splits, preprocessing and feature availability matter.
- **No hidden local state** — avoid undocumented absolute paths and manual assumptions.
- **Separate practice from memory** — notebooks show how; Obsidian preserves why.
- **Prefer evidence over claims** — association, importance and clustering are not causality.
- **Keep navigation first-class** — every topic is reachable from the root and knowledge index.

## Attribution

This project builds on the public **mlcourse.ai** curriculum. Original course materials remain the work of their respective authors and contributors. Course-derived tasks retain their applicable attribution and license notices.

See [`ATTRIBUTION.md`](./ATTRIBUTION.md).

---

<div align="center">

### Course implementation complete: Topics 01–10

[`Topic 01`](./topic01_pandas_data_analysis) · [`Topic 05`](./topic05_ensembles_random_forests) · [`Topic 10`](./topic10_gradient_boosting) · [`Obsidian`](./obsidian/00%20-%20Index/ML%20Course.md)

</div>
