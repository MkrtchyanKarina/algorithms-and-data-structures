# 1 задача. Улучшение Quick sort.
**Студентка ИТМО,  Мкртчян Карина Геворговна  466745**  

## Вариант 12

## Задание
Используя псевдокод процедуры Randomized - QuickSort, а так же Partition
из презентации к Лекции 3 (страницы 8 и 12), напишите программу быстрой
сортировки на Python и проверьте ее, создав несколько рандомных массивов,
подходящих под параметры:
- Формат входного файла (input.txt). В первой строке входного файла
содержится число n (1 ≤ n ≤ 10^4) — число элементов в массиве.
Во второй строке находятся n различных целых чисел, по модулю не
превосходящих 10^9
- Формат выходного файла (output.txt). Одна строка выходного файла
с отсортированным массивом. Между любыми двумя числами должен
стоять ровно один пробел.

  
## Input / Output 

| Input           | Output     |
|-----------------|------------|
| 5<br/>2 3 9 2 2 | 2 2 2 3 9  |




## Ограничения по времени и памяти

- Ограничение по времени. 2 сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/MkrtchyanKarina/algorithms-and-data-structures.git
   ```
2. **Перейдите в папку с проектом**
   ```bash
   cd algorithms-and-data-structures/lab5
   ```
3. **Запустить все лабораторные**
    ```bash
   python src/main.py
   ```
4. **Запустить все тесты**
    ```bash
   python -documents_count unittest discover -v
   ```