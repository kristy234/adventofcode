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
            board = []
            r = 0 # row
            c = 0 # column
            for row in list(g):
                row = [int(n.strip()) for n in row.strip().split(' ') if n.strip() != '']
                for n in row:
                    index[n].append((b,r,c))
                    c += 1
                r += 1
                c = 0
                board.append(row)
            boards.append(np.array(board))
            b += 1

boards = np.array(boards)
winning_boards = []
for n in bingo_numbers:
    print()
    print("Drawing " + str(n))
    for coordinate in index[n]:
        print("Board: " + str(coordinate[0]) + " marks off " + str((coordinate[1], coordinate[2])))
        boards[coordinate[0]][coordinate[1]][coordinate[2]] = 0
        board = boards[coordinate[0]]
        if coordinate[0] not in winning_boards and (np.all(board == 0, axis = 0).any() or np.all(board == 0, axis = 1).any()):
            winning_boards.append(coordinate[0])
            print("Bingo!")
            print("Board " + str(coordinate[0]) + " wins")
            board_sum = np.sum(board)
            print("Board total: " + str(board_sum))
            score = board_sum * n
            print("Score: " + str(score))

            if len(winning_boards) == len(boards):
                print("All boards have now won")
                print("Board " + str(coordinate[0]) + " was last to win with score " + str(score))
                print(score)
                quit()
