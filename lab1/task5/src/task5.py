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
print(selection_sort(6, [31, 41, 59, 26, 41, 58]))