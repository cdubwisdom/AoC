from collections import Counter


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self.p1 = point_1
        self.p2 = point_2
        self.length = max(abs(self.p2.x - self.p1.x), abs(self.p2.y - self.p1.y))
        self.points = [(self.p1.x + round(self.p2.x - self.p1.x) / self.length * i, self.p1.y + round(self.p2.y - self.p1.y) / self.length * i) for i in range(self.length+1)]

    def __str__(self):
        return f"({self.p1.x},{self.p1.y})->({self.p2.x},{self.p2.y})"


    def orthogonal(self):
        return self.p1.x == self.p2.x or self.p1.y == self.p2.y


def solution1(data):
    line_segments = []
    for line in data:
        p1 = Point(line[0][0], line[0][1])
        p2 = Point(line[1][0], line[1][1])
        line_segments.append(Line(p1,p2))

    intersections = Counter()
    for segment in filter(lambda x: x.orthogonal(), line_segments):
        intersections.update(segment.points)

    return len([x for x in intersections.items() if x[1] > 1])

def solution2(data):
    line_segments = []
    for line in data:
        p1 = Point(line[0][0], line[0][1])
        p2 = Point(line[1][0], line[1][1])
        line_segments.append(Line(p1,p2))

    intersections = Counter()
    for segment in line_segments:
        intersections.update(segment.points)

    return len([x for x in intersections.items() if x[1] > 1])

with open("../PuzzleData/day5_puzzle_input.txt", "r") as my_file:
    content = my_file.read()
    puzzle_data = content.split('\n')
    puzzle_data = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in puzzle_data]

print(f"Number of Intersecting Points for Orthogonal Lines: {solution1(puzzle_data)}")
print(f"Number of Intersecting Points for All Lines: {solution2(puzzle_data)}")