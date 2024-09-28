import unittest

from lab1.task1.src.task1 import insertion_sort

import psutil
import time
import random

t_start = time.perf_counter()
# test_arr = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]
test_arr = [31, 41, 59, 26, 41, 58]
# test_arr = [0]

test_res = insertion_sort(len(test_arr), test_arr)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


class InsertionSortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(5, [23, 4, 89, -10, -10]), [-10, -10, 4, 23, 89])
        self.assertEqual(insertion_sort(8, [23, 4, 3, -100, 10, 89, -10, -10]), [-100, -10, -10, 3, 4, 10, 23, 89])
        max_arr = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]
        self.assertEqual(insertion_sort(10 ** 3, max_arr), sorted(max_arr))