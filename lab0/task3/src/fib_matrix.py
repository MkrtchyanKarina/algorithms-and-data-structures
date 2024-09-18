import psutil
import time

t_start = time.perf_counter()

K = [[0, 1], [1, 1]]


def fast_multiply(x, n, m):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n % 2 == 0:
        y = fast_multiply(x, n / 2, m)
        return matrix_multiply_2x2(y, y, m)
    else:
        y = fast_multiply(x, (n - 1) / 2, m)
        y2 = matrix_multiply_2x2(y, y, m)
        return matrix_multiply_2x2(y2, x, m)


def matrix_multiply_2x2(A, B, m):
    C = [[0, 0], [0, 0]]
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % m
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % m
    return C


open("output.txt", "w").write(str(fast_multiply(K, int(open("input.txt").readline()), m=10)[0][1]))
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
