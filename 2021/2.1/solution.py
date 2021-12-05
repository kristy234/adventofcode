with open('input.txt') as input:
    forwards = 0
    down = 0
    for line in input.readlines():
        direction, amount = line.strip().split(" ")
        amount = int(amount)
        if 'forward' == direction:
            forwards += amount
        if 'down' == direction:
            down += amount
        if 'up' == direction:
            down -= amount

    print("Forwards: " + str(forwards))
    print("Down: " + str(down))
    print("Total: " + str(forwards*down))
        
