import pathlib
import sys
from typing import List, Tuple


def parse(puzzle_input_str: str) -> List[List[Tuple[int, int]]]:
    """Parse input -- list of nearly lines of vents"""
    lines = puzzle_input_str.splitlines()
    result = []
    for line in lines:
        endpoints = line.split(" -> ")
        assert(len(endpoints) == 2)
        [x1, y1] = endpoints[0].split(',')
        [x2, y2] = endpoints[1].split(',')
        result += [[(int(x1), int(y1)), (int(x2), int(y2))]]
    return result


def part1(data: List[List[Tuple[int, int]]]) -> int:
    """Solve part 1 -- Consider only horizontal and vertical lines. At how many points do at least two lines overlap?"""
    graph_size = 10 ** 3

    diagram = [[0 for _ in range(graph_size)] for _ in range(graph_size)]

    # Updating the diagram with vertical and horizontal lines
    for [(x1, y1), (x2, y2)] in data:
        # vertical lines
        if x1 == x2:
            col = x1
            for row in range(min(y1, y2), max(y1, y2) + 1):
                diagram[row][col] += 1

        # horizontal lines
        elif y1 == y2:
            row = y1
            for col in range(min(x1, x2), max(x1, x2) + 1):
                diagram[row][col] += 1

    # Calculating the number of points where at least two lines overlap
    count = 0
    for row in diagram:
        for point in row:
            if point >= 2:
                count += 1
    return count


def part2(data: List[List[Tuple[int, int]]]) -> int:
    """Solve part 2 -- Consider all of the lines. At how many points do at least two lines overlap?"""
    graph_size = 10 ** 3

    diagram = [[0 for _ in range(graph_size)] for _ in range(graph_size)]

    # Updating the diagram with vertical and horizontal lines
    for [(x1, y1), (x2, y2)] in data:
        # vertical lines
        if x1 == x2:
            col = x1
            for row in range(min(y1, y2), max(y1, y2) + 1):
                diagram[row][col] += 1

        # horizontal lines
        elif y1 == y2:
            row = y1
            for col in range(min(x1, x2), max(x1, x2) + 1):
                diagram[row][col] += 1

        # diagonal lines
        else:
            drow = 1
            dcol = 1
            if y2 < y1:
                drow = -1
            if x2 < x1:
                dcol = -1

            col = x1
            for row in range(y1, y2 + drow, drow):
                diagram[row][col] += 1
                col += dcol

    # Calculating the number of points where at least two lines overlap
    count = 0
    for row in diagram:
        for point in row:
            if point >= 2:
                count += 1
    return count


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
