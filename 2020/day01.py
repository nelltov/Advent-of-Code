import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[int]:
    """Parse input -- expense report"""
    data_str = puzzle_input_str.splitlines()
    result = []
    for num in data_str:
        result += [int(num)]
    return result


def part1(data: List[int]) -> int:
    """Solve part 1 -- Find the two entries that sum to 2020; what do you get if you multiply them together?"""
    dataset = set(data)
    for entry in dataset:
        difference = 2020 - entry
        if difference in dataset:
            return entry * difference


def part2(data: List[int]) -> int:
    """Solve part 2 -- what is the product of the three entries that sum to 2020?"""
    for i in range(len(data) - 2):
        partial_sum = 2020 - data[i]
        for j in range(i + 1, len(data)):
            difference = partial_sum - data[j]
            if difference in data[j + 1:]:
                return data[i] * data[j] * difference


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
