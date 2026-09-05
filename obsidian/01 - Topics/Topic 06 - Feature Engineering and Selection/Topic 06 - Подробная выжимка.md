---
type: topic-summary
topic: 06
status: solid
tags: [feature-engineering, feature-selection, leakage, pipelines]
---
# Topic 06 — Подробная выжимка

## Feature engineering
Это перевод сырых данных в представление, в котором модели легче выделить полезный сигнал. Хороший признак должен иметь смысл, быть доступен в момент реального прогноза и воспроизводимо строиться одинаково на train и production.

Типичные операции: логарифмы для длинных хвостов, отношения и разности, временные признаки, агрегаты, категории, interactions, обработка missing values.

## Leakage
Главный риск: случайно использовать информацию из validation/test или будущего. Даже «безобидная» медиана, рассчитанная по всему датасету, уже подглядывает в validation distribution. Поэтому `Imputer`, `Scaler`, encoder и selector помещаю внутрь `Pipeline`.

## Категории
One-hot хорош для умеренной cardinality. High-cardinality требует осторожности: hashing, frequency/target encoding с корректным out-of-fold расчётом. Target encoding по полному train без OOF создаёт leakage.

## Feature selection
Filter methods оценивают признаки независимо/почти независимо от итоговой модели. Embedded methods используют саму модель (`L1`, tree importance). Wrapper methods многократно обучают модель и стоят дороже.

## Когда удалять признаки
Не ради красивой таблицы. Цели: уменьшить стоимость сбора/инференса, variance, память, latency, повысить интерпретируемость или убрать шум.

## Чеклист
1. Доступен ли признак в момент prediction?
2. Нет ли будущего/target proxy?
3. Все transforms внутри CV?
4. Стабилен ли эффект на нескольких folds?
5. Оправдывает ли улучшение дополнительную сложность?
