from lab4.src.utils import File
import typing as tp



def calc(a: int, b: int, action: str) -> int:
    if action == "+":
        return a + b
    elif action == "*":
        return a * b
    elif action == "-":
        return a - b
    elif action == "/":
        return int(a//b)
    else:
        return 0


def equal(expression: str) -> tp.Union[int, str]:
    expression = expression.split(" ")
    if 1 < len(expression) < 3:
        return int(expression[0])
    stack = []
    for e in expression:
        if e.isnumeric():
            stack += [int(e)]
        else:
            stack[-2] = calc(stack[-2], stack[-1], e)
            stack.pop()
    if len(stack) == 1:
        return stack[0]
    else:
        return "error"




print(equal("8 9 + 1 7 - *"))
print(equal("5 15 + 4 7 + 1 - /"))
print(equal("5 15 + 4 7 + 1 -"))


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