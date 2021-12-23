import pathlib
import sys
from typing import List


def parse(puzzle_input_str):
    """Parse input -- list of passwords and the corporate policy when that password was set."""
    lines = puzzle_input_str.splitlines()
    result = []
    for line in lines:
        [count_limits, letter, password] = line.split()
        [min_count, max_count] = count_limits.split('-')
        result += [[min_count, max_count, letter[0], password]]
    return result


def part1(data):
    """Solve part 1 -- How many passwords are valid according to their policies?"""
    valid_count = 0
    for [min_count, max_count, letter, password] in data:
        if int(min_count) <= password.count(letter) <= int(max_count):
            valid_count += 1
    return valid_count


def part2(data):
    """Solve part 2 -- How many passwords are valid according to the new interpretation of the policies?"""
    valid_count = 0
    for [first_pos, second_pos, letter, password] in data:
        first_pos_letter = password[int(first_pos) - 1]
        second_pos_letter = password[int(second_pos) - 1]
        if first_pos_letter != second_pos_letter and (first_pos_letter == letter or second_pos_letter == letter):
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
