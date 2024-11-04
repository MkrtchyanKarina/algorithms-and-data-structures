from lab1.src.verifications import data_verification9


@data_verification9
def sum_dv(a, b):
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    n = len(a)
    c = [int(i) for i in "0"*(n+1)]
    for i in range(1, n+1):

        s = a[-i] + b[-i] + c[-i]

        c[-i - 1] = s // 2
        c[-i] = s % 2
    result = "".join(map(str, c))
    result = result[result.index("1"):]
    return result

# array, b = open('input9.txt').readline().split(" ")
# file_output = open('output9.txt', 'w')
# file_output.write(sum_dv(array, b))
