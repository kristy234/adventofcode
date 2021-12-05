import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

def print_diagram(diagram):
    for row in diagram:
        for n in row:
            print(int(n) if n > 0 else '.', end='')
        print()

def resize_diagram(diagram, x, y):
    if x < diagram.shape[1] and y < diagram.shape[0]:
        return diagram
    resize_y = int(max(y - diagram.shape[0] + 1, 0))
    resize_x = int(max(x - diagram.shape[1] + 1, 0))
    print(f'Resizing the matrix by ({resize_x}, {resize_y})')
    return np.pad(diagram, ((0, resize_y), (0, resize_x)), mode='constant', constant_values=0)

diagram = np.zeros((1, 1))
with open('input.txt') as input:
    for line in input.readlines():
        c1, c2 = line.split("->")
        c1 = [int(c) for c in c1.strip().split(",")]
        c2 = [int(c) for c in c2.strip().split(",")]
        print(f'{c1} -> {c2}')
        
        x1 = c1[0]
        x2 = c2[0]
        x = x1
        dx = int(0 if x1==x2 else (x2-x1)/abs(x2-x1))
        print(f"{x1} -> {x2} {dx}dx")

        y1 = c1[1]
        y2 = c2[1]
        y = y1
        dy = int(0 if y2==y1 else (y2 - y1)/abs(y2-y1))
        print(f"{y1} -> {y2} {dy}dy")

        if dx == 0 and dy == 0:
            print(f"({x}, {y})")
            # Resize the diagram if need be
            diagram = resize_diagram(diagram, x, y)
                
            # Increment the position in the diagram
            diagram[y][x] += 1
        else:
            # Start one-off so that single-value lists still get covered
            x -= dx
            y -= dy
            while (x != x2 or dx == 0) and (y != y2 or dy == 0):
                # Increment x and y
                x += dx
                y += dy

                print(f"({x}, {y})")
                # Resize the diagram if need be
                diagram = resize_diagram(diagram, x, y)
                    
                # Increment the position in the diagram
                diagram[y][x] += 1


print_diagram(diagram)
print('Total: ')
print((diagram > 1).sum())
