import re
from lab3.src.utils import *


def h_index(citations: list) -> int:
    if limits(citations):
        res = 0
        citations = sorted(citations)[::-1]
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                res += 1
        return res
    else:
        return -1


def limits(citations: list):
    n = len(citations)
    if 1 <= n <= 5000 and all(0 <= i <= 1000 for i in citations):
        return True
    else:
        return False


def h_index_txt():
    args = list(map(int, re.split('[, ]', read_txt(__file__)[0])))
    result = str(h_index(args))
    write_txt(__file__, result)



if __name__ == "__main__":
    h_index_txt()