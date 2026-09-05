<div align="center">

# Topic 01 · NumPy, Pandas & Data Analysis

### From numerical arrays to confident exploratory analysis

[![Topic](https://img.shields.io/badge/topic-01-111827)](../README.md)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Python-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/status-completed-22C55E)](./)

**Arrays · DataFrames · filtering · missing values · groupby · aggregation · EDA**

[← Repository](../README.md) · [Course materials](https://github.com/Yorko/mlcourse.ai/tree/main/jupyter_russian/topic01_pandas_data_analysis) · [Knowledge map](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Overview.md)

</div>

---

## Live notebooks

GitHub renders these notebooks directly in the browser. The NumPy and Titanic notebooks contain saved outputs verified against executed Python code, so opening them gives a real code + result preview without running Jupyter locally.

| Notebook | Focus | Preview |
|---|---|---|
| [`01_adult_pandas_analysis.ipynb`](./notebooks/01_adult_pandas_analysis.ipynb) | Complete UCI Adult Pandas assignment | [Open rendered notebook](./notebooks/01_adult_pandas_analysis.ipynb) |
| [`02_numpy_foundations.ipynb`](./notebooks/02_numpy_foundations.ipynb) | Arrays, indexing, masks, broadcasting, axis, vectorization | [Open rendered notebook](./notebooks/02_numpy_foundations.ipynb) |
| [`03_titanic_mini_eda.ipynb`](./notebooks/03_titanic_mini_eda.ipynb) | Filtering, missing data, groupby, derived features, mini-EDA | [Open rendered notebook](./notebooks/03_titanic_mini_eda.ipynb) |

> The Titanic notebook is intentionally self-contained: its compact representative sample lives inside the notebook, so the core practice does not depend on a local CSV path or an external download.

## Navigation

| Destination | Purpose |
|---|---|
| [Topic knowledge map](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Overview.md) | Central Obsidian navigation |
| [Detailed Russian summary](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Подробная%20выжимка.md) | Long-form Topic 01 reference |
| [NumPy note](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/NumPy%20-%20Основы.md) | Arrays, shapes, broadcasting and vectorization |
| [Series & DataFrame](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Pandas%20-%20Series%20and%20DataFrame.md) | Pandas data structures |
| [Indexing & Filtering](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Pandas%20-%20Indexing%20and%20Filtering.md) | Selection and boolean masks |
| [GroupBy & Aggregations](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Pandas%20-%20GroupBy%20and%20Aggregations.md) | Split → apply → combine |
| [Titanic practice note](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Titanic%20-%20Практика%20Pandas.md) | EDA workflow and interpretation |
| [Pandas quick reference](../obsidian/03%20-%20Cheatsheets/Pandas%20-%20Quick%20Reference.md) | Compact syntax reference |

## Goal

Topic 01 builds the data-manipulation layer needed before machine learning starts. The target is not memorizing APIs, but learning to translate an analytical question into a clean sequence of operations.

```text
question
   ↓
inspect structure
   ↓
select / filter
   ↓
transform
   ↓
aggregate
   ↓
validate
   ↓
interpret
```

## Learning checklist

| Block | Skill | Status |
|---|---|:---:|
| 01 | NumPy arrays, shape and dtype | 🟢 |
| 02 | Indexing, masks and broadcasting | 🟢 |
| 03 | Vectorized numerical operations | 🟢 |
| 04 | `Series` and `DataFrame` | 🟢 |
| 05 | Loading and inspecting tabular data | 🟢 |
| 06 | `.loc`, `.iloc` and conditional filtering | 🟢 |
| 07 | Sorting and descriptive statistics | 🟢 |
| 08 | Missing-value inspection and simple treatment | 🟢 |
| 09 | `groupby`, `agg` and multi-key grouping | 🟢 |
| 10 | Derived features and reshaping with `unstack()` | 🟢 |
| 11 | Converting numbers into analytical conclusions | 🟢 |

## Core toolkit

```python
import numpy as np
import pandas as pd
```

### NumPy

```python
x.shape
x.dtype
x[mask]
x.mean(axis=0)
x.reshape(...)
```

### Pandas

```python
df.head()
df.info()
df.describe()
df.isna().sum()

df.loc[condition, columns]
df.iloc[rows, columns]
df.sort_values(...)

df["category"].value_counts()
df.groupby(...).agg(...)
```

## What the practice covers

### UCI Adult

The main assignment exercises real analytical questions: category counts, subgroup means and standard deviations, proportions, education/income relationships, multi-key grouping, work-hours analysis and country-level comparisons.

### NumPy foundations

The NumPy notebook makes the numerical model explicit: shapes, slices, boolean masks, broadcasting, aggregation axes and vectorized transformations.

### Titanic mini-EDA

The Titanic notebook connects the individual Pandas tools into an EDA workflow: inspect → filter → group → handle missing values → create a feature → compare groups → interpret carefully.

## Expected outcomes

After Topic 01 I should be able to:

- reason about array and table shapes;
- recognize when broadcasting is valid;
- replace unnecessary Python loops with vectorized expressions;
- inspect an unfamiliar DataFrame before drawing conclusions;
- confidently select rows and columns;
- compose multiple boolean conditions;
- distinguish counts from proportions;
- calculate and interpret descriptive statistics;
- group by one or several categorical variables;
- inspect and consciously handle missing values;
- turn repeated conditions into derived features;
- distinguish descriptive evidence from causal claims.

## Knowledge workflow

The notebooks answer **how the analysis was performed**. The Russian Obsidian notes answer **what should remain in long-term memory**.

```text
course material
      ↓
notebook practice
      ↓
understanding
      ↓
Russian atomic notes
      ↓
Topic 01 summary
      ↓
linked Obsidian knowledge base
```

The repository's Obsidian sync workflow automatically mirrors these notes into the configured local Vault after pull/checkout. See [`docs/OBSIDIAN.md`](../docs/OBSIDIAN.md).

---

<div align="center">

### Topic 01 completed

[← `mlcourse`](../README.md) · [Knowledge map](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Overview.md) · [Detailed summary](../obsidian/01%20-%20Topics/Topic%2001%20-%20Pandas%20and%20Data%20Analysis/Topic%2001%20-%20Подробная%20выжимка.md)

</div>
