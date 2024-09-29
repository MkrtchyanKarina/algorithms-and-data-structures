from lab1.src.verifications import data_verification1


@data_verification1
def insertion_sort(n, m):
    indexes = [1]
    for i in range(1, n):
        for j in range(i, -1, -1):
            if m[i] < m[j]:
                m[i], m[j] = m[j], m[i]
                i, j = j, i
        indexes.append(i+1)
    return indexes, m


# file_input = open("input2.txt")
# file_output = open("output2.txt", "w")
#
# test_n = int(file_input.readline())
# test_m = list(map(int, file_input.readline().split(" ")))
#
# res_ind, res_m = insertion_sort(test_n, test_m)
#
# file_output.write(" ".join(map(str, res_ind)))
# file_output.write("\n")
# file_output.write(" ".join(map(str, res_m)))