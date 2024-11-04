import string
import time
from random import randint, choice

import psutil


def radix_sort(n, m, k, strings):
    alf = {i:[] for i in range(97, 123)}
    for s in strings:
        alf[ord(s[1][k])] += [s]
    return sum(alf.values(), [])

def strings_sort(n, m, k, strings):
    for ind in range(m-1, m-k-1, -1):
        strings = radix_sort(n, m, ind, strings)
    return [s[0] for s in strings]

# strings = [[1,'bbb'], [2,'aba'], [3,'baa']]
# n = 3
# m = 3
# k = 3
# print(strings_sort(m, n, k, strings))


n = 10**4
m = 5*10**7 // n
k = m
alf = string.ascii_lowercase
strings = [[] for i in range(n)]

for i in range(n):
    s = ''.join([choice(alf) for j in range(m)])
    strings[i] = [i+1, s]

start = time.time()
strings_sort(n, m, k, strings)
print("Время работы: %s секунд" % (time.time() - start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")