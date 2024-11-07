import string
import unittest
import psutil
import time
from random import *
from prettytable import PrettyTable
from lab3.task7.src.task7 import *
import typing as tp


def create_array(n: int, m: int):
    alf = string.ascii_lowercase
    strings = [''.join([choice(alf) for j in range(m)]) for i in range(n)]
    return strings


def check(n, m, k, strings):
    strings = reformat(n, strings)
    for ind in range(m - 1, m - k - 1, -1):
        strings = sorted(strings, key=lambda x: x[1][ind])
    return [s[0] for s in strings]


def arr_to_str(arr):
    return ' '.join(str(x) for x in arr[:3])

table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1

class MergeSortTest(unittest.TestCase):

    def test_str_sort0(self):
        global table
        n = 1
        m = 1
        k = 1
        strings = create_array(n, m)
        t_start = time.time()
        result = strings_sort(n, m, k, strings)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        self.assertEqual(result, check(n, m, k, strings))

        table.add_row(["Минимальные данные", f'{n} {m} {k}\n{arr_to_str(strings)}', t_end, memory, arr_to_str(result)])


    def test_str_sort1(self):
        global table
        n = 3
        m = 3
        k = 2
        strings = ['bbb', 'aba', 'baa']
        t_start = time.time()
        result = strings_sort(n, m, k, strings)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        self.assertEqual(result, check(n, m, k, strings))

        table.add_row(["Данные из примера", f'{n} {m} {k}\n{arr_to_str(strings)}', t_end, memory, arr_to_str(result)])


    def test_str_sort2(self):
        n = 5*10**3
        m = 10**4
        k = 1000
        strings = create_array(n, m)
        t_start = time.time()
        result = strings_sort(n, m, k, strings)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        self.assertEqual(result, check(n, m, k, strings))


        table.add_row(["Данные из примера", f'{n} {m} {k}\n{arr_to_str([x[:3] for x in strings[:3]])}', t_end, memory, arr_to_str(result)])
        print()
        print(table)
