from collections import Counter, defaultdict
positions = []
with open('input.txt') as input:
    for line in input.readlines():
        for position in line.strip().split(","):
            positions.append(int(position))

min_distance = -1
best_position = -1
for x in range(min(positions), max(positions)):
    distance = 0
    for pos in positions:
        distance += abs(x-pos)
    if min_distance < 0 or distance < min_distance:
        min_distance = distance
        best_position = x

print(f"Best position {best_position} with total distance of {min_distance}")
