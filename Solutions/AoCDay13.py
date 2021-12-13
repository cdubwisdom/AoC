import numpy as np


def solution1(_points, _folds, ):
    dimensions = list(zip(*points[::-1]))
    shape = (max(dimensions[0]) + 1, max(dimensions[1]) + 1)
    grid = np.zeros(shape)
    for x,y in _points:
        for fold in _folds[:1]:
            if fold[0] == "x":
                x = 0 - abs(x - int(fold[1])) + int(fold[1])
            if fold[0] == 'y':
                y = 0 - abs(y - int(fold[1])) + int(fold[1])
        grid[y][x] = 1

    return np.count_nonzero(grid)

def solution2(_points, _folds):
    xmin = min([int(x[1]) for x in folds if x[0] == 'x'])
    ymin = min([int(x[1]) for x in folds if x[0] == 'y'])
    grid = np.zeros((ymin, xmin))
    for x,y in _points:
        for fold in _folds:
            if fold[0] == "x":
                x = 0 - abs(x - int(fold[1])) + int(fold[1])
            if fold[0] == 'y':
                y = 0 - abs(y - int(fold[1])) + int(fold[1])
        grid[y][x] = 1

    for row in grid:
        print(''.join(['#' if x else '.' for x in row]))


with open("../PuzzleData/day13_puzzle_input.txt", "r") as file:
    points, folds = [line.splitlines() for line in file.read().split('\n\n')]
    points = np.array([p.split(',') for p in points]).astype(int)
    folds = [x.split()[2].split('=') for x in folds]

print(f"Number of Dots After One Fold: {solution1(points, folds)}")
print("Activation Code")
solution2(points,folds)