# Topic 08 · SGD, Feature Hashing & Online Learning

[![Notebooks CI](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml/badge.svg)](https://github.com/JSwhiz/mlcourse/actions/workflows/notebooks-ci.yml)

The course introduces scalable learning through stochastic gradient descent, hashing and Vowpal Wabbit. This repository keeps the core ideas reproducible with scikit-learn while documenting how they map to large-scale online systems.

## Notebooks
- [`01_sgd_from_batches.ipynb`](./notebooks/01_sgd_from_batches.ipynb) — batch-by-batch `partial_fit`, convergence and scaling.
- [`02_feature_hashing.ipynb`](./notebooks/02_feature_hashing.ipynb) — stateless hashing for high-cardinality sparse features.

Reasoning: `memory/latency constraint → streaming representation → incremental update → online metric → drift awareness`.

Russian notes: [`Topic 08 — Подробная выжимка`](../obsidian/01%20-%20Topics/Topic%2008%20-%20SGD%20Hashing%20and%20Online%20Learning/Topic%2008%20-%20Подробная%20выжимка.md).

[← Topic 07](https://github.com/JSwhiz/mlcourse/tree/main/topic07_unsupervised_learning) · [Repository](../README.md)
