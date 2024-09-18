import time
import psutil

t_start = time.perf_counter()


def last_digit(path1, path2):
    file = open(path1)
    n = int(file.readline())
    if 0 <= n <= 10 ** 7:
        a, b = 0, 1
        for i in range(n):
            a, b = b % 10, (a + b) % 10
        open(path2, "w").write(str(a))


last_digit("input.txt", "output.txt")
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")