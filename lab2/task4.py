def binary_search(m, x, start, end):
    middle = (end + start) // 2
    if end - start == 1 and m[middle] != x:
        return -1
    elif m[middle] == x:
        return middle
    elif m[middle] < x:
        start = middle
        return binary_search(m, x, start, end)
    elif m[middle] > x:
        end = middle
        return binary_search(m, x, start, end)


print(binary_search([2, 3, 4], 2, 0, 3))