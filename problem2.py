counter = 0

current = 0
previous = 0
x = 1

while x < 4000000:
    if x % 2 == 0:
        counter += x

    previous = current
    current = x
    x = previous + current

print(counter)
