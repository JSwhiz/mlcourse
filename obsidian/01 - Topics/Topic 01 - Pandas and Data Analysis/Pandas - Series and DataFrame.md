---
type: concept
topic: topic01
course: mlcourse.ai
status: learning
tags:
  - pandas
  - dataframe
  - series
---

# Pandas — Series and DataFrame

## Idea

`Series` is a one-dimensional labeled structure. `DataFrame` is a two-dimensional labeled table composed of columns that can have different data types.

## Mental model

Think of a `DataFrame` as a table with:

- an index identifying rows;
- named columns;
- values stored by row/column intersection;
- column-specific data types.

## Useful inspection

```python
df.head()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

## What to notice first

- number of rows and columns;
- missing values;
- unexpected data types;
- categorical vs numerical columns;
- whether the index has meaning;
- suspicious ranges or impossible values.

## Connections

- [[Pandas - Indexing and Filtering]]
- [[Pandas - GroupBy and Aggregations]]
- [[Topic 01 - Overview]]

## Questions

- When should an index carry domain meaning?
- What problems appear when numeric values are stored as strings?

## Takeaways

> Add your own examples after the first notebook.
