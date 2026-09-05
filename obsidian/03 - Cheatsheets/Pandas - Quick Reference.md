---
type: cheatsheet
topic: topic01
course: mlcourse.ai
status: learning
tags:
  - pandas
  - cheatsheet
---

# Pandas — Быстрая шпаргалка

## Первичный просмотр

```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

## Выбор данных

```python
df["column"]
df[["a", "b"]]
df.loc[rows, columns]
df.iloc[row_positions, column_positions]
```

## Фильтрация

```python
df[df["value"] > 10]
df[(df["a"] > 10) & (df["b"] == "x")]
df[df["name"].isin(["A", "B"])]
```

## Сортировка

```python
df.sort_values("value")
df.sort_values("value", ascending=False)
```

## Агрегации

```python
df["value"].mean()
df["value"].median()
df["category"].value_counts()
df.groupby("category")["value"].mean()
df.groupby("category").agg({"value": ["mean", "median", "max"]})
```

## Пропущенные значения

```python
df.isna().sum()
df.dropna()
df.fillna(...)
```

## Связанные заметки

- [[Pandas - Series and DataFrame]]
- [[Pandas - Indexing and Filtering]]
- [[Pandas - GroupBy and Aggregations]]
- [[Topic 01 - Overview]]
