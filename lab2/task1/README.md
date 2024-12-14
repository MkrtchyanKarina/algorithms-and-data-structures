# 1 задача. Сортировка слиянием
**Студентка ИТМО,  Мкртчян Карина Геворговна  466745**  

## Вариант 12

## Задание
Используя псевдокод процедур Merge и Merge-sort из презентации к Лекции 2 (страницы 6-7), напишите программу сортировки слиянием на Python и
проверьте сортировку, создав несколько рандомных массивов, подходящих
под параметры:
- Формат входного файла (input.txt). В первой строке входного файла
содержится число n (1 ≤ n ≤ 2*10^4) — число элементов в массиве.
Во второй строке находятся n различных целых чисел, по модулю не
превосходящих 10^9.
- Формат выходного файла (output.txt). Одна строка выходного файла
с отсортированным массивом. Между любыми двумя числами должен
стоять ровно один пробел.

  
## Input / Output 

| Input                         |  Output                |
|-------------------------------|------------------------|
| 10<br/>19 5 -2 -6 -9 2 -9 -10 | -10 -9 -9 -6 -2 2 5 19 |




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