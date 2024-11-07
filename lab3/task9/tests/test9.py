from lab3.task9.src.task9 import *
import time
import psutil


def test_shortest_distance():
    assert shortest_distance([Dot(0, 0), Dot(3, 4)], 2) == 5.0
    dots = create_new_dots(1000, -100, 100)
    assert shortest_distance(dots, 1000) == slow_shortest_distance(dots, 1000)


dots = centre_dots(10**5, -10**9, 10**9)
start = time.time()
print(shortest_distance(dots, 10**5))
print("Время работы: %s секунд" % (time.time() - start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")