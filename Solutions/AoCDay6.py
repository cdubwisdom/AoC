with open("../PuzzleData/day6_puzzle_input.txt", "r") as my_file:
    content = my_file.read()
    puzzle_data = content.split(",")
    puzzle_data = [int(x) for x in puzzle_data]

def solution_1(data, days):
    fish = data
    for i in range(days):
        if 0 in fish:
            for i in range(fish.count(0)):
                fish.append(9)
            fish = [7 if x <= 0 else x for x in fish]
        fish = [x-1 for x in fish]
    return len(fish)

def solution_2(data, days):
    fish_age_count = [data.count(x) for x in range(9)]
    for i in range(days):
        #print(fish_age_count)
        spawners = fish_age_count.pop(0)
        fish_age_count[6] += spawners
        fish_age_count.append(spawners)
        assert len(fish_age_count) == 9
    return sum(fish_age_count)

print(f"Laternfish after 80 days: {solution_1(puzzle_data, 80)}")
print(f"Laternfish after 256 days: {solution_2(puzzle_data, 256)}")
