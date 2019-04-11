def CheckPrime(x):
    for y in range(2, x):
        if x % y == 0:
            return False
    return True

number = 600851475143

x = 10
value = 0

while (x * x) < number:
    if number % x == 0 and CheckPrime(x) == True:
        value = x
    x += 1

print value
