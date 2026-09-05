---
type: concept
topic: topic01
course: mlcourse.ai
status: learning
tags:
  - pandas
  - indexing
  - filtering
---

# Pandas — Indexing and Filtering

## Idea

Selecting data is about expressing exactly which rows and columns are relevant to a question.

## Core tools

```python
df["column"]
df[["column_a", "column_b"]]
df.loc[row_condition, ["column_a", "column_b"]]
df.iloc[row_positions, column_positions]
```

## Boolean filtering

```python
df[df["age"] >= 30]
df[(df["age"] >= 30) & (df["city"] == "London")]
df[(df["status"] == "active") | (df["score"] > 90)]
```

Use parentheses around each condition when combining them with `&`, `|`, and `~`.

## Mental checklist

Before filtering, ask:

1. Which observations do I need?
2. Which columns are actually required?
3. Is the condition inclusive or exclusive?
4. Could missing values affect the result?
5. Can the expression be written clearly without a Python loop?

## Connections

- [[Pandas - Series and DataFrame]]
- [[Pandas - GroupBy and Aggregations]]
- [[Topic 01 - Overview]]

## Questions

- When is `query()` clearer than boolean indexing?
- When should I prefer `.loc` over chained selection?

## Takeaways

> Add examples that you personally found non-obvious.
