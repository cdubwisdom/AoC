with open("../PuzzleData/day10_puzzle_input.txt") as my_file:
    puzzle_data = [x.strip() for x in my_file.readlines()]

chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
opening_chunks = chunks.keys()
corrupt_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_points= {')': 1, ']': 2, '}': 3, '>': 4}
corrupt_score = 0
incomplete_scores = []

for line in puzzle_data:
    closing_chunks = []
    for chunk in line:
        if chunk in opening_chunks:
            closing_chunks.append(chunks[chunk])
        elif chunk == closing_chunks[-1]:
            closing_chunks.pop()
        else:
            corrupt_score += corrupt_points[chunk]
            break
    else:
        incomplete_score = 0
        while closing_chunks:
            incomplete_score = 5 * incomplete_score + incomplete_points[closing_chunks.pop()]
        incomplete_scores.append(incomplete_score)

print(f"Syntax error score: {corrupt_score}")
incomplete_scores.sort()
print(f"Autocomplete Score: {incomplete_scores[len(incomplete_scores)//2]}")