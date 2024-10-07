import numpy as np

n = 4
from random import randint

A = []
B = []
C = []
for i in range(n):
    a = []
    b = []
    c = []
    for j in range(n):
        a.append(randint(-10, 10))
        b.append(randint(-10, 10))

    A.append(a)
    B.append(b)


if n % 2 == 1:
    for i in range(n):
        A[i].append(0)
        B[i].append(0)
    n += 1
    A.append([0]*(n))
    B.append([0] * (n))

for i in range(n):
    c = []
    for j in range(n):
        c.append(0)

    C.append(c)

def multiply(X, Y):
    A = X[0][0]
    B = X[0][1]
    C = X[1][0]
    D = X[1][1]

    E = Y[0][0]
    F = Y[0][1]
    G = Y[1][0]
    H = Y[1][1]

    P1 = A * (F - H)
    P2 = (A + B) * H
    P3 = (C + D) * E
    P4 = D * (G - E)
    P5 = (A + D) * (E + H)
    P6 = (B - D) * (G + H)
    P7 = (A - C) * (E + F)
    return [P5 + P4 - P2 + P6, P1 + P2, P3 + P4,  P1 + P5 - P3 - P7]

for i in range(0, n, 2):
    for j in range(0, n, 2):
        res = multiply([A[j][i:i+2], A[j+1][i:i+2]], [B[j][i:i+2], B[j+1][i:i+2]])

        C[j][i] += res[0]
        C[j][i+1] += res[1]
        C[j+1][i] += res[2]
        C[j+1][i+1] += res[3]

print(C)
import numpy
A = numpy.array(A)
B = numpy.array(B)
print(np.dot(A,B))