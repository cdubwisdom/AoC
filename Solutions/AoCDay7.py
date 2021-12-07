with open("../PuzzleData/day7_puzzle_input.txt", "r") as my_file:
    content = my_file.read()
    puzzle_data = content.split(",")
    puzzle_data = [int(x) for x in puzzle_data]

def solution_1(data):
    positions = [x for x in range(min(data), max(data)+1)]

    fuel_spent = []
    for j in positions:
        fuel = []
        for i in range(len(data)):
            fuel.append(abs(data[i]-j))
        fuel_spent.append(sum(fuel))

    print(f"Minimum Possible Amount of Fuel: {min(fuel_spent)} to Position: {positions[fuel_spent.index(min(fuel_spent))]}")

solution_1(puzzle_data)

def solution_2(data):
    positions = [x for x in range(min(data), max(data)+1)]

    fuel_spent = []
    for j in positions:
        fuel = []
        for i in range(len(data)):
            distance = abs(data[i]-j)
            fuel.append(int(0.5*distance*(distance+1)))
        fuel_spent.append(sum(fuel))

    print(f"Minimum Possible Amount of Fuel with Non-constant Burn: {min(fuel_spent)} to Position: {positions[fuel_spent.index(min(fuel_spent))]}")

solution_2(puzzle_data)
