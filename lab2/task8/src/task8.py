from math import log2, ceil


def verification(n, A, B, attempt=1):
    res = 1
    if type(n) is int and n > 0 and type(A) is list and type(B) is list:
        if len(A) == len(B) == n:
            pass
        else:
            res *= 0
    else:
        res *= 0
    if res == 0:
        if attempt == 3:
            return 'Ошибка!'
        else:
            print("Введите данные ещё раз, соблюдая ограничения: ")
            try:
                new_n = int(input())
                new_A = list(map(int, input().split(" ")))
                new_B = list(map(int, input().split(" ")))
                return verification(new_n, new_A, new_B, attempt + 1)
            except:
                return 'Ошибка!'
    else:
        return res


def karatsuba_polynomial_multiply(*args):
    if len(args) == 1:
        path = args[0]
        file_input = open(path, 'r')
        n = int(file_input.readline())
        A = list(map(int, file_input.readline().strip().split()))
        B = list(map(int, file_input.readline().strip().split()))
        if verification(n, A, B):
            file_output = open('output' + path[5:], 'w')
            file_output.write(reformat(multiply(power_of_two(A), power_of_two(B))))
    else:
        n, A, B = args
        if verification(n, A, B):
            return reformat(multiply(power_of_two(A), power_of_two(B)))


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
    third_product = multiply([a[i] + b[i] for i in range(mid)], [c[i] + d[i] for i in range(mid)])

    middle = [third_product[i] - ac[i] - bd[i] for i in range(len(third_product))]
    result = []

    n = []
    i = 3
    while i <= len(ac):
        n.append(i)
        i = 2*i + 1
    if len(ac) in n:
        result += union(ac, middle, bd)
        return result
    else:
        return ac + middle + bd


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




# karatsuba_polynomial_multiply_main('input8.txt')
# print(karatsuba_polynomial_multiply(30, [7, 1, 7, 2, 3, 4, -2, 2, 1, 2, 1, 3, 4, 5, 2, 1, 4, -2, 5, -2, 1, 3, 3, 2, 3, 4, 4, 5, -2, -1], [1, 4, -2, 5, -2, 1, 3, 3, 2, 3, 4, 4, 5, -2, -1, 7, 1, 7, 2, 3, 4, -2, 2, 1, 2, 1, 3, 4, 5, 2]))
