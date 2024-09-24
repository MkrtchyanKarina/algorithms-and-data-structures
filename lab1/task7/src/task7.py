# input_file = open('input7.txt')
# output_file = open('output7.txt', 'w')
# n = int(input_file.readline().strip())
# M = []
# j = 1
# for i in input_file.readline().strip().split():
#     M.append([float(i), j])
#     j += 1
import random, time
def sort_land(n, M):
    sorted_M = merge_sort(M)
    return sorted_M[0][1], sorted_M[n//2][1], sorted_M[-1][1]
import sys
sys.setrecursionlimit(10**8)


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


n = 9999
M = [[round(random.random(), 2) + random.randint(-10**6, 10**6), i] for i in range(n)]
print(M)
start = time.time()
print(*sort_land(n, M), sep=" ")
print(time.time() - start)
M = sorted(M)
print(M[0][1], M[n//2][1], M[-1][1])