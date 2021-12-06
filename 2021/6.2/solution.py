from collections import Counter, defaultdict
ages = []
with open('input.txt') as input:
    for line in input.readlines():
        ages.extend([int(n) for n in line.strip().split(",")])

ages_count = Counter(ages)
print(f'Initial state: {ages}')
day = 0
while day < 256:
    baby_fish = 0
    new_ages_count = defaultdict(int)
    for a,c in ages_count.items():
        new_age = a -1
        if new_age < 0:
            # New baby fish
            new_ages_count[8] += c
            # Reset gestation
            new_ages_count[6] += c
        else:
            new_ages_count[new_age] += c

    ages_count = new_ages_count
    print(ages_count)
    
    day += 1

print(sum(ages_count.values()) )
