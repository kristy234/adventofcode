with open('input.txt') as input:
    count_larger = -3 # The first 3 measurement will be detected as an increase when it shouldn't be counted
    window_count = -3
    w1 = -1
    w2 = -1
    w3 = -1
    prev = -1
    for line in input.readlines():
        window_count += 1
        w1 = w2
        w2 = w3
        w3 = int(line.strip())
        window_sum = w1 + w2 + w3
        print("Window " + str(window_count) + ": " + str(window_sum))
        if window_sum > prev:
            print("^ Larger")
            count_larger += 1
        prev = window_sum
    print("Number of windows in total:")
    print(window_count)
    print("Number of windows that are larget than the previous window:")
    print(count_larger)
        
