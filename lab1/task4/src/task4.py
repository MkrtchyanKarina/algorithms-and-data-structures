from lab1.src.verifications import data_verification4


@data_verification4
def lineal_search(m, x):
    res = []
    for i in range(len(m)):
        if m[i] == x:
            res.append(i)
    count = len(res)
    if count == 0:
        return str(-1)
    elif count == 1:
        return str(res[0])
    else:
        return str(count) + ' ' + ", ".join(map(str, res))


# file = open("input4.txt")
# array = list(map(int, file.readline().split(" ")))
# V = int(file.readline())
# open("output4.txt", "w").write(lineal_search(array, V))

