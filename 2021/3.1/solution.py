bits = []
total = 0.0
length = 0
with open('input.txt') as input:
    for line in input.readlines():
        line = line.strip()
        while len(bits) < len(line):
            length += 1
            print("Extending the initial array until it is the right length (" + str(length) + ")")
            bits.append(0)
        total += 1
        for i in range(length):
            bits[i] += int(line[i])
    gamma = []
    epsilon = []
    gamma = ''.join(['1' if (b > total/2) else '0' for b in bits])
    print(gamma)
    epsilon = ''.join([str(abs(int(b)-1)) for b in gamma])
    print(epsilon)

    print("Gamma: " + str(int(gamma, 2)) + " (" + str(gamma) + ")")
    print("Epsilon: " + str(int(epsilon, 2)) + " (" + str(epsilon) + ")")
    print("Answer: " + str(int(gamma, 2)*int(epsilon, 2)))
    
    
