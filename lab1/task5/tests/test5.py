import unittest
from lab1.task5.src.task5 import selection_sort
import psutil
import time
import random


class InsertionSortTestCase(unittest.TestCase):
    def test_selection_sort1(self):
        t_start = time.perf_counter()
        self.assertEqual(selection_sort(1, [0]), [0])
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_selection_sort2(self):
        m = [31, 41, 59, 26, 41, 58]
        t_start = time.perf_counter()
        self.assertEqual(selection_sort(6, m), sorted(m))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_selection_sort3(self):
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]
        t_start = time.perf_counter()
        self.assertEqual(selection_sort(1000, m), sorted(m))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")