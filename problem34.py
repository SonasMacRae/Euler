def factorial(x):
    total = 1
    for i in range(1, x + 1):
        total *= i
    return total

final_total = 0
total = 0


for j in range(10, 10000000):
    temp = 0
    temp_array = list(str(j))
    for k in temp_array:
        temp += factorial(int(k))
    if temp == j:
        print temp
        final_total += temp

print final_total
