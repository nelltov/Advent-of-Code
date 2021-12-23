import pathlib
import sys
from typing import List


def parse(puzzle_input_str):
    """Parse input -- map of the caves"""
    result = dict()
    map_lines = puzzle_input_str.splitlines()
    for line in map_lines:
        start, end = line.split("-")[0], line.split("-")[1]

        if start not in result:
            result[start] = []
        if end not in result:
            result[end] = []

        result[start] += [end]
        result[end] += [start]

    return result


def part1(data):
    """ Solve part 1 -- How many paths through this cave system are there that visit small caves at most once? """


def part2(data):
    """Solve part 2 -- """


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(puzzle_data)
        # print(f"solution 1: {part1(puzzle_data)}")
        # print(f"solution 2: {part2(puzzle_data)}")
