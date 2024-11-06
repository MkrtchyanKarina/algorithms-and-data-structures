import pytest
from lab3.task9.src.task9 import shortest_distance, distance
from random import randint
import time
import psutil
def min_distance2(count, dots):
    d_min = 2*10**9
    for i in range(count-1):
        for j in range(i+1, count):
            d_min = min(d_min, distance([dots[i], dots[j]]))
    return d_min

def write_dots(count, start, end):
    dots = [()]*count
    for i in range(count):
        dots[i] = (randint(start, end), randint(start, end))
    return dots

def test_shortest_distance():
    assert shortest_distance(2, [(0, 0), (3, 4)]) == 5.0
    # dots = write_dots(100, -1000, 1000)
    # assert shortest_distance(100, dots) == min_distance2(100, dots)


dots = write_dots(10**5, -10**9, 10**9)
start = time.time()
print(shortest_distance(10**5, dots))
print("Время работы: %s секунд" % (time.time() - start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")