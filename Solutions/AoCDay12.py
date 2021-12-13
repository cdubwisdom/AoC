from typing import List
from collections import Counter

def get_connections(data, location: str):
    for i in data:
        if location != "start" and (i[0] == "start" or i[1] == "start"):
            continue

        if i[0] == location:
            yield i[1]
        if i[1] == location:
            yield i[0]

def lowercase_repeat(path, location):
    location_counts = Counter(path)
    for i,j in location_counts.items():
        if i.islower() and j > 1 and location in path:
            return True

def solution1(data):
    paths: List[List[str]] = [["start"]]
    all_paths: List[List[str]] = []
    searching = True
    while searching:
        new_paths: List[List[str]] = []
        for path in paths:
            for location in get_connections(data, path[-1]):
                if location == "end":
                    all_paths.append(path + [location])
                elif location.isupper() or (location.islower() and location not in path):
                    new_paths.append(path + [location])
        if len(new_paths) == 0:
            searching = False
        else:
            paths = new_paths

    return len(all_paths)

def solution2(data):
    paths: List[List[str]] = [["start"]]
    all_paths: List[List[str]] = []
    searching = True
    while searching:
        new_paths: List[List[str]] = []
        for path in paths:
            for location in get_connections(data, path[-1]):
                if location == "end":
                    all_paths.append(path + [location])
                elif location.isupper() or (location.islower() and not lowercase_repeat(path, location)):
                    new_paths.append(path + [location])
        if len(new_paths) == 0:
            searching = False
        else:
            paths = new_paths

    return len(all_paths)


with open("../PuzzleData/day12_puzzle_input.txt", "r") as my_file:
    content = my_file.read()
    puzzle_data = content.split("\n")
    puzzle_data = [[x for x in y.split("-")] for y in puzzle_data]


print(f"All Paths without repeating small caves: {solution1(puzzle_data)}")
print(f"All Paths with a single repeating small cave: {solution2(puzzle_data)}")