ones = []
zeros = []
initial = []
bit = 0

with open('input.txt') as input:
    for line in input.readlines():
        line = line.strip()
        length = len(line)
        initial.append(line)

if len(initial) == 0:
    print("No input")
    quit()
length = len(initial[0])

print("Input: ")
print("\n".join(initial))

print("Calculating Oxygen Generator Rating")
remaining = initial
while len(remaining) > 1 and bit < length:
    print("Number of items in remaining: " + str(len(remaining)))
    print("Calculating bit " + str(bit))

    for num in remaining:
        if '1' == num[bit]:
            print("Sorting into 'ones' for bit " + str(bit) + ": " + num)
            ones.append(num)
        else:
            print("Sorting into 'zeros' for bit " + str(bit) + ": " + num)
            zeros.append(num)

    remaining = ones if len(ones) >= len(zeros) else zeros
    bit += 1
    ones = []
    zeros = []

if len(remaining) > 1:
    print("Duplicates detected:")
    print("\n".join(remaining))
    quit()

remaining = remaining[0]
print("Remaining numner: " + remaining)
ogr = int(remaining,2)
print("Oxygen Generator Rating: " + str(ogr))

print("Calculating CO2 Scrubber Rating")
remaining = initial
bit = 0
while len(remaining) > 1 and bit < length:
    print("Number of items in remaining: " + str(len(remaining)))
    print("Calculating bit " + str(bit))

    for num in remaining:
        if '1' == num[bit]:
            print("Sorting into 'ones' for bit " + str(bit) + ": " + num)
            ones.append(num)
        else:
            print("Sorting into 'zeros' for bit " + str(bit) + ": " + num)
            zeros.append(num)

    remaining = zeros if len(zeros) <= len(ones) else ones
    bit += 1
    ones = []
    zeros = []

if len(remaining) > 1:
    print("Duplicates detected:")
    print("\n".join(remaining))
    quit()

remaining = remaining[0]
print("Remaining numner: " + remaining)
co2sr = int(remaining,2)
print("CO2 Scrubber Rating: " + str(co2sr))

print()
print("Oxygen Generator Rating: " + str(ogr))
print("CO2 Scrubber Rating: " + str(co2sr))
solution = ogr*co2sr
print("Solution: " + str(solution))
