from lab1.src.verifications import data_verification8


@data_verification8
def swap(n, m):
    res = ""
    for i in range(n-1):
        index = i + 1
        minim = m[i]

        for j in range(i+1, n):
            if m[j] < minim:
                minim = m[j]
                index = j
        if minim < m[i]:
            m[i], m[index] = m[index], m[i]

            res += "Swap elements in indices " + str(i+1) + " and " + str(index+1) + "." + "\n"
        else:
            res += "No more swaps needed."
            break
    return res


# file_input = open('input8.txt')
# file_output = open('output8.txt', 'w')
# n = int(file_input.readline())
# strings = list(map(int, file_input.readline().split(" ")))
# file_output.write(swap(n, strings))

