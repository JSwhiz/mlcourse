---
type: topic-summary
topic: 10
status: solid
tags: [gradient-boosting, ensembles, early-stopping, xgboost, lightgbm, catboost, конспект]
---
# Topic 10 — Gradient Boosting: подробная выжимка

[[ML Course]] · [[Topic 09 - Подробная выжимка]]

## 1. Главная идея

Random Forest строил много независимых деревьев и усреднял их.

Boosting делает почти противоположное: строит модели **последовательно**.

```text
model 1
  ↓ исправляем его ошибки
model 2
  ↓ исправляем оставшиеся ошибки
model 3
  ↓
...
```

Итоговый прогноз — сумма вкладов слабых моделей.

Главная мысль:

> Каждое следующее дерево должно улучшить то, что ансамбль пока предсказывает плохо.

## 2. Additive model

Общий вид:

```text
F_M(x) = F_0(x) + η h_1(x) + η h_2(x) + ... + η h_M(x)
```

- `F_0` — начальный прогноз;
- `h_m` — новое слабое дерево;
- `η` — learning rate;
- `M` — число деревьев.

Модель постепенно наращивает сложность.

## 3. Самая простая интуиция: регрессия и residuals

Пусть сначала прогнозируем средним:

```text
actual:     10  20  30
prediction: 20  20  20
residual:  -10   0  10
```

Следующее дерево пытается предсказать residuals.

После добавления его прогноза ансамбль становится ближе к настоящему `y`.

Затем считаются новые residuals, строится следующее дерево и так далее.

Это хорошая интуиция для squared error.

## 4. Почему говорят «gradient» boosting

Для произвольной differentiable loss понятие residual обобщается до **отрицательного градиента функции потерь**.

```text
на текущих predictions
↓
считаем направление, которое сильнее уменьшит loss
↓
новое дерево приближает это направление
↓
добавляем дерево к ансамблю
```

То есть boosting делает функциональный gradient descent, где шагом является новое дерево.

## 5. Weak learner

Обычно используются неглубокие деревья.

Почему не одно огромное дерево?

Boosting хочет постепенно добавлять небольшие corrections. Если каждое дерево слишком мощное, ансамбль может быстро начать подгонять шум.

Типичные глубины могут быть 2–8, но оптимальное значение зависит от задачи и реализации.

## 6. Learning rate

```text
new_prediction = old_prediction + learning_rate * tree_prediction
```

Маленький `learning_rate`:

- осторожные шаги;
- нужно больше деревьев;
- часто лучше generalization;
- обучение дольше.

Большой:

- быстрее;
- меньше деревьев;
- выше риск переобучения/нестабильности.

Поэтому `learning_rate` и `n_estimators` нельзя настраивать независимо.

## 7. `n_estimators`

Число boosting stages.

При фиксированном learning rate:

```text
слишком мало → underfit
достаточно → validation optimum
слишком много → возможен overfit
```

Отсюда важность early stopping.

## 8. Early stopping

Следим за validation loss:

```text
iteration 100 → 0.42
iteration 200 → 0.38
iteration 300 → 0.36
iteration 400 → 0.361
iteration 500 → 0.365
```

Лучшее состояние было около 300.

Early stopping прекращает обучение, если validation metric долго не улучшается.

Это:

- экономит compute;
- помогает regularization;
- автоматически подбирает эффективное число итераций.

Но validation data для early stopping должна быть отделена честно.

## 9. Depth и interactions

Глубина дерева определяет сложность взаимодействий, которые одно дерево может моделировать.

Stump (`depth=1`) умеет только очень простые corrections.

Более глубокое дерево умеет interactions между признаками.

Но глубже → больше capacity → выше риск fit noise.

## 10. Gradient Boosting vs Random Forest

| | Random Forest | Gradient Boosting |
|---|---|---|
| деревья | независимые | последовательные |
| основная идея | averaging | исправление текущей ошибки |
| parallelization | естественная | сложнее |
| sensitivity к params | умеренная | выше |
| типичная сила на tabular | высокая | очень высокая |
| overfit | averaging помогает | нужно внимательно regularize |

Random Forest часто отличный baseline. Boosting часто выигрывает по quality, но требует аккуратнее validation/tuning.

## 11. Классический sklearn GradientBoosting

```python
from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    random_state=42,
)
```

Для больших datasets современные histogram-based реализации обычно эффективнее.

## 12. Histogram-based boosting

Вместо перебора всех уникальных значений непрерывные признаки разбиваются на bins.

Это ускоряет поиск splits и уменьшает память.

Идея используется современными библиотеками и `HistGradientBoosting` в sklearn.

## 13. XGBoost

XGBoost сделал boosting очень популярным благодаря сочетанию:

- регуляризации;
- эффективной реализации;
- обработки sparse data;
- параллелизации частей вычислений;
- контроля дерева;
- early stopping.

Важно понимать не список параметров XGBoost, а базовую boosting-механику. Тогда параметры перестают выглядеть магией.

## 14. LightGBM

Сильная сторона — скорость и эффективность на больших tabular datasets.

Использует histogram approach и leaf-wise growth.

Leaf-wise рост может быстрее уменьшать loss, но на небольших данных требует контроля complexity (`num_leaves`, `min_data_in_leaf`, depth и т.д.).

## 15. CatBoost

Особенно удобен для категориальных признаков.

Главная ценность — алгоритмическая работа с категориями и ordered statistics, уменьшающая target leakage относительно наивного target encoding.

Это не означает, что можно перестать думать о leakage вообще. Временная/бизнес-доступность признаков всё равно остаётся моей ответственностью.

## 16. Почему boosting силён на tabular data

Деревья естественно умеют:

- нелинейности;
- thresholds;
- interactions;
- разные масштабы числовых признаков;
- сложную кусочную структуру.

Последовательное исправление ошибок позволяет постепенно строить очень сильную функцию.

Поэтому boosting — один из первых серьёзных кандидатов для структурированных табличных данных.

## 17. Нужен ли scaling

Для tree boosting обычный scaling числовых признаков обычно не нужен.

Split зависит от порядка значений, а не от евклидового расстояния или размера коэффициента.

Но preprocessing категорий/missing values зависит от конкретной реализации.

## 18. Regularization

Boosting регулируется не одним параметром.

Основные рычаги:

- learning rate;
- число деревьев;
- depth / leaves;
- min samples in leaf;
- row subsampling;
- column subsampling;
- L1/L2 в современных реализациях;
- early stopping.

То есть regularization — это управление скоростью и сложностью роста ансамбля.

## 19. Subsampling

Если каждое дерево обучается не на всех строках, появляется stochastic gradient boosting.

Это может:

- уменьшить корреляцию corrections;
- снизить overfit;
- ускорить обучение.

Аналогично можно выбирать подмножество признаков.

## 20. Метрика и loss — не всегда одно и то же

Модель оптимизирует training objective, например log-loss.

Но бизнес может оценивать:

- ROC-AUC;
- PR-AUC;
- recall;
- custom profit;
- MAE.

Нужно различать:

```text
что оптимизирует алгоритм
vs
по чему я выбираю модель для задачи
```

## 21. Feature importance

Как и у Random Forest, importance нельзя считать причинным эффектом.

У boosting доступны:

- split/gain importance;
- permutation importance;
- SHAP.

SHAP помогает объяснять отдельные predictions и глобальные patterns, но объясняет **модель**, а не автоматически реальный причинный процесс.

## 22. Overfitting в boosting

Симптом:

```text
train loss продолжает падать
validation loss перестал улучшаться или растёт
```

Что можно попробовать:

- уменьшить depth/leaves;
- уменьшить learning rate;
- использовать early stopping;
- увеличить min leaf;
- добавить subsampling;
- проверить leakage;
- получить больше данных.

Первым делом всё равно проверяю leakage: иногда «фантастическое качество» — не успех модели, а ошибка pipeline.

## 23. Tuning без хаоса

Не стоит одновременно перебирать 15 параметров без понимания.

Практический порядок:

1. зафиксировать validation;
2. построить простой baseline;
3. выбрать разумную complexity дерева;
4. подобрать learning rate + iterations с early stopping;
5. проверить row/column subsampling;
6. при необходимости regularization;
7. оценить стабильность по folds/seeds;
8. финальный test один раз.

## 24. Почему Kaggle любит boosting

На tabular соревнованиях:

- данные относительно небольшие/средние;
- много nonlinear interactions;
- важна каждая доля score;
- feature engineering + boosting дают сильный результат;
- inference часто приемлем.

Но production-задача может предпочесть более простую модель из-за latency, explainability или стоимости поддержки.

## 25. Boosting во временных рядах

Boosting можно применять к time series после превращения ряда в tabular features:

```text
lags
rolling stats
calendar features
external regressors
→ boosting
```

Но boosting **не исправляет неправильный random split**.

Validation всё равно должна идти по времени, как в Topic 09.

## 26. Типичные ошибки

- tuning по test;
- слишком большой learning rate;
- глубокие деревья без необходимости;
- отсутствие early stopping;
- считать XGBoost/LightGBM/CatBoost тремя совершенно несвязанными идеями;
- считать feature importance причинностью;
- игнорировать baseline;
- сравнивать модели на разных folds;
- оптимизировать leaderboard metric, забывая production cost;
- использовать boosting для временных данных с random CV.

## 27. Как я решаю tabular задачу с boosting

1. Проверяю постановку и leakage.
2. Фиксирую validation protocol.
3. Строю Dummy/linear/Random Forest baseline.
4. Обучаю базовый boosting без огромного tuning.
5. Смотрю learning curves/early stopping.
6. Настраиваю capacity деревьев.
7. Связываю learning rate с количеством iterations.
8. Проверяю stability по folds.
9. Анализирую ошибки и важность.
10. Сравниваю выигрыш с compute/latency.
11. Один раз проверяю на untouched test.

## 28. Минимум в памяти

```text
prediction = initial
for tree in trees:
    tree учится исправлять текущую ошибку
    prediction += learning_rate * tree(x)
```

Параметры, о которых думаю первыми:

```text
learning_rate
n_estimators / iterations
depth / leaves
early_stopping
subsampling
```

## 29. Самопроверка

1. Чем boosting отличается от bagging?
2. Почему в регрессии удобно думать через residuals?
3. Что означает «gradient» в Gradient Boosting?
4. Почему learning rate связан с числом деревьев?
5. Что делает early stopping?
6. Почему слишком глубокие weak learners опасны?
7. В чём общая идея XGBoost, LightGBM и CatBoost?
8. Нужен ли scaling tree boosting?
9. Почему SHAP не доказывает причинность?
10. Почему boosting не спасёт неправильную временную validation?

## 30. Финальная картина курса

После Topic 10 у меня должна сложиться не коллекция алгоритмов, а процесс:

```text
понять данные
↓
сформулировать задачу
↓
выбрать честную validation
↓
построить baseline
↓
сделать признаки без leakage
↓
сравнить простые и сложные модели
↓
проанализировать ошибки
↓
проверить устойчивость
↓
оценить production trade-offs
```

## 31. Связи

Назад → [[Topic 09 - Подробная выжимка]].

Эта тема завершает основной маршрут `mlcourse.ai`, но следующий логичный уровень — не ещё один алгоритм, а полноценный end-to-end ML-проект.
