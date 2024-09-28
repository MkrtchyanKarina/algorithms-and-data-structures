import random, time, psutil

from lab1.src.verifications import data_verification1

t_start = time.perf_counter()
def swap(a, b):
    c = b
    b = a
    a = c
    return a, b


@data_verification1
def insertion_sort(n, m):
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if m[i] > m[j]:
                m[i], m[j] = swap(m[i], m[j])
                i, j = j, i
    return m

a = int(input())
b = [int(x) for x in input().split()]
print(insertion_sort(a, b))


# test_max_m = [random.randint(-10**9, 10**9) for i in range(10**3)]
# max_result = insertion_sort(10 ** 3, test_max_m)
# if max_result == sorted(test_max_m)[::-1]:
#     print("Время работы: %s секунд" % (time.perf_counter() - t_start))
#     print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
#     print(" ".join(map(str, max_result)))