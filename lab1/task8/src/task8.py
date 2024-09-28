

import psutil
import time
import random

from lab1.src.verifications import data_verification8

t_start = time.perf_counter()


@data_verification8
def swap(n, m):
    for i in range(n-1):
        index = i + 1
        minim = m[i]

        for j in range(i+1, n):
            if m[j] < minim:
                minim = m[j]
                index = j
        if minim < m[i]:
            m[i], m[index] = m[index], m[i]

            print("Swap elements in indices " + str(i+1) + " and " + str(index+1) + ".")
        else:
            print("No more swaps needed.")

swap(5, [3, 1, 4, 2, 2])

# test_max_m = [random.randint(-10**9, 10**9) for i in range(10**5)]
# swap(10**5, test_max_m)
# print("Время работы: %s секунд" % (time.perf_counter() - t_start))
# print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

