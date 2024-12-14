# 11 задача. Бюрократия.
**Студентка ИТМО,  Мкртчян Карина Геворговна  466745**  

## Вариант 12

## Задание 
В министерстве бюрократии одно окно для приема граждан. Утром в очередь
встают n человек, i-й посетитель хочет получить ai справок. За один прием можно
получить только одну справку, поэтому если после приема посетителю нужны
еще справки, он встает в конец очереди. За время приема министерство успевает
выдать m справок. Остальным придется ждать следующего приемного дня. Ваша
задача - сказать, сколько еще справок хочет получить каждый из оставшихся
в очереди посетитель в тот момент, когда прием закончится. Если все к этому
моменту разойдутся, выведите -1.
- Формат входного файла (input.txt). В первой строке - количество посетителей n ( 1 ≤ n ≤ 10^5) и количество справок m ( 0 ≤ m ≤ 10^9).
Во второй строке для каждого посетителя в порядке очереди указано количество справок ai (1 ≤ ai ≤ 10^6), которое он рассчитывает получить.
Номером посетителя называется его место в исходной очереди.
- Формат выходного файла (output.txt). В первой строке выведите, сколько
посетителей останется в очереди, когда прием закончится. Во второй строке выведите состояние очереди на тот момент, когда прием закончится: для
всех посетителей по порядку выведите по одному числу через пробел - количество справок, которое он хочет еще получить. В случае, если в очереди
никого не останется выведите одно число: -1


  
## Input / Output 

| Input             | Output        |
|-------------------|---------------|
| 3 2 <br/> 1 2 3   | 2 <br/> 3 1   |
| 4 5 <br/> 2 5 2 3 | 3 <br/> 4 1 2 |




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