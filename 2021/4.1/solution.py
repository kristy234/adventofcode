from itertools import groupby
import numpy as np
from collections import defaultdict

bingo_numbers = []
boards = []
index = defaultdict(list)
with open('input.txt') as input:
    lines = input.readlines()

    bingo_numbers = [int(n.strip()) for n in lines[0].split(",")]

    boards = []
    board_lines = lines[2:]
    b = 0
    for k, g in groupby(board_lines, key = lambda line: line.strip() != ''):
        if k:
            print("Parsing board " + str(b))
            board = []
            r = 0 # row
            c = 0 # column
            for row in list(g):
                print("Parsing row: " + row)
                row = [int(n.strip()) for n in row.strip().split(' ') if n.strip() != '']
                for n in row:
                    print(str(n) + " appears in " + str((b, r, c)))
                    index[n].append((b,r,c))
                    c += 1
                r += 1
                c = 0
                board.append(row)
            boards.append(np.array(board))
            b += 1

boards = np.array(boards)
last_winning_score = 0
for n in bingo_numbers:
    print("Drawing " + str(n))
    for coordinate in index[n]:
        print("Board: " + str(coordinate[0]) + " marks off " + str((coordinate[1], coordinate[2])))
        boards[coordinate[0]][coordinate[1]][coordinate[2]] = 0
        board = boards[coordinate[0]]
        if np.all(board == 0, axis = 0).any() or np.all(board == 0, axis = 1).any():
            print("Bingo!")
            print("Board " + str(coordinate[0]) + " wins")
            board_sum = np.sum(board)
            print("Board total: " + str(board_sum))
            score = board_sum * n
            print("Score: " + str(score))
            last_winning_score = score 
