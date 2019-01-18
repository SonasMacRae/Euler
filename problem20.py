def factorial(x):
    total = 1
    for i in range(1, x + 1):
        total *= i
    return total

def add(x):
    total = 0
    array = list(str(x))
    for i in array:
        total += int(i)
    return total

initial = factorial(100)
final = add(initial)

print final
