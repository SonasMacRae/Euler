def Sum(x):
	number = int(str(x)[::-1])
	if str(x)[::-1][0] == "0":
		return 2
	return number + x

counter = 0

for x in range(0, 1000):
	flag = True

	for y in str(Sum(x)):
		if int(y) % 2 == 0:
			flag = False

	if flag == True:
		counter += 1

print (counter)
