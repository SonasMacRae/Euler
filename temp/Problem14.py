def DeterminValue(x):
    counter = 1
    while x != 1:
        if x % 2 == 0:
             x = even(x)
        else:
            x = odd(x)
        counter += 1
        if x == 1:
            return counter
            break

def odd(x):
    return (3 * x) + 1

def even(x):
    return x / 2

number = 0
lawd = 0

for x in range(1, 1000000):
    value = DeterminValue(x)
    if value > number:
        number = value
        lawd = x
print lawd
