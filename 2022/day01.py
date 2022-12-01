import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- lists of each elf's list of calories"""
    return list(map(lambda s: s.split(), puzzle_input_str.split("\n\n")))


def part1(data: List[str]) -> int:
    """Solve part 1 -- how many Calories are being carried by the Elf carrying the most Calories """
    return max(list(map(lambda l: sum(list(map(lambda s: int(s), l))), data)))


def part2(data: List[str]) -> int:
    """Solve part 2 -- the sum of the Calories being carried by the three Elves carrying the most Calories"""
    totals = list(map(lambda l: sum(list(map(lambda s: int(s), l))), data))
    max1 = max(totals)
    totals.remove(max1)
    max2 = max(totals)
    totals.remove(max2)
    max3 = max(totals)
    return max1 + max2 + max3


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

