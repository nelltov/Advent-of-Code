import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> str:
    """Parse input -- datastream buffer"""
    return puzzle_input_str


def part1(data: str) -> int:
    """Solve part 1 -- How many characters need to be processed before the first start-of-packet marker is detected?"""
    if len(data) < 4:
        return 0
    c1, c2, c3, c4 = data[0], data[1], data[2], data[3]
    if len(list({c1, c2, c3, c4})) == 4:
        return 4
    for i in range(4, len(data)):
        c1, c2, c3, c4 = c2, c3, c4, data[i]
        if len(list({c1, c2, c3, c4})) == 4:
            return i + 1
    return len(data)


def part2(data: str) -> int:
    """Solve part 2 -- How many characters need to be processed before the first start-of-message marker is detected?"""
    if len(data) < 14:
        return 0
    message = data[:14]
    if len(list(set(message))) == 14:
        return 14
    for i in range(14, len(data)):
        message = message[1:] + data[i]
        if len(list(set(message))) == 14:
            return i + 1
    return len(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

