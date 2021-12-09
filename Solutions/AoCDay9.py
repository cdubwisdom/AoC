from skimage.segmentation import flood
import numpy as np


def solution1(data):
    num_of_cols = len(data[0])
    num_of_rows = len(data)

    risk_level = 0
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            adjacent = []
            if row_index > 0:
                adjacent.append(data[row_index-1][col_index])
            if row_index < num_of_rows-1:
                adjacent.append(data[row_index+1][col_index])
            if col_index > 0:
                adjacent.append(data[row_index][col_index-1])
            if col_index < num_of_cols-1:
                adjacent.append(data[row_index][col_index+1])

            if value < min(adjacent):
                risk_level += value+1

    return risk_level


def solution2(data):
    num_of_cols = len(data[0])
    num_of_rows = len(data)

    low_point_locations = []
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            adjacent = []
            if row_index > 0:
                adjacent.append(data[row_index - 1][col_index])
            if row_index < num_of_rows - 1:
                adjacent.append(data[row_index + 1][col_index])
            if col_index > 0:
                adjacent.append(data[row_index][col_index - 1])
            if col_index < num_of_cols - 1:
                adjacent.append(data[row_index][col_index + 1])

            if value < min(adjacent):
                low_point_locations.append((row_index,col_index))

    location_map = np.array(data)
    location_map[location_map < 9] = 1
    basin_sizes = []
    for (i,j) in low_point_locations:
        mask = flood(location_map, (i,j), tolerance=1, connectivity=1)
        basin_sizes.append(mask.sum())

    return np.prod(sorted(basin_sizes)[-3:])

with open("../PuzzleData/day9_puzzle_input.txt", "r") as my_file:
    content = my_file.read()
    puzzle_data = content.split("\n")
    puzzle_data = [[int(x) for x in y] for y in puzzle_data]


print(f"Risk Level of Low Points: {solution1(puzzle_data)}")
print(f"Product of Three Largest Basins: {solution2(puzzle_data)}")