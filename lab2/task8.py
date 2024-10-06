import time

import psutil

A = [2, -1, 4, 3, -5, 8, 2, 3, 19]
B = [1, -7, 2, 1, -3, -2, 2, -1, 4]
C = [0] * (len(A) * 2 - 1)
def multiply(ind_a, ind_b):
    # print(ind_a, ind_b)
    global A, B, C
    for i in ind_a:
        for j in ind_a:
            C[i+j] += A[i] * B[j]
    for i in ind_b:
        for j in ind_b:
            C[i+j] += A[i] * B[j]

    for i in ind_a:
        for j in ind_b:
            C[i+j] += A[i] * B[j]
            C[i + j] += A[j] * B[i]
    return C


def merge(len_arr, array):

    middle = len_arr // 2
    list_a, list_b = array[:middle], array[middle:]
    return multiply(list_a, list_b)

# [2, -15, 15, -25, -25, 52, -67, -21, 36, -141, 22, 39, -87, -2, 43, -7, 76]






t_start = time.perf_counter()
print(merge(9, [8, 7, 6, 5, 4, 3, 2, 1, 0]))
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")