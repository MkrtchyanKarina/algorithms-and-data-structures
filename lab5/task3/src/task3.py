from lab4.src.utils import File



def pack(buffer_size, packages_count, packages):
    deque = []
    head = 0
    buffer_time = packages[0][0]
    for p in packages:
        start_time, duration = p
        head = max([head] + [index for index in range(len(deque)) if deque[index] <= start_time])
        if len(deque[head+1:]) < buffer_size:
            print(max(buffer_time, start_time))
            buffer_time += duration
            deque.append(buffer_time)
        else:
            print(-1)





pack(3, 6 ,[(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])
print()
pack(2, 3, [(0, 1), (3, 1), (10, 1)])
print()
pack(1, 2, [(0, 1), (2, 1)])
# def limits(n: int) -> bool:
#     if 1 <= n <= 10**6:
#         return True
#     else:
#         return False
#
#
# def worst_case_txt():
#     f = File(__file__)
#     arguments = f.read()
#     n = int(arguments[0])
#
#     if limits(n):
#         res = " ".join(map(str, worst_case(n)))
#         f.write(res)
#
#
#
# if __name__ == "__main__":
#     worst_case_txt()