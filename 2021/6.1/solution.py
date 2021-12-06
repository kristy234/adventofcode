ages = []
with open('input.txt') as input:
    for line in input.readlines():
        ages.extend([int(n) for n in line.strip().split(",")])

print(f'Initial state: {ages}')
day = 0
new_ages = []
while day < 80:
    baby_fish = []
    for a in ages:
        a = a - 1
        if a < 0:
            # New baby fish
            baby_fish.append(8)
            # Reset gestation
            new_ages.append(6)
        else:
            new_ages.append(a)

    ages = new_ages
    ages.extend(baby_fish)
    new_ages = []
    
    print(ages)
    
    day += 1

print(len(ages)) 
