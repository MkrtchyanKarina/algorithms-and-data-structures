# Задание №4 по варианту: Построение пирамиды
**Студентка ИТМО,  Мкртчян Карина Геворговна  466745**  

## Вариант 12

## Задание 
В этой задаче вы преобразуете массив целых чисел в пирамиду. Это важнейший шаг алгоритма сортировки под названием HeapSort. Гарантированное время
работы в худшем случае составляет O(n log n), в отличие от среднего времени работы QuickSort, равного O(n log n). QuickSort обычно используется на
практике, потому что обычно он быстрее, но HeapSort используется для внешней сортировки, когда вам нужно отсортировать огромные файлы, которые не
помещаются в памяти вашего компьютера.

Первым шагом алгоритма HeapSort является создание пирамиды (heap) из
массива, который вы хотите отсортировать.

Ваша задача - реализовать этот первый шаг и преобразовать заданный массив целых чисел в пирамиду. Вы сделаете это, применив к массиву определенное
количество перестановок (swaps). Перестановка - это операция, как вы помните,
при которой элементы ai и aj массива меняются местами для некоторых i и j.
Вам нужно будет преобразовать массив в пирамиду, используя только O(n) перестановок. Обратите внимание, что в этой задаче вам нужно будет использовать
min-heap вместо max-heap.

• Формат ввода или входного файла (input.txt). 

Первая строка содержит
целое число n (1 ≤ n ≤ 10^5), вторая содержит n целых чисел ai входного
массива, разделенных пробелом (0 ≤ ai ≤ 10^9, все ai - различны.

• Формат выходного файла (output.txt). 

Первая строка ответа должна содержать целое число m - количество сделанных свопов. Число m должно
удовлетворять условию 0 ≤ m ≤ 4n. Следующие m строк должны содержать по 2 числа: индексы i и j сделанной перестановки двух элементов,
индексы считаются с 0. После всех перестановок в нужном порядке массив должен стать пирамидой, то есть для каждого i при 0 ≤ i ≤ n−1 должны
выполняться условия:
1. если 2i + 1 ≤ n − 1, то ai < a2i+1,
2. если 2i + 2 ≤ n − 1, то ai < a2i+2.

Обратите внимание, что все элементы входного массива различны. Любая
последовательность свопов, которая менее 4n и после которой входной массив становится корректной пирамидой, считается верной.

## Input / Output 

| Input               | Output                  |
|---------------------|-------------------------|
| 5 3 <br/> 5 4 3 2 1 | 1 4 <br/> 0 1 <br/> 1 3 |
| 5 <br/> 1 2 3 4 5   | 0                       |

## Ограничения по времени и памяти

- Ограничение по времени. 3 сек.
- Ограничение по памяти. 512 мб.



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