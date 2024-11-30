import unittest
import psutil
import time
from prettytable import PrettyTable
from lab4.task2.src.task2 import *
import random
table = PrettyTable()
table.field_names = [' ', "данные", "время, сек.", "память, МБ", "результат"]
table.hrules = 1


class ScarecrowSortTest(unittest.TestCase):
    def test_worst_case0(self):
        global table
        n = 10**4
        array = ["+ 2", "+ 9"]
        for i in range(n-2):
            if random.randint(0, 1) or array.count("-") > len(array)//3:
                array += ["+ " + str(random.randint(-10**9, 10**9))]
            else:
                array += ["-"]
        t_start = time.time()
        result = queue_actions(array)
        t_end = round(time.time() - t_start, 2)
        memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
        table.add_row(["Минимальные значения", n, t_end, memory," ".join(map(str, result[:2]))])

        print(table)
