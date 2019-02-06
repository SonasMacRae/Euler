import math

def Triangle(n):
    return (n*(n+1))/2

def Pentagonal(n):
    return (n*((n*3)-1))/2

def Hexagonal(n):
    return n*((2*n)-1)

TriangleArray = []
PentagonalArray = []
HexagonalArray = []

for x in range(1, 300000):
    TriangleArray.append(Triangle(x))
    PentagonalArray.append(Pentagonal(x))
    HexagonalArray.append(Hexagonal(x))

for x in range(0, len(TriangleArray)):
    if TriangleArray[x] in PentagonalArray and TriangleArray[x] in HexagonalArray:
        print TriangleArray[x]
