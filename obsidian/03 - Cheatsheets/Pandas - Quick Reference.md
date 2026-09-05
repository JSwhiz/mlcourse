---
type: cheatsheet
topic: topic01
course: mlcourse.ai
status: learning
tags:
  - pandas
  - cheatsheet
---

# Pandas — Quick Reference

## Inspect

```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

## Select

```python
df["column"]
df[["a", "b"]]
df.loc[rows, columns]
df.iloc[row_positions, column_positions]
```

## Filter

```python
df[df["value"] > 10]
df[(df["a"] > 10) & (df["b"] == "x")]
df[df["name"].isin(["A", "B"])]
```

## Sort

```python
df.sort_values("value")
df.sort_values("value", ascending=False)
```

## Aggregate

```python
df["value"].mean()
df["value"].median()
df["category"].value_counts()
df.groupby("category")["value"].mean()
df.groupby("category").agg({"value": ["mean", "median", "max"]})
```

## Missing values

```python
df.isna().sum()
df.dropna()
df.fillna(...)
```

## Related notes

- [[Pandas - Series and DataFrame]]
- [[Pandas - Indexing and Filtering]]
- [[Pandas - GroupBy and Aggregations]]
- [[Topic 01 - Overview]]
