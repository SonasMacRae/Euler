counter = 1
total = 0
found = False
while found == False:
    total += counter
    counter += 1
    factor = 0
    for x in range(1, total):
        if total % x == 0:
            factor += 1
    if factor >= 500:
        print factor
        found = True
