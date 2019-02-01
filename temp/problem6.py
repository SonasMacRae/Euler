def SumOfSquares(x):
    total = 0
    for i in range(1, x):
        print i
        total += i * i
    return total

def SquareOfSum(x):
    total = 0
    for i in range(1, x):
        total += i
    return total * total

print SquareOfSum(101) - SumOfSquares(101)
