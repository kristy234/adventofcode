with open('input.txt') as input:
    prev = -1
    count_total = 0
    count_larger = -1 # The first measurement will be detected as an increase when it shouldn't be counted
    for line in input.readlines():
        count_total += 1
        measurement = int(line.strip())
        if measurement > prev:
            count_larger += 1
        prev = measurement
    print("Number of measurements in total:")
    print(count_total)
    print("Number of measurements that are larget than the previous measurement:")
    print(count_larger)
        
