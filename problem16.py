initialValue = 2
finalValue = 0

for x in range(1, 1000):
    initialValue *= 2

for y in str(initialValue):
    finalValue += int(y)

print finalValue
