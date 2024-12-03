from lab1.src.verifications import data_verification1


@data_verification1
def selection_sort(n, m):
    for i in range(n):
        a = m[i]
        index = i
        for j in range(i+1, n):
            if m[j] <= a:
                a = min(a, m[j])
                index = j
        m.pop(index)
        m.insert(i, a)
    return m


# file = open("input4.txt")
# test_n = int(file.readline())
# test_m = list(map(int, file.readline().split(" ")))
# open("output5.txt", "w").write(" ".join(map(str, selection_sort(test_n, test_m))))