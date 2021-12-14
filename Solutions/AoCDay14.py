from re import findall
from collections import Counter
from math import floor


def insert_element(chain, element, index):
    return chain[:index+1] + element + chain[index+1:]

def solution1(data):
    template, pairs = data[0], data[1].split("\n")
    pairs = [[y for y in x.split(" -> ")] for x in pairs]
    chain = template
    for _ in range(10):
        new_chain = chain
        for i in range(len(chain)-1):
            for pair in pairs:
                if chain[i:i+2] == pair[0]:
                    new_chain = insert_element(new_chain, pair[1], i+(len(new_chain)-len(chain)))
                    break
        chain = new_chain

    element_occurrence = [chain.count('N'), chain.count('C'), chain.count('B'), chain.count('H')]

    return max(element_occurrence)-min(element_occurrence)



def solution2(data):
    template, pairs = data[0], data[1]
    pairs = dict(findall('(\w\w) -> (\w)', pairs))
    count = Counter(map(''.join, zip(template, template[1:])))

    for _ in range(40):
        for key, n in count.copy().items():
            count[key] -= n
            middle = pairs[key]
            first, second = key
            count[first + middle] += n
            count[middle + second] += n

    element_occurrence = Counter()
    for (first, second), n in count.items():
        element_occurrence[first] += n
        element_occurrence[second] += n
    (_,most_common), *_, (_,least_common) = element_occurrence.most_common()

    return floor((most_common-least_common)/2)


with open("../PuzzleData/day14_puzzle_input.txt", "r") as my_file:
    content = my_file.read()
    puzzle_data = content.split("\n\n")

print(f"Max Element Count Subtract Min Element Count for 10 Steps: {solution1(puzzle_data)}")
print(f"Max Element Count Subtract Min Element Count for 40 Steps: {solution2(puzzle_data)}")