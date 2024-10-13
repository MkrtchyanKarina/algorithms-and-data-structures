from random import randint


def verification(n, array, attempt=1):
    res = 1
    if type(n) is int and 1 <= n <= 10 ** 5:
        if type(array) is list and n == len(array) and all(type(x) is int and abs(x) <= 10 ** 9 for x in array):
            return merge_sort(n, array)
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



def merge_sort_main(*args):
    if len(args) == 1:
        path = args[0]
        file_input = open(path, 'r')
        len_arr = int(file_input.readline().strip())
        array = list(map(int, file_input.readline().strip().split(" ")))

        file_output = open('output' + path[5:], 'w')
        result = " ".join(map(str, verification(len_arr, array)))
        file_output.write(result)
    else:
        len_arr, array = args
        return verification(len_arr, array)


def merge_sort(len_arr, array):
    middle = len_arr // 2
    list_a, list_b = array[:middle], array[middle:]
    len_a, len_b = middle, len_arr - middle
    if len_a > 1:
        list_a = merge_sort(len_a, list_a)
    if len_b > 1:
        list_b = merge_sort(len_b, list_b)
    return merge(len_a, len_b, list_a, list_b)


def merge(len_a, len_b, array_a, array_b):
    len_c = len_a + len_b
    array_c = [0] * len_c
    index_a, index_b = 0, 0
    for index_c in range(len_c):
        if index_b >= len_b:
            array_c[index_c] = array_a[index_a]
            index_a += 1
        elif index_a >= len_a:
            array_c[index_c] = array_b[index_b]
            index_b += 1
        else:
            if array_a[index_a] <= array_b[index_b]:
                array_c[index_c] = array_a[index_a]
                index_a += 1
            else:
                array_c[index_c] = array_b[index_b]
                index_b += 1
    return array_c


# def merge(len_a, len_b, array_a, array_b):
#
#     array_c = []
#     index_a, index_b = 0, 0
#     for i in range(len_a + len_b):
#         if index_b == len_b:
#             array_c.extend(array_a[index_a:])
#             break
#         elif index_a == len_a:
#             array_c.extend(array_b[index_b:])
#             break
#         else:
#             if array_a[index_a] <= array_b[index_b]:
#                 array_c.append(array_a[index_a])
#                 index_a += 1
#             else:
#                 array_c.append(array_b[index_b])
#                 index_b += 1
#
#     return array_c
print(merge_sort_main(2, 26))

# file = open('input1.txt', 'w')
#
# # merge_sort_main('input1.txt')
#
# n = 10**5
# m = ' '.join(map(str, [randint(-10 ** 9, 10 ** 9) for i in range(n)]))
# file.write(str(n))
# file.write('\n'+m)
# merge_sort_main('input1.txt')
