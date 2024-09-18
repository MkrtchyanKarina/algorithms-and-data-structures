import psutil
import time
import unittest
from lab0.task3.src.fib_matrix import last_digit

t_start = time.perf_counter()
# last_digit(331)
last_digit(10**7)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


class fib_number_test(unittest.TestCase):
    def test_fib_number(self):
        self.assertEqual(last_digit(0), 0)
        self.assertEqual(last_digit(10), 5)
        self.assertEqual(last_digit(13), 3)
        self.assertEqual(last_digit(45), 0)
        self.assertEqual(last_digit(331), 9)