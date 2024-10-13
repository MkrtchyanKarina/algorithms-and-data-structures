from math import log2, ceil


def union(a, b, c):
    n = len(a) // 2
    return a[:-n] + [a[-n + i] + b[i] for i in range(n)] + b[n:-n] + [b[-n + i] + c[i] for i in range(n)] + c[n:]


def power_of_two(m):
    n = len(m)
    return [0] * (2 ** ceil(log2(n)) - n) + m


def reformat(x):
    for i in range(len(x)):
        if x[i] != 0:
            return " ".join(map(str, x[i:]))


def multiply(poly1, poly2):

    n = len(poly1)
    if n == 1:
        return [poly1[0] * poly2[0]]

    mid = n // 2
    a = poly1[:mid]
    b = poly1[mid:]
    c = poly2[:mid]
    d = poly2[mid:]

    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_plus_bc = multiply([a[i] + b[i] for i in range(mid)], [c[i] + d[i] for i in range(mid)])

    result = [ad_plus_bc[i] - ac[i] - bd[i] for i in range(len(ad_plus_bc))]
    result2 = []

    n = []
    i = 3
    while i <= len(ac):
        n.append(i)
        i = 2*i + 1
    if len(ac) in n:
        result2 += union(ac, result, bd)
        return result2
    else:
        return ac + result + bd


def karatsuba_polynomial_multiply(x, y):
    return reformat(multiply(power_of_two(x), power_of_two(y)))


print(karatsuba_polynomial_multiply([7, 1, 7, 2, 3, 4, -2, 2, 1, 2, 1, 3, 4, 5, 2, 1, 4, -2, 5, -2, 1, 3, 3, 2, 3, 4, 4, 5, -2, -1], [1, 4, -2, 5, -2, 1, 3, 3, 2, 3, 4, 4, 5, -2, -1, 7, 1, 7, 2, 3, 4, -2, 2, 1, 2, 1, 3, 4, 5, 2]))
