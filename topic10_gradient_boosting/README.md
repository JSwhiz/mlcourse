# Topic 10 · Gradient Boosting

[![Notebooks CI](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml)

Gradient boosting builds a strong model sequentially by correcting the residual/error structure of the current ensemble. This topic focuses on learning rate, tree complexity, early stopping, validation and comparison with bagged trees.

## Notebooks
- [`01_gradient_boosting_foundations.ipynb`](./notebooks/01_gradient_boosting_foundations.ipynb) — staged additive learning and key hyperparameters.
- [`02_boosting_vs_forest.ipynb`](./notebooks/02_boosting_vs_forest.ipynb) — controlled comparison with random forest and validation metrics.

Reasoning: `baseline → residual structure → weak learner → shrinkage → validation/early stopping → error analysis`.

Russian notes: [`Topic 10 — Подробная выжимка`](../obsidian/01%20-%20Topics/Topic%2010%20-%20Gradient%20Boosting/Topic%2010%20-%20Подробная%20выжимка.md).

[← Topic 09](https://github.com/JSwhiz/mlcourse/tree/main/topic09_time_series) · [Repository](../README.md)
