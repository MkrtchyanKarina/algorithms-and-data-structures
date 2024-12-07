def last_digit(n):
    if 0 <= n <= 10 ** 7:
        a, b = 0, 1
        for i in range(n):
            a, b = b % 10, (a + b) % 10
        return a


# file_input = open("input.txt")
# file_output = open("output.txt", "w")
# high = int(file_input.readline())
# file_output.write(str(last_digit(high)))
