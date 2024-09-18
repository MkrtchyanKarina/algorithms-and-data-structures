def sum_ab2(s, n):
    if n == 2:
        print("Числа не удовлетворяют ограничению!")
    else:
        a, b = map(int, list(s.split()))
        if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= a <= 10 ** 9:
            return a + b ** 2
        else:
            print("Введите числа ещё раз: ")
            sum_ab2(input(), n + 1)


# print(sum_ab2(input(), 0))