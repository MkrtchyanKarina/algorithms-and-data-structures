import unittest

from lab1.task3.src.task3 import insertion_sort
from lab1.task3.src.task3_recursion import insertion_sort_rec

import psutil
import time
import random

t_start = time.perf_counter()
# test_arr = [0]
test_arr = [31, 41, 59, 26, 41, 58]
# test_arr = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]

test_res = insertion_sort_rec(len(test_arr), test_arr)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


class InsertionSortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(5, [23, 4, 89, -10, -10]), [89, 23, 4, -10, -10])
        self.assertEqual(insertion_sort(8, [23, 4, 3, -100, 10, 89, -10, -10]), [89, 23, 10, 4, 3, -10, -10, -100])

        max_arr = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]

        self.assertEqual(insertion_sort(10 ** 3, max_arr), sorted(max_arr)[::-1])

    def test_insertion_sort_recursion(self):
        self.assertEqual(insertion_sort_rec(5, [23, 4, 89, -10, -10]), [89, 23, 4, -10, -10])
        self.assertEqual(insertion_sort_rec(8, [23, 4, 3, -100, 10, 89, -10, -10]), [89, 23, 10, 4, 3, -10, -10, -100])

        max_arr = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]

        self.assertEqual(insertion_sort_rec(10 ** 3, max_arr), sorted(max_arr)[::-1])