C = [0] * 9
A = [2, -1, 4, 3, -5]
B = [1, -7, 2, 1, -3]
def multiply(ind_a, ind_b):

    global A, B, C
    if ind_b is None:
        a, b = ind_a
        c, d = ind_a
        C[a + c] += A[a] * B[c]
        C[b + d] += A[b] * B[d]
        C[a + d] += A[a] * B[d] + A[b] * B[c]
    else:
        if len(ind_a) == 2:
            a, b = ind_a
            c, d = ind_a
            C[a + c] += A[a] * B[c]
            C[b + d] += A[b] * B[d]
            C[a + d] += A[a] * B[d] + A[b] * B[c]

            a, b = ind_a
            c, d = ind_b
            C[a + c] += A[a] * B[c]
            C[b + d] += A[b] * B[d]
            C[a + d] += A[a] * B[d] + A[b] * B[c]

            a, b = ind_b
            c, d = ind_a
            C[a + c] += A[a] * B[c]
            C[b + d] += A[b] * B[d]
            C[a + d] += A[a] * B[d] + A[b] * B[c]

        else:
            a = b = ind_a[0]
            C[a + b] += A[a] * B[b]

            a = ind_a[0]
            c, d = ind_b
            C[a + c] += A[a] * B[c]
            C[a + d] += A[a] * B[d]

            a = ind_a[0]
            c, d = ind_b
            C[a + c] += A[c] * B[a]
            C[a + d] += A[d] * B[a]


        a, b = ind_b
        c, d = ind_b
        C[a + c] += A[a] * B[c]
        C[b + d] += A[b] * B[d]
        C[a + d] += A[a] * B[d] + A[b] * B[c]



    print(C)


def merge_sort(len_arr, array):

    middle = len_arr // 2
    list_a, list_b = array[:middle], array[middle:]

    len_a, len_b = middle, len_arr - middle
    if len_a > 2:
        list_a =  merge_sort(len_a, list_a)
    if len_b > 2:
        list_b =  merge_sort(len_b, list_b)
    print(list_a, list_b)
    multiply(list_a, list_b)









merge_sort(5, [4, 3, 2, 1, 0])
