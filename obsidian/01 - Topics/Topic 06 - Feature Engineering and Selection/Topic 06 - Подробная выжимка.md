---
type: topic-summary
topic: 06
status: solid
tags: [feature-engineering, feature-selection, leakage, pipelines, конспект]
---
# Topic 06 — Feature Engineering и Selection: подробная выжимка

[[ML Course]] · [[Topic 05 - Подробная выжимка]]

## 1. Главная идея

Алгоритм видит не реальный мир, а **представление данных**, которое я ему дал.

Один и тот же объект можно описать плохо или хорошо. Поэтому feature engineering иногда даёт больший прирост, чем замена одного алгоритма на другой.

```text
сырой объект → признаки → модель
```

Если полезный сигнал трудно выразить через исходные колонки, задача feature engineering — сделать его доступнее модели.

Но есть главное правило:

> Признак полезен только если его можно честно построить в момент реального prediction.

## 2. Пример: дата

Сырая дата:

```text
2026-09-05 18:37:00
```

Для модели могут быть полезнее:

```python
df["hour"] = df["timestamp"].dt.hour
df["weekday"] = df["timestamp"].dt.dayofweek
df["is_weekend"] = df["weekday"].isin([5, 6])
df["month"] = df["timestamp"].dt.month
```

Модель теперь явно видит календарную структуру.

## 3. Числовые преобразования

### Логарифм

Для признака с длинным правым хвостом:

```python
df["log_income"] = np.log1p(df["income"])
```

Это может уменьшить влияние огромных значений и сделать связь ближе к линейной.

### Отношения

```python
df["price_per_m2"] = df["price"] / df["area"]
```

Иногда отношение двух сырых колонок намного ближе к смыслу процесса.

### Разности

```python
df["days_since_last_order"] = prediction_date - last_order_date
```

Но здесь сразу возникает вопрос: **известна ли `last_order_date` на момент прогноза?**

## 4. Interaction features

Линейная модель сама не понимает произведение признаков, если его явно не добавить.

```python
df["age_income"] = df["age"] * df["income"]
```

PolynomialFeatures может строить такие комбинации автоматически:

```python
from sklearn.preprocessing import PolynomialFeatures
```

Но количество признаков быстро растёт, поэтому complexity нужно контролировать.

## 5. Категориальные признаки

Модель обычно не понимает строки напрямую.

### One-hot encoding

```text
city = Moscow / Kaluga / Tallinn
```

превращается примерно в:

```text
city_Moscow city_Kaluga city_Tallinn
1           0           0
```

В sklearn:

```python
OneHotEncoder(handle_unknown="ignore")
```

`handle_unknown="ignore"` важен: в production может появиться категория, которой не было на train.

## 6. High cardinality

Если категория имеет десятки тысяч значений, one-hot создаст огромное sparse пространство.

Возможные варианты:

- hashing;
- frequency encoding;
- target encoding;
- объединение редких категорий;
- доменное преобразование.

Но target encoding особенно опасен leakage.

## 7. Target encoding и leakage

Наивно:

```text
category → средний target этой category по всему dataset
```

Если объект участвует в вычислении собственного encoded value, target частично попадает в признаки.

Поэтому target encoding для train должен строиться out-of-fold.

Идея:

```text
fold 1 кодируется статистиками folds 2–5
fold 2 кодируется статистиками folds 1,3,4,5
...
```

Для test/production статистики уже считаются по всему train.

## 8. Missing values — это тоже часть модели

Нельзя просто сказать «заполню медианой» и забыть.

Вопросы:

- почему значение отсутствует;
- несёт ли сам факт пропуска информацию;
- одинаков ли механизм пропусков на train и production;
- подходит ли одна медиана всем группам.

Простой pipeline:

```python
from sklearn.impute import SimpleImputer

SimpleImputer(strategy="median")
```

Иногда полезен отдельный indicator отсутствия.

## 9. Pipeline — защита от утечки

Плохо:

```python
X = imputer.fit_transform(X)
X = scaler.fit_transform(X)
cross_val_score(model, X, y, cv=5)
```

Почему плохо? `imputer` и `scaler` уже увидели validation folds.

Правильно:

```python
Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("model", LogisticRegression()),
])
```

Тогда внутри каждого CV fold preprocessing обучается только на training части.

## 10. ColumnTransformer

Числа и категории требуют разных преобразований.

```python
from sklearn.compose import ColumnTransformer

preprocess = ColumnTransformer([
    ("num", numeric_pipeline, numeric_cols),
    ("cat", categorical_pipeline, categorical_cols),
])
```

Затем:

```python
Pipeline([
    ("preprocess", preprocess),
    ("model", model),
])
```

Это уже очень близко к нормальной production-архитектуре tabular ML.

## 11. Feature selection — зачем вообще удалять признаки

Больше признаков не всегда лучше.

Удаление может:

- снизить variance;
- уменьшить шум;
- ускорить обучение/inference;
- уменьшить память;
- повысить интерпретируемость;
- снизить стоимость сбора данных.

Но удалять признаки только ради красивого маленького списка не нужно.

## 12. Filter methods

Оценивают признаки без многократного обучения итоговой модели.

Примеры:

- variance threshold;
- correlation;
- mutual information;
- statistical tests.

Плюсы — быстро. Минус — взаимодействия признаков могут потеряться.

Признак может быть слаб сам по себе, но полезен вместе с другим.

## 13. Embedded methods

Selection происходит во время обучения модели.

Примеры:

- L1 regularization;
- tree-based importance.

```python
LogisticRegression(penalty="l1", solver="liblinear")
```

L1 может занулять коэффициенты, но при коррелированных признаках выбор конкретного признака может быть нестабильным.

## 14. Wrapper methods

Многократно обучают модель с разными наборами признаков.

Например RFE.

Плюс — selection связан с конкретной моделью. Минус — дорого вычислительно и легко переоптимизировать маленький dataset.

## 15. Leakage — центральная опасность темы

Leakage — когда при обучении доступна информация, которой не будет в реальном prediction.

Примеры:

### Будущее

Предсказываю дефолт на момент выдачи кредита, но использую `days_overdue_after_30_days`.

Это почти прямой ответ из будущего.

### Target proxy

Предсказываю churn, а в данных есть `account_closed_reason`.

### Preprocessing leakage

Scaler/imputer/selector обучен по всему dataset до CV.

### Aggregation leakage

Для объекта считаю среднее target его группы, используя его собственный target или будущие объекты.

## 16. Главное правило доступности признака

Для каждой колонки я должен уметь ответить:

```text
В какой момент она появляется?
Будет ли она известна в production именно тогда, когда модель должна дать прогноз?
```

Это часто важнее любой feature importance.

## 17. Как проверять новый признак

Не так:

```text
добавил feature → train score вырос → отлично
```

А так:

```text
baseline CV
↓
добавил feature внутри корректного pipeline
↓
тот же CV split
↓
сравнил mean + std
↓
проверил устойчивость
↓
оценил стоимость получения feature
```

## 18. Feature selection тоже должен быть внутри CV

Если сначала выбрать лучшие признаки по всему dataset, а потом сделать CV, validation уже повлиял на выбор признаков.

Правильно:

```python
Pipeline([
    ("preprocess", preprocess),
    ("select", SelectKBest(k=20)),
    ("model", LogisticRegression()),
])
```

## 19. Когда feature engineering особенно важно

- линейные модели;
- временные данные;
- бизнес-агрегаты;
- сырые даты;
- high-cardinality категории;
- текстовые признаки;
- когда доменная логика известна лучше, чем модели.

Tree ensembles умеют сами находить многие нелинейные splits, но даже им плохой representation может сильно мешать.

## 20. Типичные ошибки

- строить feature из будущего;
- fit preprocessing до CV;
- target encode без OOF;
- создавать сотни признаков без проверки;
- выбирать features по test;
- считать missing values просто технической грязью;
- игнорировать unseen categories;
- забывать стоимость feature в production;
- удалять коррелированный признак только потому, что correlation высокая, не проверив модель.

## 21. Как я думаю о признаке

Перед добавлением нового feature:

1. Какой физический/бизнес-смысл он выражает?
2. Из каких сырых данных строится?
3. Когда эти данные доступны?
4. Нет ли target/future leakage?
5. Как обработать missing/unseen values?
6. Нужно ли scaling/encoding?
7. Где должен происходить `fit` преобразования?
8. Улучшает ли feature CV?
9. Стабильно ли улучшение?
10. Оправдана ли стоимость в production?

## 22. Минимальный production-like шаблон

```python
preprocess = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]), numeric_cols),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]), categorical_cols),
])

model = Pipeline([
    ("preprocess", preprocess),
    ("model", LogisticRegression(max_iter=2000)),
])
```

## 23. Самопроверка

1. Почему медиана, рассчитанная по всему dataset до CV, является leakage?
2. Почему target encoding требует OOF?
3. Чем filter, embedded и wrapper selection отличаются?
4. Зачем `handle_unknown="ignore"`?
5. Почему feature importance недостаточно для решения удалить признак?
6. Что значит «признак доступен в момент prediction»?
7. Почему selection должен быть частью Pipeline?
8. Когда feature engineering может дать больше, чем смена модели?

## 24. Связи

Назад → [[Topic 05 - Подробная выжимка]].

Дальше → [[Topic 07 - Подробная выжимка]]: когда я меняю representation признаков, я меняю и геометрию данных, на которой работают PCA и clustering.
