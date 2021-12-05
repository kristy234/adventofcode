with open('input.txt') as input:
    aim = 0
    forwards = 0
    down = 0
    for line in input.readlines():
        direction, amount = line.strip().split(" ")
        amount = int(amount)
        if 'forward' == direction:
            forwards += amount
            down += aim*amount
        if 'down' == direction:
            aim += amount
        if 'up' == direction:
            aim -= amount

    print("Forwards: " + str(forwards))
    print("Down: " + str(down))
    print("Total: " + str(forwards*down))
        
