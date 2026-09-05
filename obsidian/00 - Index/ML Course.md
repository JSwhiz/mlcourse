---
type: index
course: mlcourse.ai
status: solid
tags:
  - machine-learning
  - mlcourse
---

# ML Course

Центральная навигационная заметка по моему прохождению `mlcourse.ai`.

## Темы

- [[Topic 01 - Overview|Topic 01 — NumPy, Pandas и анализ данных]]
- [[Topic 02 - Обзор|Topic 02 — Визуальный анализ данных]]
- [[Topic 03 - Подробная выжимка|Topic 03 — Decision Trees и k-NN]]
- [[Topic 04 - Подробная выжимка|Topic 04 — Линейные модели]]
- [[Topic 05 - Подробная выжимка|Topic 05 — Ансамбли и Random Forest]]
- [[Topic 06 - Подробная выжимка|Topic 06 — Feature Engineering и Feature Selection]]
- [[Topic 07 - Подробная выжимка|Topic 07 — PCA и кластеризация]]
- [[Topic 08 - Подробная выжимка|Topic 08 — SGD, hashing и online learning]]
- [[Topic 09 - Подробная выжимка|Topic 09 — Временные ряды]]
- [[Topic 10 - Подробная выжимка|Topic 10 — Gradient Boosting]]

## Как темы связаны

```text
01 данные и Pandas
 ↓
02 визуальный EDA
 ↓
03 базовая классификация: trees / k-NN
 ↓
04 линейные модели и regularization
 ↓
05 ансамбли и random forests
 ↓
06 качество признакового пространства
 ↓
07 unsupervised representation / clustering
 ↓
08 масштабируемое и online обучение
 ↓
09 отдельная логика данных во времени
 ↓
10 gradient boosting как сильный табличный ensemble
```

## Мои основные правила после курса

1. Сначала формулирую задачу, target и реальный сценарий использования.
2. До модели исследую данные и качество признаков.
3. Validation protocol выбираю до перебора моделей.
4. Любой preprocessing, который обучается на данных, помещаю внутрь pipeline/CV.
5. Test set не использую как инструмент настройки.
6. Для временных рядов сохраняю хронологию и проверяю availability каждого признака.
7. Более сложная модель должна доказать пользу против простого baseline.
8. Feature importance, correlation и clustering не интерпретирую как причинность.
9. В notebook фиксирую: вопрос → гипотеза → проверка → результат → ограничение.
10. В Obsidian сохраняю не синтаксис, а mental models и правила принятия решений.

## Быстрые переходы

### Topic 01–02
- [[Topic 01 - Подробная выжимка]]
- [[Pandas - Quick Reference]]
- [[Topic 02 - Подробная выжимка]]
- [[Визуализация - Как выбирать график]]
- [[Визуализация - Распределения и выбросы]]
- [[Визуализация - Корреляции]]

### Topic 03–10
- [[Topic 03 - Подробная выжимка]]
- [[Topic 04 - Подробная выжимка]]
- [[Topic 05 - Подробная выжимка]]
- [[Topic 06 - Подробная выжимка]]
- [[Topic 07 - Подробная выжимка]]
- [[Topic 08 - Подробная выжимка]]
- [[Topic 09 - Подробная выжимка]]
- [[Topic 10 - Подробная выжимка]]

## Репозиторий

- [GitHub-репозиторий](https://github.com/JSwhiz/mlcourse)
- [Topic 01](https://github.com/JSwhiz/mlcourse/tree/main/topic01_pandas_data_analysis)
- [Topic 02](https://github.com/JSwhiz/mlcourse/tree/main/topic02_data_visualization)
- [Topic 03](https://github.com/JSwhiz/mlcourse/tree/main/topic03_decision_trees_knn)
- [Topic 04](https://github.com/JSwhiz/mlcourse/tree/main/topic04_linear_models)
- [Topic 05](https://github.com/JSwhiz/mlcourse/tree/main/topic05_ensembles_random_forests)
- [Topic 06](https://github.com/JSwhiz/mlcourse/tree/main/topic06_feature_engineering_selection)
- [Topic 07](https://github.com/JSwhiz/mlcourse/tree/main/topic07_unsupervised_learning)
- [Topic 08](https://github.com/JSwhiz/mlcourse/tree/main/topic08_sgd_hashing_online_learning)
- [Topic 09](https://github.com/JSwhiz/mlcourse/tree/main/topic09_time_series)
- [Topic 10](https://github.com/JSwhiz/mlcourse/tree/main/topic10_gradient_boosting)

## Статусы заметок

- `learning` — активно изучаю;
- `review` — нужно повторить;
- `solid` — могу объяснить и применить без подсказок.
