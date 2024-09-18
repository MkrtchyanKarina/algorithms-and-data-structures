import psutil
import time
from lab0.task2.src.fib_matrix import fib_number
import unittest

t_start = time.perf_counter()
# fib_number(0)
# fib_number(10)
fib_number(45)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


class fib_number_test(unittest.TestCase):
    def test_fib_number(self):
        self.assertEqual(fib_number(0), 0)
        self.assertEqual(fib_number(10), 55)
        self.assertEqual(fib_number(13), 233)
        self.assertEqual(fib_number(45), 1134903170)