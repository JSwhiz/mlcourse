<div align="center">

# Machine Learning Course

### A hands-on journey through `mlcourse.ai` — from data analysis to classical machine learning

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Course](https://img.shields.io/badge/course-mlcourse.ai-111827)](https://mlcourse.ai/)
[![Status](https://img.shields.io/badge/status-in%20progress-22C55E)](https://github.com/JSwhiz/mlcourse)

**Solutions · experiments · notes · takeaways**

[Course](https://mlcourse.ai/) · [Russian materials](https://github.com/Yorko/mlcourse.ai/tree/main/jupyter_russian) · [Progress](#progress) · [Getting started](#getting-started)

</div>

---

## About

This repository is my personal workspace for the **mlcourse.ai** curriculum. I use it to work through each topic, solve practical assignments, test alternative approaches, and document the reasoning behind the results.

The goal is not to collect finished notebooks, but to build a clear and reproducible learning trail:

**problem → exploration → solution → result → takeaway**

> The original course materials belong to their respective authors. This repository contains my own solutions, notes, experiments, and data that can be shared publicly.

## Progress

| # | Topic | Status | Materials |
|---:|---|:---:|---|
| 01 | Pandas & exploratory data analysis | 🟡 In progress | [`topic01_pandas_data_analysis`](./topic01_pandas_data_analysis) |
| 02 | Data visualization | ⚪ Planned | — |
| 03 | Classification, decision trees & k-NN | ⚪ Planned | — |
| 04 | Linear models | ⚪ Planned | — |
| 05 | Ensembles & random forests | ⚪ Planned | — |
| 06 | Feature engineering | ⚪ Planned | — |
| 07 | Unsupervised learning | ⚪ Planned | — |
| 08 | Time series fundamentals | ⚪ Planned | — |

<sub>The roadmap will evolve as I move through the course.</sub>

## Tech stack

- **Python 3.11+** — primary language
- **JupyterLab** — interactive analysis and experimentation
- **Pandas / NumPy** — data processing and numerical computing
- **Matplotlib / Seaborn** — visualization
- **Scikit-learn** — classical machine learning

The stack will expand as later topics require additional tools.

## Repository structure

```text
mlcourse/
├── topic01_pandas_data_analysis/
│   └── README.md
├── .gitignore
└── README.md
```

Each topic is kept self-contained and may include:

```text
topicXX_name/
├── notebooks/      # solutions and experiments
├── data/           # publishable datasets
├── images/         # plots and illustrations
└── README.md       # scope, notes and key takeaways
```

## Getting started

Clone the repository:

```bash
git clone https://github.com/JSwhiz/mlcourse.git
cd mlcourse
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install the core dependencies:

```bash
pip install jupyterlab pandas numpy matplotlib seaborn scikit-learn
```

Start JupyterLab:

```bash
jupyter lab
```

## Workflow

For each topic, I try to keep the process consistent:

1. Study the relevant course section and reference notebook.
2. Reproduce the core ideas independently.
3. Solve the exercises and test alternative approaches.
4. Record useful observations, mistakes, and patterns.
5. Keep a clean final solution with concise takeaways.

That way, the repository stays useful as a learning record rather than becoming a dump of disconnected notebooks.

## Branching convention

Each course topic is developed in its **own branch**. The `main` branch stays clean and represents the consolidated state of the course repository.

Branch naming convention:

```text
topicXX-short-topic-name
```

Examples:

```text
topic01-pandas-data-analysis
topic02-data-visualization
topic03-classification-trees-knn
```

The lifecycle of a topic is:

```text
main
  ↓
create topic branch
  ↓
work through exercises / notebooks / notes
  ↓
track work with issues
  ↓
review the topic
  ↓
merge back into main
```

Rules:

- one topic = one dedicated branch;
- topic-specific commits go to that branch, not directly to `main`;
- issues are used as the working checklist for each topic;
- the branch is merged only when the topic is in a clean, reproducible state;
- after merging, `main` should contain the finished version of that topic.

## Principles

- **Understand before copying** — every solution should be explainable.
- **Keep it reproducible** — notebooks should run top-to-bottom without hidden state.
- **Prefer clean experiments** — temporary exploration should not clutter the final version.
- **Write down the takeaway** — the result matters less without the reasoning behind it.
- **Increase complexity gradually** — from data analysis to model building and evaluation.

---

<div align="center">

### Learn by building, testing, and explaining.

[`github.com/JSwhiz`](https://github.com/JSwhiz)

</div>
