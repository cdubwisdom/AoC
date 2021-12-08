def solution1(data):
    occurrence = 0
    for line in data:
        for digit in line['output']:
            if len(digit) in (7, 4, 3, 2):
                occurrence+=1

    return occurrence

def solution2(data):
    output_sum = 0
    for line in data:
        patterns = {
            i: [set(v) for v in list(filter(lambda v: len(v) == i, line['pattern']))]
            for i in [2, 3, 4, 5, 6, 7]
        }

        digits = {
            1: patterns[2][0],
            4: patterns[4][0],
            7: patterns[3][0],
            8: patterns[7][0]
        }
        digits[3] = next(x for x in patterns[5] if x >= digits[1])
        digits[5] = next(x for x in patterns[5] if x >= digits[4]-digits[1])
        digits[2] = next(x for x in patterns[5] if x != digits[3] and x != digits[5])
        digits[9] = next(x for x in patterns[6] if x >= digits[3])
        digits[6] = next(x for x in patterns[6] if x >= digits[2] - digits[1])
        digits[0] = next(x for x in patterns[6] if x != digits[9] and x != digits[6])

        output_sum += int("".join([next(str(x) for x, y in digits.items() if y == set(d)) for d in line['output']]))

    return output_sum


with open("../PuzzleData/day8_puzzle_input.txt", "r") as my_file:
    content = my_file.readlines()
    puzzle_data = [{
        'pattern': line.split('|')[0].strip().split(' '),
        'output': line.split('|')[1].strip().split(' ')
    } for line in content]


print(f"Occurrences of 1, 4, 7, and 8: {solution1(puzzle_data)}")
print(f"Sum of all Output Values: {solution2(puzzle_data)}")