def merge_sort(len_arr, array):
    middle = len_arr // 2
    list_a, list_b = array[:middle], array[middle:]
    len_a, len_b = middle, len_arr - middle
    if len_a > 1:
        list_a = merge_sort(len_a, list_a)
    if len_b > 1:
        list_b = merge_sort(len_b, list_b)
    return merge(middle, len_arr - middle, list_a, list_b)


def merge(len_a, len_b, array_a, array_b):
    len_c = len_a + len_b
    array_c = [0] * len_c
    index_a, index_b = 0, 0
    for index_c in range(len_c):
        if index_b >= len_b:
            array_c[index_c] = array_a[index_a]
            index_a += 1
        elif index_a >= len_a:
            array_c[index_c] = array_b[index_b]
            index_b += 1
        else:
            if array_a[index_a] <= array_b[index_b]:
                array_c[index_c] = array_a[index_a]
                index_a += 1
            else:
                array_c[index_c] = array_b[index_b]
                index_b += 1
    return array_c



print(merge_sort(5, [7, 6, 8, 2, 4]))
