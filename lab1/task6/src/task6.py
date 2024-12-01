from lab1.src.verifications import data_verification1


@data_verification1
def bubble_sort(n, m):
    for i in range(n):
        # print(strings[index], strings)
        for j in range(0, n-i-1):

            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
    return m


file = open("input6.txt")
test_n = int(file.readline())
test_m = list(map(int, file.readline().split(" ")))
open("output6.txt", "w").write(" ".join(map(str, bubble_sort(test_n, test_m))))


