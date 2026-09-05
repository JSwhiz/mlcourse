---
type: topic
topic: topic01
course: mlcourse.ai
status: solid
tags:
  - machine-learning
  - numpy
  - pandas
  - data-analysis
---

# Topic 01 — NumPy, Pandas и анализ данных

## Цель

Научиться превращать сырой табличный датасет в понятные ответы: понимать структуру массивов и таблиц, выбирать нужные данные, фильтровать, агрегировать, работать с пропусками и формулировать корректные выводы.

## Карта знаний

### NumPy

- [[NumPy - Основы]]

### Pandas

- [[Pandas - Series and DataFrame]]
- [[Pandas - Indexing and Filtering]]
- [[Pandas - GroupBy and Aggregations]]
- [[Pandas - Quick Reference]]

### Практика и итог

- [[Titanic - Практика Pandas]]
- [[Topic 01 - Подробная выжимка]]

## Практические ноутбуки

1. [UCI Adult — полный Pandas-анализ](https://github.com/JSwhiz/mlcourse/blob/topic01-pandas-data-analysis/topic01_pandas_data_analysis/notebooks/01_adult_pandas_analysis.ipynb)
2. [NumPy Foundations](https://github.com/JSwhiz/mlcourse/blob/topic01-pandas-data-analysis/topic01_pandas_data_analysis/notebooks/02_numpy_foundations.ipynb)
3. [Titanic mini-EDA](https://github.com/JSwhiz/mlcourse/blob/topic01-pandas-data-analysis/topic01_pandas_data_analysis/notebooks/03_titanic_mini_eda.ipynb)

## Что должно остаться после темы

- уверенное понимание `ndarray`, `Series` и `DataFrame`;
- понимание `shape`, `dtype`, `axis` и broadcasting;
- уверенная работа с `.loc`, `.iloc` и булевыми масками;
- умение проверять типы и пропуски;
- `value_counts`, `sort_values`, `groupby`, `agg`, `unstack`;
- понимание разницы между количеством и долей;
- привычка смотреть на размер группы вместе с её метрикой;
- векторизация вместо лишних Python-циклов;
- разделение описательного наблюдения и причинного вывода.

## Модель решения аналитической задачи

> **вопрос → структура данных → выбор/фильтр → преобразование → агрегат → проверка → интерпретация**

Если эта цепочка понятна, конкретный NumPy/Pandas-метод обычно находится естественно.

## GitHub

- [Папка Topic 01](https://github.com/JSwhiz/mlcourse/tree/topic01-pandas-data-analysis/topic01_pandas_data_analysis)
- [Ветка Topic 01](https://github.com/JSwhiz/mlcourse/tree/topic01-pandas-data-analysis)
- [Issues](https://github.com/JSwhiz/mlcourse/issues?q=Topic%2001)

## Итог

Topic 01 закрывает базовый слой, без которого сложно двигаться дальше в ML: данные сначала нужно уметь представить, проверить, выбрать и корректно описать — и только потом строить модели.

Для повторения всей темы одной заметкой: [[Topic 01 - Подробная выжимка]].
