import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

def print_diagram(diagram):
    for row in diagram:
        for n in row:
            print(int(n) if n > 0 else '.', end='')
        print()


diagram = np.zeros((1, 1))
with open('input.txt') as input:
    for line in input.readlines():
        c1, c2 = line.split("->")
        c1 = [int(c) for c in c1.strip().split(",")]
        c2 = [int(c) for c in c2.strip().split(",")]
        print(f'{c1} -> {c2}')
        
        # Only consider straight lines
        if c1[0] != c2[0] and c1[1] != c2[1]:
            print(f"Skipping {c1} -> {c2} as it is not a straight line")
            continue
       
        x1 = min(c1[0], c2[0])
        x2 = max(c1[0], c2[0])
        y1 = min(c1[1], c2[1])
        y2 = max(c1[1], c2[1])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                # Resize the diagram if need be
                if x >= diagram.shape[1] or y >= diagram.shape[0]:
                    resize_y = max(y - diagram.shape[0] + 1, 0)
                    resize_x = max(x - diagram.shape[1] + 1, 0)
                    print(f'Resizing the matrix by ({resize_x}, {resize_y})')
                    diagram = np.pad(diagram, ((0, resize_y), (0, resize_x)), mode='constant', constant_values=0)
                
                # Increment the position in the diagram
                diagram[y][x] += 1

print_diagram(diagram)
print('Total: ')
print((diagram > 1).sum())
