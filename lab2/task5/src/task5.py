# def frequent(n, array):
#     dict = {}
#     res = 1
#     for i in range(n):
#         elem = array[i]
#         if elem in dict:
#             dict[elem] += 1
#         else:
#             dict[elem] = 1
#         if dict[elem] > n / 2:
#             return 1
#         else:
#             res = 1
#     if res:
#         return 0
# print(frequent(5, [3, 4, 3, 3, 4]))


# from collections import Counter
# n = 5
# my_list = [1, 1, 2, 3, 1]
# most_common_element = Counter(my_list).most_common(1)[0][1] > n / 2
#
# print(most_common_element)

