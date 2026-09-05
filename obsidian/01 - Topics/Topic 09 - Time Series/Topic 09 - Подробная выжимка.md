---
type: topic-summary
topic: 09
status: solid
tags: [time-series, forecasting, validation, leakage]
---
# Topic 09 — Подробная выжимка

## Прогноз начинается с горизонта
Нельзя просто сказать «предсказываю продажи». Нужно определить момент формирования прогноза и horizon: завтра, через 7 дней, на следующий месяц. От этого зависит, какие признаки реально доступны.

## Компоненты
Trend — долгосрочное направление. Seasonality — повторяющийся календарный паттерн. Autocorrelation — связь ряда с его прошлыми значениями. Noise — непредсказуемая часть в рамках выбранной модели.

## Baseline
`y[t-1]`, seasonal naive `y[t-7]`, историческое среднее — обязательные конкуренты. Сложная модель имеет смысл только если стабильно превосходит разумный baseline на будущих периодах.

## Lag features
`lag_1`, `lag_7`, rolling mean/std. Важно делать `shift(1)` перед rolling, если текущее значение target в момент prediction неизвестно. Иначе получаю target leakage.

## Validation
Random split почти всегда неверен для forecast. Использую chronological holdout, expanding window или rolling window (`TimeSeriesSplit`). Folds должны имитировать реальный сценарий: обучаюсь на прошлом, проверяюсь на более позднем будущем.

## Prophet и подобные модели
Инструмент вторичен. Сначала нужно понять baseline, seasonality, holidays/regressors, horizon и backtesting. Библиотека не исправляет неправильную постановку временной задачи.

## Drift
У временного ряда качество может деградировать по календарю. Поэтому кроме средней CV-метрики смотрю score по folds/периодам, residuals во времени и устойчивость к смене режима.

## Чеклист
1. Когда формируется прогноз?
2. Какой horizon?
3. Какие данные доступны именно тогда?
4. Какой naive baseline?
5. Есть ли leakage в rolling/aggregates?
6. Validation воспроизводит production timeline?
