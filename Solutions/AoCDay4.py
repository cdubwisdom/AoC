import numpy as np

input = open('../PuzzleData/day4_puzzle_input.txt').read()

draw, boards = input.split('\n', 1)
draw = [int(i) for i in draw.split(',')]
boards = boards.strip().split('\n\n')

boards = [
    np.array([[int(j) for j in i.split(' ') if j != ''] for i in board.strip().split('\n')])
    for board in boards
]

def checkIfWon(board):
    for y in range(board.shape[0]):
        if np.all(board[y,:] < 0): return True

    for x in range(board.shape[1]):
        if np.all(board[:,x] < 0): return True

    return False

def result(board, call):
    return np.sum(board[board > 0]) * call

winner = []
for call in draw:
    for i in range(len(boards)-1,-1,-1):
        board = boards[i]
        board[board == call] *= -1
        if checkIfWon(board):
            winner.append((board, call))
            boards.pop(i)

print('Part 1:' , result(*winner[0]))
print('Part 2:' , result(*winner[len(winner)-2]))
