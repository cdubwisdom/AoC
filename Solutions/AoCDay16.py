
def solution1(data):
    binary_str =  bin(int(data, 16))[2:].zfill(len(data)*4)
    print(binary_str)
    packet_v, packet_id = int(binary_str[:3],2), int(binary_str[3:6],2)
    if packet_id != 4:
        packet_len_id = int(binary_str[6])
        if packet_len_id == 1:
            pass
        elif packet_len_id == 0:
            print(binary_str[7:22])
            sub_packet_len = int(binary_str[7:22],2)
            print(sub_packet_len)
            sub_packets = binary_str[22:22+sub_packet_len]





test = True
if test:
    with open("../PuzzleData/test_data.txt", "r") as my_file:
        content = my_file.read()
        puzzle_data = str(content)
else:
    with open("../PuzzleData/day15_puzzle_input.txt", "r") as my_file:
        content = my_file.read()
        puzzle_data = str(content)


print(solution1(puzzle_data))