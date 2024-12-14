# 7 задача. Поиск максимального подмассива за линейное время.
**Студентка ИТМО,  Мкртчян Карина Геворговна  466745**  

## Вариант 12

## Задание
Можно найти максимальный подмассив за линейное время, воспользовавшись
следующими идеями. Начните с левого конца массива и двигайтесь вправо, отслеживая найденный к данному моменту максимальный подмассив. Зная максимальный подмассив массива A[1..j], распространите ответ на поиск максимального
подмассива, заканчивающегося индексом j + 1, воспользовавшись следующим
наблюдением: максимальный подмассив массива A[1..j + 1] представляет собой
либо максимальный подмассив массива A[1..j], либо подмассив A[i..j + 1] для
некоторого 1 ≤ i ≤ j + 1. Определите максимальный подмассив вида A[i..j + 1]
за константное время, зная максимальный подмассив, заканчивающийся индексом
j.
В этом случае у вас возможны 2 варианта тестирования: первый предполагает
создание рандомного массива чисел, аналогично задаче №1 (в этом случае формат входного и выходного файла смотрите там). Второй вариант - взять любые
данные по акциям какой-либо компании, аналогично задаче №6.

  
## Input / Output 

| Input                           | Output |
|---------------------------------|--------|
| 10<br/>6 8 -2 5 -10 5 5 -1 4 -8 | 0 8 20 |




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