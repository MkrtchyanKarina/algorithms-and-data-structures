from lab0.src.utils import File

def fib_number(n: int) -> int:
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


def limits(number: int) -> bool:
    if 0 <= number <= 10**7:
        return True
    else:
        return False


def addition_sqrt_txt():
    f = File(__file__)
    arguments = f.read()
    number = int(arguments[0])
    if limits(number):
        res = str(fib_number(number))
        f.write(res)


if __name__ == "__main__":
    addition_sqrt_txt()

