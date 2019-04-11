numberList = []

value = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        numberList.append(x * y)

for x in numberList:
    if str(x) == str(x)[::-1] and x > value:
        value = x

print value
