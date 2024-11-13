from lab3.task9.src.task9 import *
import time
import psutil
import unittest
from random import randint
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1


class ShortestDistanceTest(unittest.TestCase):
    def test_shortest_distance0(self):
        global table
        n = 1
        array = [(7, 7)]
        m = [Dot(x, y) for x, y in array]
        t_start = time.time()
        result = shortest_distance(n, m)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, slow_shortest_distance(n, m))
        table.add_row(["Минимальные значения", f'{n}\n{" ".join(map(str, array))}', t_end, memory,result])

    def test_shortest_distance1(self):
        global table
        n = 4
        array = [(7, 7), (1, 100), (4, 8), (7, 7)]
        m = [Dot(x, y) for x, y in array]
        t_start = time.time()
        result = shortest_distance(n, m)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, slow_shortest_distance(n, m))
        table.add_row(["Значения из примера", f'{n}\n{" ".join(map(str, array))}', t_end, memory,result])

    def test_shortest_distance2(self):
        global table
        n = 2
        array = [(0, 0), (3, 4)]
        m = [Dot(x, y) for x, y in array]
        t_start = time.time()
        result = shortest_distance(n, m)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        self.assertEqual(result, slow_shortest_distance(n, m))
        table.add_row(["Значения из примера", f'{n}\n{" ".join(map(str, array))}', t_end, memory,result])

    def test_shortest_distance3(self):
        global table
        n = 10**5
        start, end = -10**9, 10**9
        array = [(randint(start, end), randint(start, end)) for i in range(n)]
        m = [Dot(x, y) for x, y in array]
        t_start = time.time()
        result = shortest_distance(n, m)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        table.add_row(["Максимальные значения", f'{n}\n{" ".join(map(str, array[:2]))}...', t_end, memory,result])
        print(f'\n{__file__}')
        print(table)
