import sys
sys.setrecursionlimit(10**8)


def swap(a, b):
    c = b
    b = a
    a = c
    return a, b


def insertion_sort_rec(n, m, index=1):
    if index == n:
        return m
    else:
        for j in range(index - 1, -1, -1):
            if m[index] > m[j]:
                m[index], m[j] = swap(m[index], m[j])
                index, j = j, index
        return insertion_sort_rec(n, m, index + 1)


# file = open("input_rec3.txt")
# test_n = int(file.readline())
# test_m = list(map(int, file.readline().split(" ")))
# open("output_rec3.txt", "w").write(" ".join(map(str, insertion_sort_rec(test_n, test_m))))

