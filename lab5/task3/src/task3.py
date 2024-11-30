from lab4.src.utils import File



def net_packet_processing(buffer_size, packages_count, packages):
    if packages_count == 0:
        return None
    deque = []
    result = []
    head = 0
    buffer_time = packages[0][0]
    for p in packages:
        start_time, duration = p
        head = max([head] + [index for index in range(len(deque)) if deque[index] <= start_time])
        if len(deque[head+1:]) < buffer_size:
            result += [max(buffer_time, start_time)]
            buffer_time += duration
            deque.append(buffer_time)
        else:
            result += [-1]
    # print(result)
    return result





net_packet_processing(1, 1, [(0, 0)])


def limits(buffer_size, packages_count, packages) -> bool:
    if (1 <= buffer_size <= 10**5) and (1 <= packages_count <= 10**5) and all(0 <= a <= 10**6 and 0 <= p <= 10**3 for a, p in packages):
        return True
    else:
        return False
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