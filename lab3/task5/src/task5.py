def h_index(citations):
    res = 0
    citations = sorted(citations)[::-1]
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            res += 1
    return res
print(h_index([1, 3, 1]))
