import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[int]:
    """Parse input -- list of the ages of nearby lanternfish"""
    data_str = puzzle_input_str.split(',')
    result = []
    for num in data_str:
        result += [int(num)]

    return result


def part1(data: List[int]) -> int:
    """Solve part 1 -- Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?"""
    current_state = [0 for _ in range(9)]
    for num in data:
        current_state[num] += 1

    for _ in range(80):
        previous_zero = current_state[0]
        for i in range(8):
            # shifting all the internal timers down by 1
            current_state[i] = current_state[i + 1]

        # creating the new lanternfish
        current_state[8] = previous_zero

        # resetting the timers of fish that were at 0
        current_state[6] += previous_zero

    return sum(current_state)


def part2(data: List[int]) -> int:
    """Solve part 2 -- How many lanternfish would there be after 256 days?"""
    current_state = [0 for _ in range(9)]
    for num in data:
        current_state[num] += 1

    for _ in range(256):
        previous_zero = current_state[0]
        for i in range(8):
            # shifting all the internal timers down by 1
            current_state[i] = current_state[i + 1]

        # creating the new lanternfish
        current_state[8] = previous_zero

        # resetting the timers of fish that were at 0
        current_state[6] += previous_zero

    return sum(current_state)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
