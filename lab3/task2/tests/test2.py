import unittest
import psutil
import time
from prettytable import PrettyTable
from lab3.task2.src.task2 import *

table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1


class ScarecrowSortTest(unittest.TestCase):
    def test_worst_case0(self):
        global table
        t_start = time.time()
        n = 1
        result = worst_case(n)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, [1])
        table.add_row(["Минимальные значения", n, t_end, memory," ".join(map(str, result))])

    def test_worst_case1(self):
        global table
        t_start = time.time()
        n = 3
        result = worst_case(n)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, [1, 3, 2])
        table.add_row(["Значения из примера", n, t_end, memory," ".join(map(str, result))])

    def test_worst_case2(self):
        global table
        t_start = time.time()
        n = 10
        result = worst_case(n)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, [1, 4, 6, 8, 10, 5, 3, 7, 2, 9])
        table.add_row(["Минимальные значения", n, t_end, memory," ".join(map(str, result))])

    def test_worst_case3(self):
        global table
        t_start = time.time()
        n = 10**6
        result = worst_case(n)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        table.add_row(["Минимальные значения", n, t_end, memory,f'{" ".join(map(str, result[:10]))}...'])
        print(f'\n{__file__}')
        print(table)
