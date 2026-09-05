---
type: concept
topic: topic01
course: mlcourse.ai
status: learning
tags:
  - pandas
  - groupby
  - aggregation
---

# Pandas — GroupBy and Aggregations

## Idea

`groupby()` implements the split → apply → combine pattern: split data into groups, calculate something for each group, then combine the results.

## Core patterns

```python
df.groupby("category")["value"].mean()

df.groupby("category").agg({
    "value": ["mean", "median", "min", "max"],
    "id": "count",
})

df.groupby(["country", "segment"])["revenue"].sum()
```

## Questions aggregations can answer

- Which group has the highest average value?
- How many observations belong to each category?
- How different are median and mean inside a group?
- Which segment contributes the most to the total?
- Are differences stable across another grouping variable?

## Common traps

- averaging an identifier or another meaningless numeric column;
- ignoring missing values;
- grouping by a column with inconsistent labels;
- reporting a group statistic without checking group size;
- confusing association with causation.

## Connections

- [[Pandas - Series and DataFrame]]
- [[Pandas - Indexing and Filtering]]
- [[Topic 01 - Overview]]

## Questions

- When is `transform()` more appropriate than `agg()`?
- How should very small groups affect interpretation?

## Takeaways

> Add one real conclusion from your dataset after completing the aggregation exercises.
