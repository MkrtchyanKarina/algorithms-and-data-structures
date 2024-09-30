from lab1.src.verifications import data_verification7
import sys
sys.setrecursionlimit(10**8)

@data_verification7
def sort_land(n, M):
    M = [[M[i], i+1] for i in range(n)]
    sorted_M = merge_sort(M)
    return sorted_M[0][1], sorted_M[n//2][1], sorted_M[-1][1]



def merge_sort(arr):
    n = len(arr)
    m = n // 2
    arr1 = arr[:m]
    arr2 = arr[m:]
    n1, n2 = m, n-m
    if n1 > 1:
        arr1 = merge_sort(arr1)
    if n2 > 1:
        arr2 = merge_sort(arr2)
    return merge_list(arr1, arr2, n1, n2)


def merge_list(arr1, arr2, n1, n2):
    res_arr = []
    i1, i2 = 0, 0
    while i1 < n1 and i2 < n2:
        if arr1[i1] <= arr2[i2]:
            res_arr.append(arr1[i1])
            i1 += 1
        else:
            res_arr.append(arr2[i2])
            i2 += 1
    res_arr += arr1[i1:] + arr2[i2:]
    return res_arr


# input_file = open('input7.txt')
# output_file = open('output7.txt', 'w')
# n = int(input_file.readline().strip())
# M = [float(i) for i in input_file.readline().strip().split()]
# output_file.write(" ".join(map(str, sort_land(n, M))))
