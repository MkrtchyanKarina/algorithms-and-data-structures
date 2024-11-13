import unittest
import psutil
import time
from prettytable import PrettyTable
from lab3.task3.src.task3 import *
from random import randint

table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1


class ScarecrowSortTest(unittest.TestCase):
    def test_scr_sort0(self):
        global table
        l = [2]
        t_start = time.time()
        result = scarecrow_sort(1, 1, l)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, 'ДА')
        table.add_row(["Минимальные значения", f'{' '.join(map(str, l))}', t_end, memory,result])

    def test_scr_sort1(self):
        global table
        l = [2, 1, 3]
        t_start = time.time()
        result = scarecrow_sort(3, 2, l)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, 'НЕТ')
        table.add_row(["Значения из примера", f'{' '.join(map(str, l))}', t_end, memory,result])

    def test_scr_sort2(self):
        global table
        l = [1, 5, 3, 4, 1, 7, 6, 8, 2]
        t_start = time.time()
        result = scarecrow_sort(9, 4, l)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, 'НЕТ')
        table.add_row(["Значения из примера", f'{' '.join(map(str, l))}', t_end, memory,result])

    def test_scr_sort3(self):
        global table
        l = [1, 5, 3, 4, 1]
        t_start = time.time()
        result = scarecrow_sort(5, 3, l)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, 'ДА')
        table.add_row(["Значения из примера", f'{' '.join(map(str, l))}', t_end, memory,result])

    def test_scr_sort4(self):
        global table
        l = [randint(-10**9, 10**9) for i in range(10**5)]
        t_start = time.time()
        result = scarecrow_sort(10**5, 10, l)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        table.add_row(["Максимальные значения", f'{' '.join(map(str, l[:4]))}', t_end, memory,result])
        print(f'\n{__file__}')
        print(table)