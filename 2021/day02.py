import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- list of commands and units"""
    return puzzle_input_str.splitlines()


def part1(data: List[str]) -> int:
    """Solve part 1 -- Calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth"""
    horizontal_pos = 0
    depth = 0

    if len(data) <= 1:
        return 0

    for instruction in data:
        [command, units] = instruction.split()
        if command == 'forward':
            horizontal_pos += int(units)
        elif command == 'down':
            depth += int(units)
        elif command == 'up':
            depth -= int(units)

    return horizontal_pos * depth


def part2(data):
    """Solve part 2 -- Using a new interpretation of the commands,
    calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth?"""
    horizontal_pos = 0
    depth = 0
    aim = 0

    if len(data) <= 1:
        return 0

    for instruction in data:
        [command, units] = instruction.split()
        if command == 'forward':
            horizontal_pos += int(units)
            depth += aim * int(units)
        elif command == 'down':
            aim += int(units)
        elif command == 'up':
            aim -= int(units)

    return horizontal_pos * depth


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

