import unittest
import psutil
import time
import random

from lab2.task7.src.task7 import line_find_max_subarray


class MaxSubarrayTest(unittest.TestCase):
    def test_max_subarray1(self):
        n = 1
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        print(n, *m[:10])
        t_start = time.perf_counter()
        result = line_find_max_subarray(n, m)
        res = sum(m[result[0]:result[1]+1])
        if res < 0:
            res = 0
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")
        self.assertEqual(result[2], res)


    def test_max_subarray2(self):
        n = 1000
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        print(n, *m[:10])
        t_start = time.perf_counter()
        result = line_find_max_subarray(n, m)
        res = sum(m[result[0]:result[1]+1])
        if res < 0:
            res = 0
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")
        self.assertEqual(result[2], res)

    def test_max_subarray3(self):
        n = 10**4
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        print(n, *m[:10])
        t_start = time.perf_counter()
        result = line_find_max_subarray(n, m)
        res = sum(m[result[0]:result[1]+1])
        if res < 0:
            res = 0
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")
        self.assertEqual(result[2], res)


    def test_max_subarray4(self):
        n = 10**5
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        print(n, *m[:10])
        t_start = time.perf_counter()
        result = line_find_max_subarray(n, m)
        res = sum(m[result[0]:result[1]+1])
        if res < 0:
            res = 0
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")
        self.assertEqual(result[2], res)



