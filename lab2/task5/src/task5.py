indexes = [0] * (10**9 + 1)


def max_count(n, array):
    res = 0
    for i in array:
        indexes[i] += 1
        if indexes[i] >= n // 2:
            res += 1
            break
    return res

