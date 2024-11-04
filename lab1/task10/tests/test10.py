import unittest
from lab1.task10.src.task10 import palindrome
import psutil
import time
import random


class InsertionSortTestCase(unittest.TestCase):
    def test_palindrome1(self):
        t_start = time.perf_counter()
        self.assertEqual(palindrome(1, "array"), "array")
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_palindrome2(self):
        t_start = time.perf_counter()
        self.assertEqual(palindrome(10, "ABDRBCANOR"), "ABRCRBA")
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_palindrome3(self):
        t_start = time.perf_counter()
        self.assertEqual(palindrome(3, "AAB"), "ABA")
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_palindrome4(self):
        t_start = time.perf_counter()
        self.assertEqual(palindrome(6, "QAZQAZ"), "AQZZQA")
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_palindrome5(self):
        t_start = time.perf_counter()
        self.assertEqual(palindrome(6, "ABCDEF"), "array")
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

    def test_palindrome6(self):
        str_test = "".join(chr(random.randint(65, 90)) for i in range(10**5))
        t_start = time.perf_counter()
        palindrome(10**5, str_test)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")