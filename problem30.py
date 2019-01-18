def check(x):
    total = 0
    array = list(str(x))
    for i in array:
        temp = int(i)
        total += temp * temp * temp * temp * temp
    if total == x:
        return True

total = 0

for i in range(1, 10000000):
    if check(i) == True:
        total += i
print total
