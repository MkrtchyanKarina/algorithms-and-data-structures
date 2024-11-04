import typing as tp
from random import randint
import time
import psutil

def quick_sort(m):
    if len(m) > 1:
        pivot = m[randint(0, len(m) - 1)]
        start = [i for i in m if i < pivot]
        equal = [i for i in m if i == pivot]
        end = [i for i in m if i > pivot]
        m = quick_sort(start) + equal + quick_sort(end)
    return m
a = randint(-10**9, 10**9)
l = [randint(-10**9, 10**9) for i in range((10**5)//2)] + [a] * (10**5//2)
# print(quick_sort(l) == sorted(l))
# print(l.count(array))

start = time.time()
print(quick_sort(l))
print("Время работы: %s секунд" % (time.time() - start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")