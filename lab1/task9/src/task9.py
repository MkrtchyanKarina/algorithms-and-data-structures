import random


n = 10**3
a = [round(random.random()) for i in range(n)]
b = [round(random.random()) for j in range(n)]
res_main = int("".join(str(i) for i in a), 2) + int("".join(str(i) for i in b), 2)
def sum_dv(a, b, n):
    c = [int(i) for i in "0"*(n+1)]
    for i in range(1, n+1):

        s = a[-i] + b[-i] + c[-i]

        c[-i - 1] = s // 2
        c[-i] = s % 2

    return c
res = sum_dv(a, b, n)
print(int("".join(str(i) for i in res), 2) == res_main)
print(res)