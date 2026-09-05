# Topic 06 · Feature Engineering & Feature Selection

[![Notebooks CI](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml)

Feature work is where domain assumptions become model inputs. This topic focuses on leakage-safe preprocessing, categorical encoding, interactions, missing values and selection inside a pipeline.

## Notebooks
- [`01_feature_engineering_pipeline.ipynb`](./notebooks/01_feature_engineering_pipeline.ipynb) — mixed numerical/categorical preprocessing with `ColumnTransformer`.
- [`02_feature_selection.ipynb`](./notebooks/02_feature_selection.ipynb) — filter/model-based selection evaluated by cross-validation.

Reasoning: `raw signal → representation hypothesis → leakage-safe transform → validation → keep only useful complexity`.

Russian notes: [`Topic 06 — Подробная выжимка`](../obsidian/01%20-%20Topics/Topic%2006%20-%20Feature%20Engineering%20and%20Selection/Topic%2006%20-%20Подробная%20выжимка.md).

[← Topic 05](../topic05_ensembles_random_forests) · [Repository](../README.md)
