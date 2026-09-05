# mlcourse

Личный репозиторий с практическими работами по курсу [mlcourse.ai](https://mlcourse.ai/), русская версия материалов: [jupyter_russian](https://github.com/Yorko/mlcourse.ai/tree/main/jupyter_russian).

## Структура

Каждая тема хранится в отдельной директории. Внутри удобно держать исходный ноутбук, собственные решения, данные (если их разрешено публиковать) и краткие выводы.

```text
mlcourse/
├── topic01_pandas_data_analysis/   # Pandas и анализ данных
├── .gitignore
└── README.md
```

## Как работать

1. Откройте соответствующий ноутбук из [материалов курса](https://github.com/Yorko/mlcourse.ai/tree/main/jupyter_russian).
2. Создайте или скопируйте ноутбук в папку нужной темы.
3. Сохраните решение и выводы рядом с ним.
4. Зафиксируйте изменения:

   ```bash
   git add topic01_pandas_data_analysis
   git commit -m "Solve pandas data analysis exercises"
   git push
   ```

## Окружение

Для запуска ноутбуков подойдёт Python 3.11+ и JupyterLab:

```bash
python -m venv .venv
source .venv/bin/activate
pip install jupyterlab pandas numpy matplotlib seaborn scikit-learn
jupyter lab
```

> Исходные учебные материалы принадлежат их авторам. В этом репозитории размещаются только мои решения, заметки и разрешённые для публикации данные.
