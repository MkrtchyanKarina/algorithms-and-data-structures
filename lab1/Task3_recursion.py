import random, time, psutil

t_start = time.perf_counter()


def swap(a, b):
    c = b
    b = a
    a = c
    return a, b


def insertion_sort(n, m, index=1):
    if index == n:
        return m
    else:
        for j in range(index - 1, -1, -1):
            if m[index] < m[j]:
                m[index], m[j] = swap(m[index], m[j])
                index, j = j, index
        return insertion_sort(n, m, index + 1)


print(insertion_sort(6, [31, 41, 59, 26, 41, 58]))

try:
    test_max_m = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]
    max_result = insertion_sort(10 ** 3, test_max_m)
    if max_result == sorted(test_max_m):
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
        print(" ".join(map(str, max_result)))
except RecursionError:
    print("Stack overflow")
