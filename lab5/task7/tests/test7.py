import time
import unittest
from random import randint
import psutil

from lab5.task7.src.task7 import heap_sort_max
from lab5.src.utils import table


class TestHeapSort(unittest.TestCase):
    def test_should_heapsort_small_arr(self):
        # given
        n = 10**3
        array = [randint(-10**9, 10**9) for _ in range(n)]

        # when
        t_start = time.perf_counter()
        result = heap_sort_max(n, array)
        t_end = time.perf_counter() - t_start
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, sorted(array)[::-1])
        table.add_row(["Минимальные значения", f'{n}\n{array[:4]}', t_end, memory, f'{result[:4]}'])

        print()
        print(table)
        table.clear_rows()



    def test_should_heapsort_middle_arr(self):
        # given
        n = 10**4
        array = [randint(-10**9, 10**9) for _ in range(n)]

        # when
        t_start = time.perf_counter()
        result = heap_sort_max(n, array)
        t_end = time.perf_counter() - t_start
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, sorted(array)[::-1])
        table.add_row(["Средние значения", f'{n}\n{array[:4]}', t_end, memory, f'{result[:4]}'])

        print()
        print(table)
        table.clear_rows()


    def test_should_heapsort_big_arr(self):
        # given
        n = 10**5
        array = [randint(-10**9, 10**9) for _ in range(n)]

        # when
        t_start = time.perf_counter()
        result = heap_sort_max(n, array)
        t_end = time.perf_counter() - t_start
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, sorted(array)[::-1])
        table.add_row(["Максимальные значения", f'{n}\n{array[:4]}', t_end, memory, f'{result[:4]}'])

        print()
        print(table)
        table.clear_rows()



    def test_should_heapsort_repeat(self):
        # given
        n = 10**5
        x, y = randint(-10**9, 10**9), randint(10**9, 10**9)
        array = [[x, y][i % 2] for i in range(n)]

        # when
        t_start = time.perf_counter()
        result = heap_sort_max(n, array)
        t_end = time.perf_counter() - t_start
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, sorted(array)[::-1])
        table.add_row(["Повторяющиеся значения", f'{n}\n{array[:4]}', t_end, memory, f'{result[:4]}'])

        print()
        print(table)
        table.clear_rows()

if __name__ == "__main__":
    unittest.main()
