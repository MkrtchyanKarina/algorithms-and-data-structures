import unittest
import psutil
import time
import random

from lab2.task3.src.task3 import bubble_sort, number_of_permutations


class PermutationsTest(unittest.TestCase):
    def test_permutations1(self):
        n = 1
        m = [0]
        print(n, *m)
        t_start = time.perf_counter()
        result = number_of_permutations(n, m)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")
        self.assertEqual(result, bubble_sort(n, m))

    def test_permutations2(self):
        n = 1000
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        print(n, *m[:10])
        t_start = time.perf_counter()
        result = number_of_permutations(n, m)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")
        self.assertEqual(result, bubble_sort(n, m))


    def test_permutations3(self):
        n = 10**4
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        print(n, *m[:10])
        t_start = time.perf_counter()
        result = number_of_permutations(n, m)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")
        self.assertEqual(result, bubble_sort(n, m))

    def test_permutations4(self):
        n = 10**5
        m = [random.randint(-10 ** 9, 10 ** 9) for i in range(n)]
        print(n, *m[:10])
        t_start = time.perf_counter()
        number_of_permutations(n, m)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")


