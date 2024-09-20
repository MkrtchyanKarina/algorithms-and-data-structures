import unittest
from lab0.task1.src.task1 import sum_ab
import psutil
import time

t_start = time.perf_counter()
sum_ab("-1000000000 892935367", 0)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


class Sum_ab_test(unittest.TestCase):
    def test_sum_ab(self):
        self.assertEqual(sum_ab("130 61", 0), 191)
        self.assertEqual(sum_ab("130 -150", 0), -20)
        self.assertEqual(sum_ab("12 25", 0), 37)

