import unittest
import psutil
import time
from lab1.task2.src.task2 import insertion_sort
import random

class InsertionSortTestCase(unittest.TestCase):
    def test_insertion_sort1(self):
        t_start = time.perf_counter()
        self.assertEqual(insertion_sort(1, [0]),
                         ([1], [0]))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_insertion_sort2(self):
        t_start = time.perf_counter()
        self.assertEqual(insertion_sort(10, [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]),
                         ([1, 2, 2, 2, 3, 5, 5, 6, 9, 1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_insertion_sort3(self):
        t_start = time.perf_counter()
        n = 10**3
        insertion_sort(n, [random.randint(-10**9, 10**9) for i in range(n)])
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")