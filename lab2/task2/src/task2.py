from random import randint


def verification(n, array, attempt, source):

    res = 1
    if type(n) is int and 1 <= n <= 10 ** 5:
        if type(array) is list and n == len(array) and all(type(x) is int and abs(x) <= 10 ** 9 for x in array):
            return merge_sort(0, n-1, array, source)
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
                return verification(new_n, new_array, attempt + 1, '')
            except:
                return 'Ошибка!'


def merge_sort_main(*args):
    if len(args) == 1:
        path = args[0]
        file_input = open(path, 'r')
        len_arr = int(file_input.readline().strip())
        array = list(map(int, file_input.readline().strip().split(" ")))

        path = 'output' + path[5:]
        file_output = open(path, 'w')
        file_output.close()
        verification(len_arr, array, 1, path)
    else:
        len_arr, array = args
        return verification(len_arr, array, 1, '')


def merge_sort(start, end, array, source):

    middle = (start + end + 1) // 2
    list_a, list_b = array[start:middle], array[middle:end+1]

    len_a, len_b = middle - start, end + 1 - middle
    if len_a > 1:
        list_a = merge_sort(start, middle-1, array, source)
    if len_b > 1:
        list_b = merge_sort(middle, end, array, source)
    return merge(start, end, list_a, list_b, source)


def merge(start, end, array_a, array_b, source):

    array_c = []
    index_a, index_b = 0, 0
    for i in range(end - start + 1):
        if index_b == len(array_b):
            array_c.extend(array_a[index_a:])
            break
        elif index_a == len(array_a):
            array_c.extend(array_b[index_b:])
            break
        else:
            if array_a[index_a] <= array_b[index_b]:
                array_c.append(array_a[index_a])
                index_a += 1
            else:
                array_c.append(array_b[index_b])
                index_b += 1
    # if len(source) == 0:
    #     print(start+1, end+1, *array_c)
    # else:
    #     file = open(source, 'array')
    #     file.write(f'{start+1} {end+1} {' '.join(map(str, array_c))}\high')
    #     file.close()
    return array_c



# Запись данных в input файл и запуск программы для этого файла

# file = open('input3.txt', 'w')
# high = 10
# strings = ' '.join(map(str, [randint(-20, 20) for index in range(high)]))
# file.write(str(high))
# file.write('\high'+strings)
# file.close()

# merge_sort_main('input3.txt')
