import unittest
from lab1.task7.src.task7 import sort_land
import psutil
import time
import random
from statistics import median


class InsertionSortTestCase(unittest.TestCase):
    def test_insertion_sort1(self):
        t_start = time.perf_counter()
        self.assertEqual(sort_land(3, [1.19, 8.9, 0.4]), (3, 1, 2))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_insertion_sort2(self):
        t_start = time.perf_counter()
        self.assertEqual(sort_land(5, [10.00, 8.70, 0.01, 5.00, 3.00]), (3, 4, 1))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_insertion_sort3(self):
        n = 9999
        M = [round(random.random(), 2) + random.randint(0, 10 ** 6 - 1) for i in range(n)]
        ind1 = M.index(min(M))+1
        ind2 = M.index(median(M))+1
        ind3 = M.index(max(M))+1
        t_start = time.perf_counter()
        self.assertEqual(sort_land(n, M), (ind1,ind2, ind3))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")