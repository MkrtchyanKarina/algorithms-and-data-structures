import unittest
import psutil
import time
import random

from lab1.task2.src.task2 import insertion_sort

t_start = time.perf_counter()

# test_arr = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]
test_arr = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0,]
test_res = insertion_sort(len(test_arr), test_arr)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


class InsertionSortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(10, [1, 8, 4, 2, 3, 7, 5, 6, 9, 0,]), ([1, 2, 2, 2, 3, 5, 5, 6, 9, 1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))