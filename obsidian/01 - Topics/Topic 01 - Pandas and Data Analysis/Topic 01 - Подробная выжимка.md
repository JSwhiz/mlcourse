---
type: summary
topic: topic01
course: mlcourse.ai
status: solid
tags:
  - numpy
  - pandas
  - data-analysis
  - python
  - конспект
---

# Topic 01 — подробная выжимка по NumPy и Pandas

[[ML Course]] · [[Topic 01 - Overview]] · [[NumPy - Основы]] · [[Pandas - Quick Reference]] · [[Titanic - Практика Pandas]]

## 1. Главная идея темы

До машинного обучения нужно научиться уверенно работать с данными. Topic 01 строит базовый аналитический слой: сначала численные массивы NumPy, затем табличные структуры Pandas и, наконец, связный EDA-процесс.

Базовая цепочка:

> **вопрос → понять структуру → выбрать данные → отфильтровать → преобразовать → сгруппировать → посчитать → проверить → интерпретировать.**

## 2. NumPy: численная основа

Главный объект NumPy — `ndarray`, однородный многомерный массив.

```python
import numpy as np
x = np.array([1, 2, 3, 4])
```

Первое, что важно понимать у массива:

```python
x.shape
x.ndim
x.dtype
x.size
```

### Индексация

```python
A = np.arange(12).reshape(3, 4)
A[0]
A[:, 1]
A[1:, 2:]
```

### Булевы маски

```python
A[A > 5]
A[A % 2 == 0]
```

Маска — массив `True/False`, который выбирает элементы. Та же идея позже используется в Pandas.

### Broadcasting

```python
A + np.array([10, 20, 30, 40])
```

NumPy умеет виртуально расширять совместимые формы. Размерности сравниваются справа налево: они должны совпадать или одна из них должна быть равна `1`.

### `axis`

```python
A.mean(axis=0)  # по каждому столбцу
A.mean(axis=1)  # по каждой строке
```

Полезная модель: указанная ось «схлопывается».

### Векторизация

Вместо цикла:

```python
result = []
for value in x:
    result.append(value ** 2 + 3 * value)
```

лучше:

```python
result = x ** 2 + 3 * x
```

Векторизация обычно короче, яснее и быстрее.

## 3. Pandas: Series и DataFrame

`Series` — одномерная структура с индексом. `DataFrame` — двумерная таблица из согласованных Series.

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

После загрузки нельзя сразу делать выводы. Сначала:

```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

Проверяем:

- размер таблицы;
- смысл строки;
- смысл признаков;
- типы;
- пропуски;
- подозрительные значения;
- числовые и категориальные признаки.

## 4. Выбор: `[]`, `.loc`, `.iloc`

```python
df["age"]
df[["age", "salary"]]
```

`.loc` — по меткам и логическим условиям:

```python
df.loc[df["sex"] == "Female", "age"]
```

`.iloc` — по физическим позициям:

```python
df.iloc[:5, :3]
```

Для аналитических условий обычно удобнее `.loc`.

## 5. Булева фильтрация

```python
df[df["age"] >= 30]
```

Несколько условий:

```python
df[(df["age"] >= 30) & (df["sex"] == "Female")]
df[(df["salary"] == ">50K") | (df["hours-per-week"] > 60)]
df[~df["native-country"].isin(["United-States", "Canada"])]
```

Операторы:

- `&` — И;
- `|` — ИЛИ;
- `~` — НЕ.

Условия при комбинировании заключаются в скобки.

## 6. Доля через среднее булевой маски

`True` ведёт себя как `1`, `False` — как `0`.

```python
(df["native-country"] == "Germany").mean()
```

Поэтому среднее логической маски — доля строк, где условие истинно.

```python
df["salary"].eq(">50K").mean()
```

Для процентов умножаем на 100.

## 7. `value_counts()`

```python
df["sex"].value_counts()
df["sex"].value_counts(normalize=True)
```

Первый вариант — количества, второй — доли.

Это один из первых инструментов для категориального столбца.

## 8. Описательная статистика

```python
df["age"].mean()
df["age"].median()
df["age"].std()
df["age"].min()
df["age"].max()
```

Среднее чувствительно к выбросам. Медиана устойчивее. Стандартное отклонение показывает масштаб разброса.

## 9. `groupby`: split → apply → combine

```python
df.groupby("salary")["age"].mean()
```

Логика:

1. split — разделить строки на группы;
2. apply — посчитать функцию внутри каждой группы;
3. combine — собрать результаты.

Несколько статистик:

```python
df.groupby("salary")["age"].agg(["mean", "median", "std", "min", "max"])
```

Несколько ключей:

```python
df.groupby(["race", "sex"])["age"].describe()
```

## 10. `agg()`

```python
df.groupby("category").agg({
    "value": ["mean", "median", "max"],
    "id": "count",
})
```

Полезно, когда одному группированию нужно несколько разных агрегатов.

## 11. Строковые методы

```python
df["marital-status"].str.startswith("Married")
df["name"].str.lower()
df["text"].str.contains("python", case=False)
```

Операция применяется ко всему Series без ручного цикла.

## 12. Сортировка

```python
df.sort_values("age")
df.sort_values("age", ascending=False)
df.sort_values(["salary", "age"], ascending=[True, False])
```

Удобна для экстремумов и читабельного представления результата.

## 13. Пропуски

```python
df.isna().sum()
```

Базовые операции:

```python
df.dropna()
df.fillna(value)
```

Но механически удалять или заполнять пропуски нельзя. Нужно понять их происхождение и смысл.

Простой учебный вариант для возраста:

```python
median_age = df["age"].median()
df["age_filled"] = df["age"].fillna(median_age)
```

В ML-проекте статистику заполнения вычисляют только на train-части, иначе возможна утечка данных.

## 14. Новые признаки

Если одно условие используется много раз, его полезно оформить как признак:

```python
df["is_child"] = df["age_filled"] < 16
```

После этого анализ становится читаемее:

```python
df.groupby("is_child")["survived"].agg(["count", "mean"])
```

## 15. `copy()` и безопасные изменения

```python
men = df[df["sex"] == "Male"].copy()
men["married"] = men["marital-status"].str.startswith("Married")
```

Явная копия показывает, что рабочая таблица должна быть независимой от исходной.

## 16. `unstack()`

После группировки по нескольким признакам:

```python
df.groupby(["sex", "pclass"])["survived"].mean().unstack()
```

Один уровень индекса переносится в столбцы, и результат превращается в компактную сравнительную таблицу.

## 17. Что показал UCI Adult

В основной практике:

- мужчин: **21 790**, женщин: **10 771**;
- средний возраст женщин — около **36.86 года**;
- доля Германии — около **0.42%**;
- средний возраст группы `>50K` — около **44.25**, группы `<=50K` — около **36.78**;
- высокий доход встречается и без перечисленного высшего образования;
- максимальный возраст мужчины `Amer-Indian-Eskimo` — **82 года**;
- доля `>50K` среди женатых мужчин выше, чем среди неженатых;
- максимум рабочего времени — **99 часов/неделю**;
- 99 часов работают **85 человек**, около **29.4%** из них имеют доход `>50K`.

Это описательная статистика, а не доказательство причинности.

## 18. Что дала практика Titanic

Titanic хорошо связывает отдельные Pandas-приёмы в единый процесс:

1. осмотреть структуру;
2. проверить пропуски;
3. сформировать точную подвыборку;
4. сравнить группы;
5. создать производный признак;
6. представить многоуровневое сравнение через `unstack()`;
7. сформулировать вывод без переинтерпретации.

Если `survived` закодирован `0/1`, то:

```python
df.groupby("sex")["survived"].mean()
```

сразу даёт долю выживших внутри каждой группы.

Но вместе с долей важно смотреть размер группы:

```python
df.groupby("pclass")["survived"].agg(["count", "mean"])
```

Маленькие группы могут давать очень нестабильные проценты.

## 19. Типичные ошибки

### Лишние Python-циклы

Плохо:

```python
result = []
for value in df["age"]:
    if value > 30:
        result.append(value)
```

Лучше:

```python
df.loc[df["age"] > 30, "age"]
```

### Количество вместо доли

Если группы разного размера, абсолютное число событий почти всегда хуже доли для сравнения.

### Причинный вывод из групповых различий

Разница средних или долей сама по себе не доказывает причину.

### Игнорирование типов

`"42"` и `42` — разные значения с точки зрения типов. Ошибочный dtype ломает сортировку, арифметику и агрегирование.

### Chained indexing

Вместо:

```python
df[df["sex"] == "Female"]["age"]
```

яснее:

```python
df.loc[df["sex"] == "Female", "age"]
```

## 20. Как мыслить при решении задачи

Вопрос: «Каков средний возраст женщин?»

Разложение:

1. наблюдения — женщины;
2. условие — `sex == "Female"`;
3. признак — `age`;
4. агрегат — среднее.

Отсюда:

```python
df.loc[df["sex"] == "Female", "age"].mean()
```

Важно учиться строить выражение из смысла вопроса, а не вспоминать готовую строку кода.

## 21. Минимум, который должен остаться в памяти

```python
# NumPy
x.shape
x.dtype
x[mask]
x.mean(axis=0)
x.reshape(...)

# осмотр DataFrame
df.head()
df.info()
df.describe()
df.isna().sum()

# выбор
df["col"]
df[["a", "b"]]
df.loc[condition, "col"]
df.iloc[rows, cols]

# фильтрация
df[(cond1) & (cond2)]

# категории
df["category"].value_counts()

# сортировка
df.sort_values("col")

# группы
df.groupby("group")["value"].mean()
df.groupby("group").agg(...)

# пропуски
df["col"].fillna(...)

# переформатирование
df.groupby(["a", "b"])["value"].mean().unstack()
```

## 22. Итоговая ментальная модель

NumPy учит мыслить массивами и формами. Pandas добавляет имена столбцов, индексы и удобную табличную семантику. EDA объединяет эти инструменты в процесс принятия аналитических решений.

> **Не начинай с метода. Начинай с вопроса.**

Сначала сформулируй, какие строки, признаки и метрика нужны. После этого код становится следствием логики анализа.

## Практика

- [UCI Adult — полный Pandas-анализ](https://github.com/JSwhiz/mlcourse/blob/topic01-pandas-data-analysis/topic01_pandas_data_analysis/notebooks/01_adult_pandas_analysis.ipynb)
- [NumPy Foundations](https://github.com/JSwhiz/mlcourse/blob/topic01-pandas-data-analysis/topic01_pandas_data_analysis/notebooks/02_numpy_foundations.ipynb)
- [Titanic mini-EDA](https://github.com/JSwhiz/mlcourse/blob/topic01-pandas-data-analysis/topic01_pandas_data_analysis/notebooks/03_titanic_mini_eda.ipynb)
