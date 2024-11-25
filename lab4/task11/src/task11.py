from lab4.src.utils import File
import typing as tp



def bureaucracy(n:int, m:int, queue:list[int]):
    deque = queue.copy()
    head = 0
    end = n
    while m > 0:
        deque[head] -= 1
        m -= 1
        if deque[head] > 0:
            deque += [deque[head]]
            end += 1
        head += 1

    return end - head, deque[head:end]
print(bureaucracy(3, 2, [1, 2, 3]))
print(bureaucracy(4, 5, [2, 5, 2, 3]))


# def limits(n: int, k: int, array: list[int]) -> bool:
#     if 1 <= k < n <= 10**5 and all(abs(x) <= 10**9 for x in array):
#         return True
#     else:
#         return False
#
#
# def scarecrow_sort_txt():
#     f = File(__file__)
#     data = f.read()
#     n, k = list(map(int, data[0].split(" ")))
#     array = list(map(int, data[1].split(" ")))
#     if limits(n, k, array):
#         f.write(scarecrow_sort(n, k, array))
#
#
# if __name__ == "__main__":
#     scarecrow_sort_txt()