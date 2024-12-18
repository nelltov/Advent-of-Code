import pathlib
import sys
from typing import List
import re


def parse(puzzle_input_str: str) -> str:
    return puzzle_input_str


def part1(data: str) -> int:
    """Solve part 1 -- Scan the corrupted memory for uncorrupted mul instructions.
    What do you get if you add up all the results of the multiplications?"""
    result = 0
    re_pattern = r"mul\(\d\d?\d?,\d\d?\d?\)"
    mul_list = re.findall(re_pattern, data)
    for instruction in mul_list:
        xy_pair = instruction[4:-1].split(",")
        x = xy_pair[0]
        y = xy_pair[1]
        result += (int(x) * int(y))

    return result


def part2(data):
    """Solve part 2 -- Handle the new instructions;
    what do you get if you add up all the results of just the enabled multiplications?"""
    enabled = True
    result = 0
    re_pattern = r"mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\)"
    instruction_list = re.findall(re_pattern, data)
    for instruction in instruction_list:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            xy_pair = instruction[4:-1].split(",")
            x = xy_pair[0]
            y = xy_pair[1]
            result += (int(x) * int(y))

    return result

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")



