from lab4.src.utils import File


def queue_actions(actions: list[str]):
    queue = []
    head = 0
    deleted_elements = []
    for a in actions:
        if a == "-":
            deleted_elements += [queue[head]]
            head += 1
        else:
            elem = int(a[1:])
            queue += [elem]
    return deleted_elements
s = ['+ 1', '+ 10', '-', '-', '+ -3', '+ 4', '-']
print(queue_actions(s))



# def limits(high: int) -> bool:
#     if 1 <= high <= 10**6:
#         return True
#     else:
#         return False
#
#
# def worst_case_txt():
#     f = File(__file__)
#     arguments = f.read()
#     high = int(arguments[0])
#
#     if limits(high):
#         res = " ".join(map(str, worst_case(high)))
#         f.write(res)
#
#
#
# if __name__ == "__main__":
#     worst_case_txt()