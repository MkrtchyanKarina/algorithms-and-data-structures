def fib_number(n):
    return fast_multiply([[0, 1], [1, 1]], n)[0][1]
def fast_multiply(x, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n % 2 == 0:
        y = fast_multiply(x, n / 2)
        return matrix_multiply_2x2(y, y)
    else:
        y = fast_multiply(x, (n - 1) / 2)
        y2 = matrix_multiply_2x2(y, y)
        return matrix_multiply_2x2(y2, x)


def matrix_multiply_2x2(A, B):
    C = [[0, 0], [0, 0]]
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0])
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0])
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1])
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1])
    return C


# file_input = open("input.txt")
# file_output = open("output.txt", "w")
# high = int(file_input.readline())
# file_output.write(str(fib_number(high)))
