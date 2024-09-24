import psutil
import time
import random

t_start = time.perf_counter()


def insertion_sort(n, m):
    new_m = []
    indexes = [1]
    for k in range(1, n):
        new_m.append(m[k])
        i = k
        for j in range(i, -1, -1):
            if m[i] < m[j]:
                m[i], m[j] = m[j], m[i]
                i, j = j, i
        indexes.append(i+1)
    return indexes, m

# print(sort_v(10, [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]))
test_max_m = [random.randint(-10**9, 10**9) for i in range(10**3)]
max_result = insertion_sort(10 ** 3, test_max_m)
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
print(" ".join(map(str, max_result)))



file_input = open("input2.txt")
file_output = open("output2.txt", "w")

test_n = int(file_input.readline())
test_m = list(map(int, file_input.readline().split(" ")))

res_ind, res_m = insertion_sort(test_n, test_m)

file_output.write(" ".join(map(str, res_ind)))
file_output.write("\n")
file_output.write(" ".join(map(str, res_m)))