
def qsort(array, left, right):
    pivot = array[(left + right) // 2]
    print(array, pivot)
    i = left
    j = right
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if left < j:
        qsort(array, left, j)
    if i < right:
        qsort(array, i, right)


def worst_case(n):
    worst_arr = [i + 1 for i in range(n)]
    for i in range(2, len(worst_arr)):
        worst_arr[i], worst_arr[i // 2] = worst_arr[i // 2], worst_arr[i]
    return worst_arr


print(worst_case(19))

