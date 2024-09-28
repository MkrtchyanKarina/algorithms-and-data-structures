from lab1.src.verifications import data_verification1


@data_verification1
def insertion_sort(n, m):
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if m[i] < m[j]:
                m[i], m[j] = m[j], m[i]
                i, j = j, i
    return m

print(insertion_sort(10**8, []))
# file = open("input1.txt")
# test_n = int(file.readline())
# test_m = list(map(int, file.readline().split(" ")))
# open("output1.txt", "w").write(" ".join(map(str, insertion_sort(test_n, test_m))))