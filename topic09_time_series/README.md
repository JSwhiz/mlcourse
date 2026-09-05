# Topic 09 · Time Series

[![Notebooks CI](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml)

Time changes the validation contract. This topic treats ordering, horizon, lagged information and rolling features as first-class modeling decisions.

## Notebooks
- [`01_time_series_foundations.ipynb`](./notebooks/01_time_series_foundations.ipynb) — trend, seasonality, lags, naive baseline and chronological holdout.
- [`02_time_aware_validation.ipynb`](./notebooks/02_time_aware_validation.ipynb) — `TimeSeriesSplit`, lag-feature regression and leakage checks.

Reasoning: `forecast horizon → available-at-time-t information → baseline → chronological validation → residual/drift analysis`.

Russian notes: [`Topic 09 — Подробная выжимка`](../obsidian/01%20-%20Topics/Topic%2009%20-%20Time%20Series/Topic%2009%20-%20Подробная%20выжимка.md).

[← Topic 08](../topic08_sgd_hashing_online_learning) · [Repository](../README.md)
