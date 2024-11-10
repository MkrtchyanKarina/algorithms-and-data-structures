import unittest
from random import randint

import psutil
import time
from prettytable import PrettyTable
from lab3.task1.src.task1 import *

table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1


class QuickSortTest(unittest.TestCase):
    def test_quick_sort0(self):
        global table
        t_start = time.time()
        n = 1
        m = [randint(-10, 10) for i in range(n)]
        result = quick_sort(m)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, sorted(m))
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, m))}', t_end, memory," ".join(map(str, result))])

    def test_quick_sort1(self):
        global table
        t_start = time.time()
        n = 5
        m = [2, 3, 9, 2, 2]
        result = quick_sort(m)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, sorted(m))
        table.add_row(["Значения из примера", f'{n}\n{" ".join(map(str, m))}', t_end, memory," ".join(map(str, result))])

    def test_quick_sort2(self):
        global table
        t_start = time.time()
        n = 10
        m = [randint(-100, 100) for i in range(n)]
        result = quick_sort(m)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, sorted(m))
        table.add_row(["Значения из примера", f'{n}\n{" ".join(map(str, m))}', t_end, memory," ".join(map(str, result))])

    def test_quick_sort3(self):
        global table
        t_start = time.time()
        n = 10**4
        m = [randint(-10**9, 10**9) for i in range(n)]
        result = quick_sort(m)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, sorted(m))
        table.add_row(["Максимальные значения", f'{n}\n{" ".join(map(str, m[:3]))}...', t_end, memory, f'{" ".join(map(str, result[:3]))}...'])
        print()
        print(table)

