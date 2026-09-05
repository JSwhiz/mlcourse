<div align="center">

# Topic 01 · Pandas & Data Analysis

### Exploratory data analysis with `pandas`

[![Topic](https://img.shields.io/badge/topic-01-111827)](../README.md)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-completed-22C55E)](./)

**DataFrames · filtering · aggregation · grouping · exploratory analysis**

[← Back to repository](../README.md) · [Course materials](https://github.com/Yorko/mlcourse.ai/tree/main/jupyter_russian) · [Obsidian notes](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Overview.md)

</div>

---

## Navigation

| Destination | Purpose |
|---|---|
| [Completed Adult analysis notebook](notebooks/01_adult_pandas_analysis.ipynb) | Reproducible practical work and answers |
| [Detailed Russian summary](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Подробная%20выжимка.md) | Full long-term study note for Obsidian |
| [Topic overview](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Overview.md) | Knowledge map |
| [Series & DataFrame](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Pandas%20-%20Series%20and%20DataFrame.md) | Core data structures |
| [Indexing & Filtering](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Pandas%20-%20Indexing%20and%20Filtering.md) | Selection and boolean masks |
| [GroupBy & Aggregations](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Pandas%20-%20GroupBy%20and%20Aggregations.md) | Split-apply-combine |
| [Quick reference](../obsidian/03%20-%20Cheatsheets/Pandas%20-%20Quick%20Reference.md) | Compact Pandas cheatsheet |

## Goal

Learn to move from a raw tabular dataset to reproducible, interpretable answers. Topic 01 covers the Pandas workflow required for exploratory data analysis: loading and inspecting data, selecting observations, filtering, descriptive statistics, grouping, aggregation, and communicating conclusions.

## Learning checklist

| Block | Skill | Status |
|---|---|:---:|
| 01 | Loading and inspecting data | 🟢 |
| 02 | Working with `Series` and `DataFrame` | 🟢 |
| 03 | Indexing and selecting data | 🟢 |
| 04 | Conditional filtering | 🟢 |
| 05 | Sorting | 🟢 |
| 06 | Descriptive statistics | 🟢 |
| 07 | `groupby` and aggregation | 🟢 |
| 08 | Vectorized and string operations | 🟢 |
| 09 | Turning results into conclusions | 🟢 |

## Practical work

The main notebook solves the open mlcourse.ai demo assignment on the UCI Adult dataset and adds explanations around every analytical step.

Covered operations include:

```python
df.head()
df.info()
df.describe()
df["column"].value_counts()
df.loc[condition, "column"]
df.iloc[...]
df.sort_values(...)
df.groupby(...).agg(...)
df.isna().sum()
```

The notebook loads `adult.data.csv` from a local `data/` directory when available and otherwise falls back to the public mlcourse.ai raw dataset, so it remains easy to run without committing a duplicate dataset.

## Analysis model

```text
Question
   ↓
Understand the data
   ↓
Select rows and columns
   ↓
Transform / aggregate
   ↓
Validate the result
   ↓
Interpret without overclaiming
```

The key lesson is that Pandas syntax is secondary. The transferable skill is decomposing a question into a sequence of operations over a table.

## Key takeaways

- Boolean masks are the foundation of expressive filtering.
- `.loc` is the clearest default for condition-based row/column selection.
- The mean of a boolean Series is a convenient way to calculate a share.
- `value_counts()` is a fast first look at categorical features.
- `groupby()` implements the split → apply → combine pattern.
- `agg()` makes multi-statistic summaries explicit and readable.
- Vectorized Pandas operations should usually replace manual Python loops over rows.
- Group comparisons should often use shares rather than raw counts.
- Descriptive relationships do not establish causality.

For the complete Russian explanation, examples, common mistakes, and mental models, see [Topic 01 — Подробная выжимка](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Подробная%20выжимка.md).

## Repository structure

```text
topic01_pandas_data_analysis/
├── notebooks/
│   └── 01_adult_pandas_analysis.ipynb
└── README.md

obsidian/
├── 01 - Topics/
│   └── Topic 01 - Pandas and Data Analysis/
│       ├── Topic 01 - Overview.md
│       ├── Topic 01 - Подробная выжимка.md
│       ├── Pandas - Series and DataFrame.md
│       ├── Pandas - Indexing and Filtering.md
│       └── Pandas - GroupBy and Aggregations.md
└── 03 - Cheatsheets/
    └── Pandas - Quick Reference.md
```

## Source and attribution

The practical task is based on the open demo materials of [mlcourse.ai](https://github.com/Yorko/mlcourse.ai) by Yury Kashnitsky, distributed under CC BY-NC-SA 4.0. The notebook in this repository contains my own solution structure, code, explanations, and conclusions.

---

<div align="center">

**Topic 01 / completed**

[← `mlcourse`](../README.md) · [Notebook](notebooks/01_adult_pandas_analysis.ipynb) · [Detailed notes](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Подробная%20выжимка.md)

</div>
