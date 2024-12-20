# 4 задача по выбору. Линейный поиск
**Студентка ИТМО,  Мкртчян Карина Геворговна  466745**  

## Вариант 12

## Задание
Рассмотрим задачу поиска.
- Формат входного файла. Последовательность из n чисел A = a1, a2, ... , an
в первой строке, числа разделены пробелом, и значение V во второй строке.
Ограничения: 0 ≤ n ≤ 10^3, −10^3 ≤ ai, V ≤ 10^3
- Формат выходного файла. Одно число - индекс i, такой, что V = A[i],
или значение −1, если V отсутствует.
- Напишите код линейного поиска, при работе которого выполняется сканирование последовательности в поисках значения V .
- Если число встречается несколько раз, то выведите, сколько раз встречается
число и все индексы i через запятую.
- Дополнительно: попробуйте найти свинью, как в лекции. Используйте во
входном файле последовательность слов из лекции, и найдите соответствующий индекс.


## Input / Output 

| Input                                  | Output       |
|----------------------------------------|--------------|
| 1 56 78 27 454 2 3 454 89 13 <br/> 454 | 2 <br/> 4, 7 |



## Ограничения по времени и памяти

- Ограничение по времени. Отсутствует.
- Ограничение по памяти. Отсутствует.


## Запуск проекта
1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/MkrtchyanKarina/algorithms-and-data-structures.git
   ```
2. **Перейдите в папку с проектом**
   ```bash
   cd algorithms-and-data-structures/lab1
   ```
3. **Запустить все лабораторные**
    ```bash
   python src/main.py
   ```
4. **Запустить все тесты**
    ```bash
   python -m unittest discover
   ```