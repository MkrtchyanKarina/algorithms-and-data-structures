def data_verification1(func):
    def check(n, m, repeat=0):
        if 1 <= n <= 10**3 and all(abs(x) <= 10**9 for x in m) and len(m) == n:
            return func(n, m)
        else:
            if repeat >= 2:
                return "Invalid data"
            else:
                print("Enter data again")
                n = int(input())
                m = [int(i) for i in input().split()]
                return check(n, m, repeat+1)
    return check


def data_verification4(func):
    def check(M, V, repeat=0):
        if len(M) <= 10**3 and all(abs(x) <= 10**3 for x in M) and abs(V) <= 10**3 :
            return func(M, V)
        else:
            if repeat >= 2:
                return "Invalid data"
            else:
                print("Enter data again")
                M = [int(i) for i in input().split()]
                V = int(input())
                return check(M, V, repeat+1)
    return check


def data_verification7(func):
    def check(n, M, repeat=0):
        if 3 <= n < 10**4 and all(0 < x <= 10**6 for x in M) and len(M) == n:
            return func(n, M)
        else:
            if repeat >= 2:
                return "Invalid data"
            else:
                print("Enter data again")
                n = int(input())
                M = [round(float(i), 2) for i in input().split()]
                return check(n, M, repeat+1)
    return check

def data_verification8(func):
    def check(n, m, repeat=0):
        if 3 <= n <= 5000 and all(abs(x) <= 10**9 for x in m) and len(m) == n:
            return func(n, m)
        else:
            if repeat >= 2:
                return "Invalid data"
            else:
                print("Enter data again")
                n = int(input())
                m = [int(i) for i in input().split()]
                return check(n, m, repeat+1)
    return check

def data_verification9(func):
    def check(a, b, repeat=0):
        if 1 <= len(a) == len(b) <= 10**3:
            return func(a, b)
        else:
            if repeat >= 2:
                return "Invalid data"
            else:
                print("Enter data again")
                a, b = input().split()
                return check(a, b, repeat+1)
    return check