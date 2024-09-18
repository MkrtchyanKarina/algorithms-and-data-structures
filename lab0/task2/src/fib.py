def fib_number(n):
    if 0 <= n <= 45:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


# file_input = open("input.txt")
# file_output = open("output.txt", "w")
# n = int(file_input.readline())
# file_output.write(str(fib_number(n)))
