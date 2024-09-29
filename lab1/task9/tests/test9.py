import unittest
import random
from lab1.task9.src.task9 import sum_dv
import psutil
import time


class InsertionSortTestCase(unittest.TestCase):

    def test_insertion_sort1(self):
        a, b = "1", "1"
        t_start = time.perf_counter()
        self.assertEqual(sum_dv(a, b), "10")
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_insertion_sort2(self):
        a, b = "111000", "010101"
        t_start = time.perf_counter()
        self.assertEqual(sum_dv(a, b), bin(int(a, 2) + int(b, 2))[2:])
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_insertion_sort3(self):
        n = 10**3
        a = "".join(map(str, [round(random.random()) for i in range(n)]))
        b = "".join(map(str, [round(random.random()) for j in range(n)]))
        t_start = time.perf_counter()
        self.assertEqual(sum_dv(a, b), bin(int(a, 2) + int(b, 2))[2:])
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")