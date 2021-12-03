#Opens file and saves it as a list
my_file = open("../PuzzleData/day3_puzzle_input.txt", "r")
content = my_file.read()
puzzle_data = content.split("\n")
my_file.close()

#Returns the number of times '0' and '1' occurs in a specific element of a string
def occurrence_rates(data, i):
    zero_occurrence_rate = 0
    one_occurrence_rate = 0
    for j in data:
        if j[i] == "0":
            zero_occurrence_rate+=1
        elif j[i] == "1":
            one_occurrence_rate+=1
            
    return zero_occurrence_rate, one_occurrence_rate

#Intalize gamma rating string value
gamma_rate_str = ""
#Iterates through list of strings
for i in range(len(puzzle_data[0])):
    #Gets occurrence rates
    zero_occurrence_rate, one_occurrence_rate = occurrence_rates(puzzle_data, i)
    #Builds string of binary based on occurrence rate
    if zero_occurrence_rate > one_occurrence_rate:
        gamma_rate_str = gamma_rate_str+"0"
    else:
        gamma_rate_str = gamma_rate_str+"1"
    
#Inverts string of binary '1011'->'01001'
epsilon_rate_str = ''.join(['1' if i == '0' else '0' for i in gamma_rate_str])

#converts string of binary to its integer
gamma_rate = int(gamma_rate_str, 2)
epsilon_rate = int(epsilon_rate_str, 2)

#Prints results to console
print(f"Gamma Rate: {gamma_rate}", f"Epsilon Rate: {epsilon_rate}")
print(f"Power Consumption: {gamma_rate*epsilon_rate}")
print("")

#Intailizes Oxygen generation rate list of binaries
ox_gen_rate_list = puzzle_data
#Iterates through position of binary value within string
for i in range(len(ox_gen_rate_list)):
    #Breaks loop and gets final result
    if len(ox_gen_rate_list) == 1:
        ox_gen_rate = int(ox_gen_rate_list[0], 2)
        break
    #Gets occurrence rates
    zero_occurrence_rate, one_occurrence_rate = occurrence_rates(ox_gen_rate_list, i)
    #Replaces list with new list that only contains values based on highest occurrence rate
    if zero_occurrence_rate > one_occurrence_rate:
        ox_gen_rate_list = [x for x in ox_gen_rate_list if x[i] == "0"]
    elif zero_occurrence_rate < one_occurrence_rate:
        ox_gen_rate_list = [x for x in ox_gen_rate_list if x[i] == "1"]
    #If rates are equal assigns '1'
    elif zero_occurrence_rate == one_occurrence_rate:
        ox_gen_rate_list = [x for x in ox_gen_rate_list if x[i] == "1"]

#Does all the same as above but looks for least occurrence instead of most
co2_gen_rate_list = puzzle_data
for i in range(len(co2_gen_rate_list)):
    if len(co2_gen_rate_list) == 1:
        co2_gen_rate = int(co2_gen_rate_list[0], 2)
        break
    zero_occurrence_rate, one_occurrence_rate = occurrence_rates(co2_gen_rate_list, i)
    if zero_occurrence_rate < one_occurrence_rate:
        co2_gen_rate_list = [x for x in co2_gen_rate_list if x[i] == "0"]
    elif zero_occurrence_rate > one_occurrence_rate:
        co2_gen_rate_list = [x for x in co2_gen_rate_list if x[i] == "1"]
    # If rates are equal assigns '0'
    elif zero_occurrence_rate == one_occurrence_rate:
        co2_gen_rate_list = [x for x in co2_gen_rate_list if x[i] == "0"]

#Prints results to console
print(f"Oxygen Generation Rating: {ox_gen_rate}", f"CO2 Scrubber Rating: {co2_gen_rate}")
print(f"Life Support Rating {ox_gen_rate*co2_gen_rate}")



  