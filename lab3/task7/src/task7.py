import time

import psutil

from lab3.src.utils import *
import typing as tp


def time_memory(function):
    def check(n: int, m: int, k: int, strings: tp.List[str]):
        start = time.time()
        function(n, m, k, strings)
        print("Время работы: %s секунд" % (time.time() - start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
    return check

def strings_sort_txt():
    arguments = read_txt(task_number=7)
    n, m, k = list(map(int, arguments[0].split()))
    strings = []
    for s in range(n):
        strings.append(arguments[s+1])
    res = ' '.join(map(str, strings_sort(n, m, k, strings)))
    write_txt(task_number=7, result=res)


def radix_sort(k: int, strings: tp.List[tp.List[str]]):
    alf = {i:[] for i in range(97, 123)}
    for s in strings:
        alf[ord(s[1][k])] += [s]
    return sum(alf.values(), [])

def reformat(n, strings):
    strings_indexes = []
    for s in range(n):
        strings_indexes.append([s+1, strings[s]])
    return strings_indexes


def strings_sort(n: int, m: int, k: int, strings: tp.List[str]):
    strings = reformat(n, strings)
    for ind in range(m-1, m-k-1, -1):
        strings = radix_sort(ind, strings)
    return [s[0] for s in strings]


if __name__ == "__main__":
    strings_sort_txt()