import random

from lab1.src.verifications import data_verification9

n = 10**3
a = "".join(map(str, [round(random.random()) for i in range(n)]))
b = "".join(map(str, [round(random.random()) for j in range(n)]))
res_main = int(a, 2) + int(b, 2)

@data_verification9
def sum_dv(a, b):
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    n = len(a)
    c = [int(i) for i in "0"*(n+1)]
    for i in range(1, n+1):

        s = a[-i] + b[-i] + c[-i]

        c[-i - 1] = s // 2
        c[-i] = s % 2

    return "".join(map(str, c))
res = sum_dv(a, b)
print(int(res, 2) == res_main)
print(res)