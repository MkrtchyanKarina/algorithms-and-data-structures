import unittest
from lab2.task5.src.task5 import max_count
import psutil
import time
import random


class InsertionSortTestCase(unittest.TestCase):
    def test_max_count1(self):
        n = 50_000
        test_arr = [5090] * n + [random.randint(0, 10 ** 9) for i in range(n)]
        random.shuffle(test_arr)
        t_start = time.perf_counter()
        self.assertEqual(max_count(n*2, test_arr), 1)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

