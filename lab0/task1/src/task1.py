def sum_ab(s, n):
    if n == 2:
        print("Числа не удовлетворяют ограничению!")
    else:
        a, b = map(int, list(s.split()))
        if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
            return a + b
        else:
            print("Введите числа ещё раз: ")
            sum_ab(input(), n+1)


# print(sum_ab(input(), 0))

