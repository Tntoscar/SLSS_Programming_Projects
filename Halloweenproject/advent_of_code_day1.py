# Advent of code 2021 Day 1

# To open the file
with open("./data/input-day1.txt") as f:
    depths = []

    for line in f:
        depths.append(int(line))
increases = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        increases += 1

print(increases)

increases = 0

for i in range(1, len(depths)):
    if i == 1 and sum(depths[:i]) > depths[0]:
        increases += 1
    elif sum(depths[i-2:i]):
