import unittest
from lab0.task1.src.task2 import sum_ab2
import psutil
import time

t_start = time.perf_counter()
sum_ab2("-1000000000 892935367", 0)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


class Sum_ab2_test(unittest.TestCase):
    def test_sum_ab2(self):
        self.assertEqual(sum_ab2("130 61", 0), 3851)
        self.assertEqual(sum_ab2("12 -25", 0), 637)
        self.assertEqual(sum_ab2("-25 4", 0), -9)