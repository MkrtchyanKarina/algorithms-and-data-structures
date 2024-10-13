import unittest
import psutil
import time
import random

from lab2.task1.src.task1 import merge_sort_main


class MergeSortTest(unittest.TestCase):
    def test_merge_sort1(self):
        n = 1
        m = [0]
        t_start = time.perf_counter()
        self.assertEqual(merge_sort_main(n, m), sorted(m))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")



    def test_merge_sort2(self):
        n = 1000
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]

        t_start = time.perf_counter()
        self.assertEqual(merge_sort_main(n, m), sorted(m))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_merge_sort3(self):
        n = 1000
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]

        t_start = time.perf_counter()
        self.assertEqual(merge_sort_main(n, m), sorted(m))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_merge_sort4(self):
        n = 10**4
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]

        t_start = time.perf_counter()
        self.assertEqual(merge_sort_main(n, m), sorted(m))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_merge_sort5(self):
        n = 10**5
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]

        t_start = time.perf_counter()
        self.assertEqual(merge_sort_main(n, m), sorted(m))
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
# 4.437565200030804

