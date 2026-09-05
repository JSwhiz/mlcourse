<div align="center">

# Topic 01 · Pandas & Data Analysis

### Getting comfortable with tabular data using `pandas`

[![Topic](https://img.shields.io/badge/topic-01-111827)](../README.md)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-in%20progress-F59E0B)](./)

**DataFrames · filtering · aggregation · grouping · exploratory analysis**

[← Back to repository](../README.md) · [Course materials](https://github.com/Yorko/mlcourse.ai/tree/main/jupyter_russian)

</div>

---

## Goal

The first topic focuses on the core tools required to work confidently with tabular data in Python. The goal is to learn how to move from a raw dataset to clear answers to concrete analytical questions.

The central tool is **Pandas**, especially the `DataFrame` abstraction: loading data, inspecting dataset structure, selecting and filtering observations, calculating descriptive statistics, grouping records, and discovering useful patterns.

> This directory contains my own solutions, experiments, and takeaways. It is not a copy of the course material, but a working record of my progress through `mlcourse.ai`.

## Learning checklist

| Block | Skill | Status |
|---|---|:---:|
| 01 | Loading and inspecting data | 🟡 |
| 02 | Working with `Series` and `DataFrame` | 🟡 |
| 03 | Indexing and selecting data | 🟡 |
| 04 | Conditional filtering | 🟡 |
| 05 | Sorting | 🟡 |
| 06 | Descriptive statistics | 🟡 |
| 07 | `groupby` and aggregation | 🟡 |
| 08 | Applying functions to data | 🟡 |
| 09 | Turning results into conclusions | 🟡 |

**Legend:** 🟢 completed · 🟡 in progress · ⚪ planned

## Core toolkit

```python
import numpy as np
import pandas as pd
```

Operations that should feel natural by the end of this topic:

```python
df.head()
df.info()
df.describe()

df["column"]
df.loc[...]
df.iloc[...]

df[df["column"] > value]
df.sort_values(...)
df.groupby(...).agg(...)
```

The point is not to memorize methods. The important skill is understanding **which transformation or query is required to answer a particular question about the data**.

## Analysis flow

```text
Dataset
   ↓
Inspect
   ↓
Clean / Select
   ↓
Transform
   ↓
Aggregate
   ↓
Analyze
   ↓
Conclusion
```

For every exercise, I try to follow the same sequence:

1. understand the structure and meaning of the features;
2. identify which observations and columns are relevant;
3. obtain the result with Pandas;
4. verify that the result is interpreted correctly;
5. write a concise human-readable conclusion.

## Topic structure

The directory is intentionally kept lightweight at the beginning. As the topic grows, it may contain:

```text
topic01_pandas_data_analysis/
├── notebooks/
│   └── ...                  # solutions and experiments
├── data/
│   └── ...                  # data that can be published
├── images/
│   └── ...                  # plots and illustrations when useful
└── README.md
```

Empty directories are not created in advance. They appear only when there is real content to store in them.

## Expected outcomes

After completing Topic 01, I should be able to:

- quickly understand an unfamiliar tabular dataset;
- confidently select rows and columns;
- build compound filtering conditions;
- calculate and interpret descriptive statistics;
- group data and apply aggregations;
- answer analytical questions without unnecessary Python loops;
- explain the meaning of the result instead of merely printing a number.

## Notes & takeaways

This section will grow as exercises are completed.

> **Key idea:** good analysis starts with a well-formulated question, not with a Pandas method call.

---

<div align="center">

**Topic 01 / Pandas & Data Analysis**

[← `mlcourse`](../README.md) · [Repository roadmap](../README.md#progress)

</div>
