def myBinary(x):
    output = ""
    y = 1
    powersList = [1]
    while 2 * y <= x:
        y *= 2
        powersList.append(y)
    for i in powersList[::-1]:
        if x - i >= 0:
            output += "1"
            x -= i
        else:
            output += "0"
    return output

def palidromic(x):
    y = str(x)[::-1]
    if str(x) == y:
        return True
    return False

sum = 0

for x in range(1, 1000000):
    if palidromic(x) and palidromic(myBinary(x)):
        sum += x
        print x
        print myBinary(x)

print sum
