import numpy as np

def get_adjacent(octo_map, pos):
    num_of_rows, num_of_cols = octo_map.shape
    row_index, col_index = pos

    adjacent_pos = set()
    if row_index > 0:
        adjacent_pos.add((row_index - 1,col_index))
    if row_index < num_of_rows - 1:
        adjacent_pos.add((row_index + 1,col_index))
    if col_index > 0:
        adjacent_pos.add((row_index,col_index - 1))
    if col_index < num_of_cols - 1:
        adjacent_pos.add((row_index,col_index + 1))
    if row_index > 0 and col_index > 0:
        adjacent_pos.add((row_index - 1,col_index - 1))
    if row_index > 0 and col_index < num_of_cols -1:
        adjacent_pos.add((row_index - 1,col_index + 1))
    if row_index < num_of_rows-1 and col_index > 0:
        adjacent_pos.add((row_index + 1,col_index - 1))
    if row_index < num_of_rows-1 and col_index < num_of_cols -1:
        adjacent_pos.add((row_index + 1,col_index + 1))

    return adjacent_pos

def solution1(data):
    num_of_rows, num_of_cols = data.shape
    total_flashes = 0
    for step in range(100):
        flashes = set()
        data += np.ones(data.shape, dtype=int)
        flashed = True if np.count_nonzero(data > 9) > 0 else False
        total_flashes += np.count_nonzero(data > 9)
        data = np.where(data > 9, 0, data)

        while flashed:
            flashed = False
            for i in range(num_of_rows):
                for j in range(num_of_cols):
                    adjacents = get_adjacent(data, (i,j))
                    for adj in adjacents - flashes:
                        if data[i,j] != 0 and data[adj] == 0:
                            data[i,j] += 1
            if np.count_nonzero(data > 9) > 0:
                flashed = True
            total_flashes += np.count_nonzero(data > 9)
            flashes.update([x for x in zip(np.where(data == 0)[0], np.where(data == 0)[1])])
            data = np.where(data > 9, 0, data)

    return total_flashes

def solution2(data):
    num_of_rows, num_of_cols = data.shape
    step_count = 0
    while data.sum() != 0:
        flashes = set()
        data += np.ones(data.shape, dtype=int)
        flashed = True if np.count_nonzero(data > 9) > 0 else False
        data = np.where(data > 9, 0, data)

        while flashed:
            flashed = False
            for i in range(num_of_rows):
                for j in range(num_of_cols):
                    adjacents = get_adjacent(data, (i, j))
                    for adj in adjacents - flashes:
                        if data[i, j] != 0 and data[adj] == 0:
                            data[i, j] += 1
            if np.count_nonzero(data > 9) > 0:
                flashed = True
            flashes.update([x for x in zip(np.where(data == 0)[0], np.where(data == 0)[1])])
            data = np.where(data > 9, 0, data)
        step_count += 1

    return step_count+1


with open("../PuzzleData/day11_puzzle_input.txt", "r") as my_file:
    content = my_file.read()
    puzzle_data = content.split("\n")
    puzzle_data = np.array([[int(x) for x in y] for y in puzzle_data])

print(f"Number of Flashes After 100 Steps: {solution1(puzzle_data)}")
print(f"Number of Steps Till Synchronisation: {solution2(puzzle_data)}")