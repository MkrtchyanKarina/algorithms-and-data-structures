from random import shuffle, randint


def scarecrow_sort(n: int, k: int, array: list) -> str:
    for i in range(k):
        for j in range(i+k, n, k):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    if all(array[i] <= array[i+1] for i in range(n-1)):
        return "ДА"
    else:
        return "НЕТ"


l = [1, 5, 3, 4, 1]
print(scarecrow_sort(5, 3, l))


l = [1, 5, 3, 4, 1, 7, 6, 8, 2]
print(scarecrow_sort(9, 4, l))

l = [randint(-10**9, 10**9) for i in range(10**5)]
print(scarecrow_sort(10**5, 10**3, l))