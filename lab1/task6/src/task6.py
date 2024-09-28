import psutil
import time
import random
from lab1.src.verifications import data_verification1
t_start = time.perf_counter()

@data_verification1
def bubble_sort(n, m):
    for i in range(n):
        for j in range(i+1, n):
            if m[i] > m[j]:
                m[i], m[j] = m[j], m[i]
    return m


test_max_m = [random.randint(-10**9, 10**9) for i in range(10**3)]
max_result = bubble_sort(10 ** 3, test_max_m)
if max_result == sorted(test_max_m):
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
    print(" ".join(map(str, max_result)))

