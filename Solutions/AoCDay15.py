import numpy as np
import heapq


def solution1(data):
    num_of_rows, num_of_cols = data.shape
    risks = np.array([[-1]*num_of_cols for _ in range(num_of_rows)])
    risks[0,0] = 0
    queue = [(0,0,0)]
    while risks[-1,-1] == -1:
        risk, row, col = heapq.heappop(queue)
        for row_change, col_change in [(-1,0),(1,0),(0,-1),(0,1)]:
            new_row, new_col = row + row_change, col + col_change
            if 0 <= new_row < num_of_rows and 0 <= new_col < num_of_cols and risks[new_row,new_col] == -1:
                risks[new_row,new_col] = risk + data[new_row,new_col]
                heapq.heappush(queue, (risks[new_row,new_col], new_row, new_col))
    return risks[-1,-1]

def solution2(data):
    num_of_rows, num_of_cols = data.shape
    new_map = np.array([[0] *(5*num_of_cols) for _ in range(5*num_of_rows)])
    for scaled_row in range(5):
        for scaled_col in range(5):
            for row in range(num_of_rows):
                for col in range(num_of_cols):
                    new_row, new_col = num_of_rows*scaled_row+row, num_of_cols*scaled_col+col
                    new_map[new_row,new_col] = data[row,col] + scaled_row + scaled_col
                    if new_map[new_row,new_col] > 9:
                        new_map[new_row,new_col] -= 9

    return solution1(new_map)


test = False
if test:
    with open("../PuzzleData/test_data.txt", "r") as my_file:
        content = my_file.read()
        puzzle_data = content.split("\n")
        puzzle_data = np.array([[int(x) for x in y] for y in puzzle_data])
else:
    with open("../PuzzleData/day15_puzzle_input.txt", "r") as my_file:
        content = my_file.read()
        puzzle_data = content.split("\n")
        puzzle_data = np.array([[int(x) for x in y] for y in puzzle_data])

print(f"Lowest Risk Level: {solution1(puzzle_data)}")
print(f"Lowest Risk Level in Expanded Cave: {solution2(puzzle_data)}")