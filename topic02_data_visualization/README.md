<div align="center">

# Topic 02 · Visual Data Analysis

### Turning analytical questions into useful visual evidence

[![Topic](https://img.shields.io/badge/topic-02-111827)](../README.md)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0)](https://seaborn.pydata.org/)
[![Notebooks CI](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml)
[![Status](https://img.shields.io/badge/status-in%20progress-F59E0B)](./)

**Distributions · categories · comparisons · correlations · EDA · visual reasoning**

[← Repository](../README.md) · [Course Topic 02](https://mlcourse.ai/book/topic02/topic02_intro.html) · [Knowledge map](../obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Topic%2002%20-%20Обзор.md)

</div>

---

## Goal

Topic 02 is about using visualization as an analytical instrument rather than decoration. Every plot in this topic follows the same reasoning pattern:

```text
question
   ↓
feature types
   ↓
choose the plot
   ↓
inspect the pattern
   ↓
check with numbers
   ↓
state a careful conclusion
```

The notebooks deliberately include short **Reasoning** blocks. They document the useful, reviewable analytical logic — what is being tested, why a chart is appropriate, what is visible, and what cannot be concluded from the chart alone.

## Notebooks

| Notebook | Focus | Status |
|---|---|:---:|
| [`01_visual_analysis_toolbox.ipynb`](./notebooks/01_visual_analysis_toolbox.ipynb) | Core visual-analysis patterns on telecom churn | 🟡 |
| [`02_telecom_churn_visual_eda.ipynb`](./notebooks/02_telecom_churn_visual_eda.ipynb) | End-to-end visual EDA and feature hypotheses | 🟡 |
| [`03_cardio_visual_assignment.ipynb`](./notebooks/03_cardio_visual_assignment.ipynb) | mlcourse.ai cardiovascular demo assignment | 🟡 |

The data is loaded from the official public `mlcourse.ai` repository so the analysis uses the original course datasets rather than toy replacements.

## Learning checklist

| Block | Skill | Status |
|---|---|:---:|
| 01 | Match a chart to an analytical question | 🟡 |
| 02 | Histograms and KDE | 🟡 |
| 03 | Box plots and violin plots | 🟡 |
| 04 | Count plots and grouped categorical comparisons | 🟡 |
| 05 | Scatter plots and multivariate encoding | 🟡 |
| 06 | Pearson and Spearman heatmaps | 🟡 |
| 07 | Compare distributions by target | 🟡 |
| 08 | Detect suspicious observations visually | 🟡 |
| 09 | Build and test feature hypotheses | 🟡 |
| 10 | Avoid causal claims from descriptive plots | 🟡 |

## The rule I want to keep

A visualization is useful only when I can finish this sentence:

> **I am drawing this chart because I want to check whether ...**

If I cannot formulate the question, the chart is probably decorative.

## Knowledge notes

All personal notes that sync to Obsidian are written in Russian:

- [Topic 02 — Обзор](../obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Topic%2002%20-%20Обзор.md)
- [Как выбирать график](../obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Визуализация%20-%20Как%20выбирать%20график.md)
- [Распределения и выбросы](../obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Визуализация%20-%20Распределения%20и%20выбросы.md)
- [Корреляции](../obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Визуализация%20-%20Корреляции.md)
- [Подробная выжимка](../obsidian/01%20-%20Topics/Topic%2002%20-%20Visual%20Data%20Analysis/Topic%2002%20-%20Подробная%20выжимка.md)

## Definition of done

Topic 02 is complete when:

- every notebook runs top-to-bottom in CI;
- every chart has an explicit analytical purpose;
- visual conclusions are checked with numerical summaries where appropriate;
- the official cardiovascular demo assignment is reproduced;
- Russian Obsidian notes contain the reusable concepts;
- README navigation and previews are up to date.

---

<div align="center">

**Topic 02 / Visual Data Analysis**

[← Topic 01](../topic01_pandas_data_analysis) · [Repository](../README.md)

</div>
