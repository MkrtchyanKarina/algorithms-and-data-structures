import unittest
import psutil
import time
from random import *
from prettytable import PrettyTable
from lab3.task5.src.task5 import *
from scholarmetrics import hindex

table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1


class HIndexTest(unittest.TestCase):
    def test_str_sort0(self):
        global table
        n = 1
        start = 2
        end = 19
        citations = [randint(start, end) for i in range(n)]
        t_start = time.time()
        result = h_index(citations)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, hindex(citations))
        table.add_row(["Минимальные значения", f'{' '.join(map(str, citations))}', t_end, memory,result])

    def test_str_sort1(self):
        global table
        citations = [1, 3, 1]
        t_start = time.time()
        result = h_index(citations)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, hindex(citations))
        table.add_row(["Значения из примера", f'{' '.join(map(str, citations))}', t_end, memory,result])

    def test_str_sort2(self):
        global table
        citations = [3, 0, 6, 1, 5]
        t_start = time.time()
        result = h_index(citations)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, hindex(citations))
        table.add_row(["Значения из примера", f'{' '.join(map(str, citations))}', t_end, memory,result])

    def test_str_sort3(self):
        global table
        n = 1000
        start = 1
        end = 5000
        citations = [randint(start, end) for i in range(n)]
        t_start = time.time()
        result = h_index(citations)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, hindex(citations))
        table.add_row(["Максимальные значения", f'{' '.join(map(str, citations[:4]))}...', t_end, memory,result])
        print(f'\n{__file__}')
        print(table)