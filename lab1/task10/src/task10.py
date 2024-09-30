from lab1.src.verifications import data_verification10


def merge_sort(string):
    n = len(string)
    m = n // 2
    arr1 = string[:m]
    arr2 = string[m:]
    n1, n2 = m, n-m
    if n1 > 1:
        arr1 = merge_sort(arr1)
    if n2 > 1:
        arr2 = merge_sort(arr2)
    return merge_list(arr1, arr2, n1, n2)


def merge_list(arr1, arr2, n1, n2):
    res_str = ""
    i1, i2 = 0, 0
    while i1 < n1 and i2 < n2:
        if arr1[i1] >= arr2[i2]:
            res_str += arr1[i1]
            i1 += 1
        else:
            res_str += arr2[i2]
            i2 += 1
    res_str += arr1[i1:] + arr2[i2:]
    return res_str


@data_verification10
def palindrome(n: int, s: str, index=0):
    s = merge_sort(s)
    count1 = ""
    count2 = ""
    while index < n:
        k = s[index]
        count = 1
        index += 1
        while index < n:
            if s[index] == k:
                count += 1
                index += 1
            else:
                break
        count1 = k * (count % 2) + count1
        count2 += k * (count // 2) * 2
    return palindrome2(count1, count2)


def palindrome2(count1, count2):
    if len(count1) > 0:
        res_str = count1[0]
    else:
        res_str = ""
    pairs_count = len(count2)
    for i in range(0, pairs_count, 2):
        res_str = count2[i] + res_str + count2[i+1]
    return res_str


# file = open("input10.txt")
# test_n = int(file.readline())
# test_s = file.readline()
# open("output10.txt", "w").write(palindrome(test_n, test_s))


