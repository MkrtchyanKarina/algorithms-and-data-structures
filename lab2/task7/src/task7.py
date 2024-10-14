from random import randint


def line_find_max_subarray_main(*args):
    if len(args) == 1:
        path = args[0]
        file_input = open(path, 'r')
        n = int(file_input.readline().strip())
        array = list(map(int, file_input.readline().strip().split(" ")))
        result = " ".join(map(str, line_find_max_subarray(n, array)))
        file_output = open('output' + path[5:], 'w')
        file_output.write(result)
        file_output.close()
    else:
        n, array = args
        line_find_max_subarray(n, array)


def line_find_max_subarray(n, array):
    if verification(n, array):
        max_sum = 0
        start_index = 0
        end_index = 0
        sums = 0
        for i in range(n):

            if sums == 0:
                start_index = i
            sums += array[i]
            if max_sum < sums:
                max_sum = sums
                end_index = i
            if sums < 0:
                sums = 0
        return start_index, end_index, max_sum


def verification(n, array, attempt=1):
    res = 1
    if type(n) is int and 1 <= n <= 10 ** 5:
        if type(array) is list and n == len(array) and all(type(x) is int and abs(x) <= 10 ** 9 for x in array):
            res = 1
        else:
            res *= 0
    else:
        res *= 0
    if res == 0:
        if attempt == 3:
            return 'Ошибка!'

        else:
            print("Введите данные ещё раз, соблюдая ограничения: ")
            try:
                new_n = int(input())
                new_array = list(map(int, input().split(" ")))
                return verification(new_n, new_array, attempt + 1)
            except:
                return 'Ошибка!'
    else:
        return res






# Запись данных в input файл и запуск программы для этого файла

# file = open('input7.txt', 'w')
# n = 10**5
# m = ' '.join(map(str, [randint(-10**9, 10**9) for i in range(n)]))
# file.write(str(n))
# file.write('\n'+m)
#
# file.close()
# line_find_max_subarray_main('input7.txt')