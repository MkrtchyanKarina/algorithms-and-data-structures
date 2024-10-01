from lab1.src.verifications import data_verification1


def swap(a, b):
    c = b
    b = a
    a = c
    return a, b


@data_verification1
def insertion_sort(n, m):
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if m[i] > m[j]:
                m[i], m[j] = swap(m[i], m[j])
                i, j = j, i
    return m


# file = open("input3.txt")
# test_n = int(file.readline())
# test_m = list(map(int, file.readline().split(" ")))
# open("output3.txt", "w").write(" ".join(map(str, insertion_sort(test_n, test_m))))
