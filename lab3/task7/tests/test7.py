import string
import unittest
import psutil
import time
from random import *
from prettytable import PrettyTable

table = PrettyTable()
#
table.field_names = [' ', "данные", "время", "память"]
#
# print(table)
from lab3.task7.src.task7 import *

def create_array(n: int, m: int):
    alf = string.ascii_lowercase
    strings = [''.join([choice(alf) for j in range(m)]) for i in range(n)]
    return strings


def check(n, m, k, strings):
    strings = reformat(n, strings)
    for ind in range(m - 1, m - k - 1, -1):
        strings = sorted(strings, key=lambda x: x[1][ind])
    return [s[0] for s in strings]


class MergeSortTest(unittest.TestCase):

    def test_merge_sort1(self):
        n = 1000
        m = 400
        k = 30
        strings = create_array(n, m)
        t_start = time.time()
        self.assertEqual(strings_sort(n, m, k, strings), check(n, m, k, strings))
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        table.add_row(["Минимальные данные", f'{n} {m} {k}\n{' '.join(x[:3] for x in strings[:3])}', f'{t_end} секунд', f'{memory} МБ'])
        print(table)

