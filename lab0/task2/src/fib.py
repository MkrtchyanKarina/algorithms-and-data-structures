import psutil
import time

t_start = time.perf_counter()


def fib_number(path1, path2):
    file = open(path1)
    n = int(file.readline())
    if 0 <= n <= 45:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        open(path2, "w").write(str(a))


fib_number("input.txt", "output.txt")
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")