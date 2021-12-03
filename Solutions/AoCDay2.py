#Opens file and saves it as a list
my_file = open("../PuzzleData/day2_puzzle_input.txt", "r")
content = my_file.read()
puzzle_data = content.split("\n")
puzzle_data = [x.split(" ") for x in puzzle_data]
my_file.close()

#Intalize values
horiz = 0
depth = 0
#Iterate over commands
for command, number in puzzle_data:
    if 'down' in command:
        #get number value from command
        number = int(number)
        depth+=number
    elif 'up' in command:
        number = int(number)
        depth-=number
    if 'forward' in command:
        number = int(number)
        horiz+=number
        
print(f"Horizontal Postion: {horiz}")
print(f"Depth: {depth}")
print(f"Nonsense Solution: {horiz*depth}")
print("")

#Reset values for new caluclations
horiz = 0
depth = 0
aim = 0
for command,number in puzzle_data:
    if 'down' in command:
        number = int(number)
        aim+=number
    elif 'up' in command:
        number = int(number)
        aim-=number
    if 'forward' in command:
        number = int(number)
        horiz+=number
        depth = depth+(aim*number)
        
print(f"Horizontal Postion: {horiz}")
print(f"Depth: {depth}")
print(f"Aim: {aim}")
print(f"Solution: {horiz*depth}")