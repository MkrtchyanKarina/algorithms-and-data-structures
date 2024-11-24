from lab4.src.utils import File


def queue_actions(actions: list[str]):
    queue = []
    minim = []  # для хранения минимума используем структуру данных "дек"
    answers = []
    for a in actions:
        if a == "?":
            answers += [minim[0]]
        elif a == "-":
            deleted_elem = queue.pop(0)
            if deleted_elem == minim[0]:
                minim.pop(0)
        else:
            elem = int(a[1:])
            if len(minim) > 0:
                while minim[-1] > elem:
                    minim.pop(-1)
            minim += [elem]
            queue += [elem]
    return "\n".join(map(str, answers))
s = ['+ 1', '?', '+ 10', '?', '-', '?', '-']
print(queue_actions(s))




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