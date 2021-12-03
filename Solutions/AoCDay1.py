#Opens file and saves it as a list of ints
my_file = open("../PuzzleData/day1_puzzle_input.txt", "r")
content = my_file.read()
puzzle_data = content.split("\n")
puzzle_data = [int(x) for x in puzzle_data]
my_file.close()

#To track number of depth increases
count = 0
#iterate and compare depth values
for prev_depth, new_depth in zip(puzzle_data, puzzle_data[1:]):
    #increment count if depth increases
    count += prev_depth < new_depth

#display results to console
print(f"Number of Depth Changes: {count}")
print("")

#reset count
count = 0
#create initial value
prev_sum = sum(puzzle_data[:3])
#iterate over data, discard is first value in prev_sum, add is subsequent value of sliding window
for discard, add in zip(puzzle_data, puzzle_data[3:]):
    new_sum = prev_sum - discard + add
    #increment count
    count += new_sum > prev_sum
    #recasts new_sum as prev_sum
    prev_sum = new_sum

#display result to console
print(f"Number of Three-Measurement Sliding Window Depth Changes: {count}")
