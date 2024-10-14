import unittest
import psutil
import time
import random

from lab2.task8.src.task8 import karatsuba_polynomial_multiply
def poly_multiply(n, A, B):
    C = [0] * (2*n - 1)
    for i in range(n):
        for j in range(n):

            C[i+j] += A[i] * B[j]
    return ' '.join(map(str, C))


class PolyMultiplyTest(unittest.TestCase):
    def test_multiply1(self):
        n = 1
        A = [4]
        B = [5]
        print(f'{n}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}')

        t_start = time.perf_counter()
        result = karatsuba_polynomial_multiply(n, A, B)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")

        self.assertEqual(result, poly_multiply(n, A, B))

    def test_multiply2(self):
        n = 100
        A = [random.randint(-10 ** 3, 10 ** 3) for i in range(n)]
        B = [random.randint(-10 ** 3, 10 ** 3) for i in range(n)]
        print(f'{n}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}')

        t_start = time.perf_counter()
        result = karatsuba_polynomial_multiply(n, A, B)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")

        self.assertEqual(result, poly_multiply(n, A, B))

    def test_multiply3(self):
        n = 10**3
        A = [random.randint(-10 ** 5, 10 ** 5) for i in range(n)]
        B = [random.randint(-10 ** 5, 10 ** 5) for i in range(n)]
        print(f'{n}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}')

        t_start = time.perf_counter()
        result = karatsuba_polynomial_multiply(n, A, B)
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ \n")

        self.assertEqual(result, poly_multiply(n, A, B))



