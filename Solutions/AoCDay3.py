my_file = open("../PuzzleData/day3_puzzle_input.txt", "r")
content = my_file.read()
puzzle_data = content.split("\n")
my_file.close()


def occurrence_rates(data):
    zero_occurrence_rate = 0
    one_occurrence_rate = 0
    for j in data:
        if j[i] == "0":
            zero_occurrence_rate+=1
        elif j[i] == "1":
            one_occurrence_rate+=1
            
    return zero_occurrence_rate, one_occurrence_rate

gamma_rate_str = ""
for i in range(len(puzzle_data[0])):
    zero_occurrence_rate, one_occurrence_rate = occurrence_rates(puzzle_data)
    if zero_occurrence_rate > one_occurrence_rate:
        gamma_rate_str = gamma_rate_str+"0"
    else:
        gamma_rate_str = gamma_rate_str+"1"
    
epsilon_rate_str = ''.join(['1' if i == '0' else '0' for i in gamma_rate_str])

gamma_rate = int(gamma_rate_str, 2)
epsilon_rate = int(epsilon_rate_str, 2)

print(f"Gamma Rate: {gamma_rate}", f"Epsilon Rate: {epsilon_rate}")
print(f"Power Consumption: {gamma_rate*epsilon_rate}")
print("")

def occurrence_rates_by_position(data, position):
    zero_occurrence_rate = 0
    one_occurrence_rate = 0
    for i in data:
        if i[position] == "0":
            zero_occurrence_rate+=1
        elif i[position] == "1":
            one_occurrence_rate+=1
    return zero_occurrence_rate, one_occurrence_rate
    
ox_gen_rate_list = puzzle_data
for i in range(len(ox_gen_rate_list)):
    if len(ox_gen_rate_list) == 1:
        ox_gen_rate = int(ox_gen_rate_list[0], 2)
        break
    zero_occurrence_rate, one_occurrence_rate = occurrence_rates_by_position(ox_gen_rate_list, i)
    if zero_occurrence_rate > one_occurrence_rate:
        ox_gen_rate_list = [x for x in ox_gen_rate_list if x[i] == "0"]
    elif zero_occurrence_rate < one_occurrence_rate:
        ox_gen_rate_list = [x for x in ox_gen_rate_list if x[i] == "1"]
    elif zero_occurrence_rate == one_occurrence_rate:
        ox_gen_rate_list = [x for x in ox_gen_rate_list if x[i] == "1"]
        
co2_gen_rate_list = puzzle_data
for i in range(len(co2_gen_rate_list)):
    if len(co2_gen_rate_list) == 1:
        co2_gen_rate = int(co2_gen_rate_list[0], 2)
        break
    zero_occurrence_rate, one_occurrence_rate = occurrence_rates_by_position(co2_gen_rate_list, i)
    if zero_occurrence_rate < one_occurrence_rate:
        co2_gen_rate_list = [x for x in co2_gen_rate_list if x[i] == "0"]
    elif zero_occurrence_rate > one_occurrence_rate:
        co2_gen_rate_list = [x for x in co2_gen_rate_list if x[i] == "1"]
    elif zero_occurrence_rate == one_occurrence_rate:
        co2_gen_rate_list = [x for x in co2_gen_rate_list if x[i] == "0"]
    
print(f"Oxygen Generation Rating: {ox_gen_rate}", f"CO2 Scrubber Rating: {co2_gen_rate}")
print(f"Life Support Rating {ox_gen_rate*co2_gen_rate}")



  