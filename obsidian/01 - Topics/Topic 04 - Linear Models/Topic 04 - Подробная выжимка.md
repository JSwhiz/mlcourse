---
type: topic-summary
topic: 04
status: solid
tags: [linear-models, regression, logistic-regression, regularization, конспект]
---
# Topic 04 — Linear Models: подробная выжимка

[[ML Course]] · [[Topic 03 - Подробная выжимка]]

## 1. Главная идея

Линейная модель пытается объяснить target **взвешенной суммой признаков**.

```text
prediction = w0 + w1*x1 + w2*x2 + ... + wp*xp
```

Это простая форма, и именно поэтому она полезна: быстро обучается, даёт сильный baseline и заставляет явно думать о признаках, масштабе, loss и regularization.

Главный вопрос темы:

> Как получить модель достаточно гибкую для сигнала, но достаточно ограниченную, чтобы она не подгоняла шум?

## 2. Linear Regression

Для одного признака:

```text
y_hat = w0 + w1*x
```

`w0` — intercept. `w1` — насколько изменяется prediction при увеличении `x` на единицу, если остальные признаки фиксированы.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

Важно: коэффициент описывает связь внутри модели. Это **не автоматическое доказательство причинности**.

## 3. Ошибка и MSE

Residual:

```text
residual = actual - prediction
```

MSE:

```text
MSE = mean((y - y_hat)^2)
```

Квадрат сильно штрафует большие ошибки.

OLS выбирает коэффициенты, минимизирующие сумму квадратов residuals.

## 4. Зачем смотреть residuals

Одна итоговая метрика может скрывать структуру ошибки.

Хороший residual plot должен выглядеть примерно как случайное облако вокруг нуля.

Если вижу:

```text
дугу → возможно, не хватает нелинейности
воронку → variance ошибки зависит от уровня prediction
временной рисунок → не учтена временная структура
```

то проблема может быть в specification, а не просто в «плохом score».

## 5. Logistic Regression

Несмотря на название, это классификатор.

Сначала строится линейный score:

```text
z = w0 + w1*x1 + ... + wp*xp
```

Затем sigmoid:

```text
p = 1 / (1 + exp(-z))
```

получает число от 0 до 1, которое интерпретируется как вероятность класса 1 при выполнении модельных предпосылок.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)
proba = model.predict_proba(X_test)[:, 1]
```

## 6. Log-odds

Logistic regression линейна не в probability, а в log-odds:

```text
log(p / (1-p)) = w0 + w1*x1 + ...
```

Поэтому `exp(w_i)` можно интерпретировать как multiplicative change в odds при увеличении признака на единицу при фиксированных остальных признаках.

Но опять: это модельная ассоциация, не причинный эффект.

## 7. Threshold 0.5 — просто default

`predict()` обычно использует порог около 0.5.

Но бизнес может требовать другой компромисс.

Если пропустить fraud очень дорого:

```text
важен recall → threshold можно снизить
```

Если ложное обвинение дорого:

```text
важен precision → threshold может быть выше
```

Поэтому правильная последовательность:

```text
цена FP/FN → метрика → модель → threshold
```

а не наоборот.

## 8. Почему scaling важен

Допустим:

```text
age: 20–80
income: 20 000–500 000
```

Для обычной unregularized linear regression изменение единиц само по себе не должно разрушать predictive capability, но для regularization и numerical optimization масштаб очень важен.

Поэтому обычно:

```python
Pipeline([
    ("scale", StandardScaler()),
    ("model", LogisticRegression()),
])
```

## 9. Проблема больших коэффициентов

Если признаков много, они коррелируют или данных мало, модель может подобрать большие нестабильные коэффициенты.

На train всё выглядит хорошо, но небольшое изменение данных сильно меняет параметры.

Regularization штрафует слишком сложное решение.

## 10. Ridge / L2

Оптимизируем примерно:

```text
loss + λ * Σ w_i²
```

Большие коэффициенты становятся дорогими.

Эффект:

- коэффициенты плавно сжимаются;
- модель становится стабильнее;
- особенно полезно при коррелированных признаках;
- обычно коэффициенты не становятся ровно нулевыми.

Для regression:

```python
from sklearn.linear_model import Ridge
Ridge(alpha=1.0)
```

## 11. Lasso / L1

```text
loss + λ * Σ |w_i|
```

L1 может занулять часть коэффициентов.

```python
from sklearn.linear_model import Lasso
Lasso(alpha=...)
```

Это даёт sparse решение и одновременно грубый feature selection.

Но если признаки сильно коррелируют, Lasso может нестабильно выбирать один из них.

## 12. `alpha`, `lambda` и `C`

У разных sklearn моделей параметр называется по-разному.

Для Ridge/Lasso:

```text
alpha больше → regularization сильнее
```

Для LogisticRegression используется `C`, обратная сила regularization:

```text
C меньше → regularization сильнее
C больше → regularization слабее
```

Это легко перепутать.

## 13. Bias–Variance

Очень сильная regularization:

```text
коэффициенты маленькие
модель слишком простая
→ high bias / underfit
```

Очень слабая:

```text
модель свободнее подгоняет train
→ выше variance / overfit
```

Подбираю силу regularization по CV.

## 14. Почему preprocessing должен быть внутри Pipeline

Плохо:

```python
X_scaled = StandardScaler().fit_transform(X)
cross_val_score(model, X_scaled, y, cv=5)
```

Scaler увидел статистики всех folds, включая validation.

Правильно:

```python
pipe = Pipeline([
    ("scale", StandardScaler()),
    ("model", LogisticRegression(max_iter=2000)),
])

cross_val_score(pipe, X, y, cv=5)
```

Каждый fold получает scaler, обученный только на своей train части.

## 15. Multicollinearity

Если два признака почти дублируют друг друга, например:

```text
distance_km
 distance_meters
```

модель может распределять вес между ними нестабильно.

Prediction при этом может быть нормальным, но интерпретация отдельных коэффициентов становится ненадёжной.

Ridge часто помогает стабилизировать коэффициенты.

## 16. Метрики regression

### MAE

Средняя абсолютная ошибка. Интерпретируется в единицах target.

### MSE / RMSE

Сильнее штрафуют крупные ошибки. RMSE снова имеет единицы target.

### R²

Показывает, какую долю вариации относительно простого среднего объясняет модель в данном dataset.

`R²=0` примерно соответствует baseline среднего; отрицательный R² возможен — модель хуже такого baseline.

## 17. Метрики classification

Как и в Topic 03:

- accuracy;
- precision;
- recall;
- F1;
- ROC-AUC;
- PR-AUC;
- log-loss;
- calibration.

Для probabilistic model важно не только ранжирование, но иногда и качество самих вероятностей.

## 18. Calibration

Если модель говорит `0.8` для ста похожих объектов, хорошо откалиброванная вероятность означает, что примерно 80 из них действительно positive.

Высокий ROC-AUC не гарантирует хорошую calibration.

Это важно, если probability используется для риска, цены, ожидаемой прибыли или threshold decisions.

## 19. Learning curves

Смотрим train и validation score при росте размера train.

### Оба плохие и близкие

Вероятен high bias. Больше тех же данных может почти не помочь — нужны признаки или более выразительная модель.

### Train хороший, validation хуже

High variance. Могут помочь:

- больше данных;
- regularization;
- упрощение модели;
- удаление шума.

## 20. Интерпретация коэффициентов

После StandardScaler коэффициенты разных числовых признаков становятся чуть удобнее сравнивать по масштабу, но осторожность всё равно нужна.

На коэффициенты влияют:

- корреляции признаков;
- encoding категорий;
- regularization;
- interactions, которых нет в модели;
- распределение данных.

Поэтому «самый большой коэффициент = самый важный реальный фактор» — слишком сильный вывод.

## 21. Нелинейность и feature engineering

Линейная модель линейна по переданным features, но сами features могут быть нелинейными:

```python
X["age_squared"] = X["age"] ** 2
X["income_log"] = np.log1p(X["income"])
```

Тогда модель остаётся линейной по коэффициентам, но может описывать более сложную зависимость.

Это мост к Topic 06.

## 22. Типичные ошибки

- scaling до CV;
- подбор `alpha`/`C` по test;
- путать направление `C` и `alpha`;
- считать threshold 0.5 законом;
- использовать accuracy при сильном дисбалансе;
- сравнивать сырые коэффициенты признаков разных масштабов;
- считать коэффициент причинным эффектом;
- игнорировать residuals;
- делать вывод только по train score.

## 23. Как я решаю задачу линейной моделью

1. Определяю target и метрику.
2. Строю Dummy/simple baseline.
3. Определяю preprocessing.
4. Собираю всё stateful в Pipeline.
5. Обучаю простую linear/logistic model.
6. Проверяю CV.
7. Подбираю regularization.
8. Для regression анализирую residuals.
9. Для classification анализирую confusion matrix, ROC/PR и threshold.
10. Проверяю calibration, если важны вероятности.
11. Интерпретирую коэффициенты только с учётом масштаба и корреляций.
12. Финально проверяю на untouched test.

## 24. Минимум в памяти

```python
Pipeline([
    ("scale", StandardScaler()),
    ("model", LogisticRegression(C=1.0, max_iter=2000)),
])

Ridge(alpha=1.0)
Lasso(alpha=0.01)
```

И концептуально:

```text
linear model = weighted sum
regularization = цена за сложность коэффициентов
CV выбирает силу regularization
test остаётся закрытым
```

## 25. Самопроверка

1. Почему logistic regression называется regression, хотя решает classification?
2. Что делает sigmoid?
3. Почему threshold 0.5 можно менять?
4. Чем L1 отличается от L2?
5. Почему `C` меньше означает более сильную regularization?
6. Почему scaler должен быть внутри CV Pipeline?
7. Что показывает residual plot?
8. Почему коррелированные признаки мешают интерпретации коэффициентов?
9. Чем хороший ROC-AUC отличается от хорошей calibration?

## 26. Связи

Назад → [[Topic 03 - Подробная выжимка]].

Дальше → [[Topic 05 - Подробная выжимка]]: вместо стабилизации одной модели regularization мы будем стабилизировать множество деревьев усреднением.
