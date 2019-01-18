import array

namez = array.names
namez.sort()

total_score = 0
position = 1

for name in namez:
    name_score = 0

    for char in name:
        name_score += ord(char) - 64

    total_score += name_score * position
    position += 1

print total_score
