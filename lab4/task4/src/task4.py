from lab4.src.utils import File


def bracket_sequence(brackets):
    bracket_pairs = {')': '(',
                     '}': '{',
                     ']': '['}
    if len(brackets) == 1:
        symbol = brackets[0]
        if symbol in bracket_pairs.keys() or symbol in bracket_pairs.values():
            return "1"
        else:
            return "Success"
    else:
        stack = ""
        err_ind = 1
        for b in brackets:
            if b in bracket_pairs.values():
                stack += b
            elif b in bracket_pairs.keys():
                if bracket_pairs[b] == stack[-1]:
                    stack = stack[:-1]
                else:
                    return err_ind
            else:
                pass
            err_ind += 1
    return "Success"

print(bracket_sequence("{"))





# def limits(high: int, k: int, array: list[int]) -> bool:
#     if 1 <= k < high <= 10**5 and all(abs(x) <= 10**9 for x in array):
#         return True
#     else:
#         return False
#
#
# def scarecrow_sort_txt():
#     f = File(__file__)
#     data = f.read()
#     high, k = list(map(int, data[0].split(" ")))
#     array = list(map(int, data[1].split(" ")))
#     if limits(high, k, array):
#         f.write(scarecrow_sort(high, k, array))
#
#
# if __name__ == "__main__":
#     scarecrow_sort_txt()