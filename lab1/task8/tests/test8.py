import psutil
import time
import random
from lab1.task8.src.task8 import swap

t_start = time.perf_counter()
test_max_m = [random.randint(-10**9, 10**9) for i in range(5000)]
swap(5000, test_max_m)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
