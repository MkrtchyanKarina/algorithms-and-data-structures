import random

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


def palindrome(n, s):
    s = merge_sort(s)
    count1 = ""
    count2 = ""
    for i in range(n):
        k = s[i]
        if k not in count2 and k not in count1:
            rep = 0
            for j in range(i+1, n):
                if s[j] == k:
                    count2 += s[j]
                    rep += 1
            if rep % 2 == 0:
                count1 += k
            else:
                count2 += k

    return palindrome2(count1, count2)

def palindrome2(count1, count2):
    res_str = ""
    n = len(count2)
    if n != 0:
        for i in range(0, n, 2):
            res_str = count2[i] + res_str + count2[i+1]
        if len(count1) != 0:
            return res_str[:n//2] + count1[0] + res_str[n//2:]
        else:
            return res_str
    else:
        return count1[0]

str_test = "".join(chr(random.randint(65, 91)) for i in range(10**5 + 1))
print(palindrome(10**5, str_test))

