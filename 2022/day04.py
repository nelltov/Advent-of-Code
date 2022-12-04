import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- list of the section assignments for each pair"""
    return puzzle_input_str.splitlines()


def part1(data: List[str]) -> int:
    """Solve part 1 -- In how many assignment pairs does one range fully contain the other?"""
    count = 0
    for pair in data:
        e1e2 = pair.split(",")
        e1, e2 = e1e2[0], e1e2[1]
        e1range = e1.split("-")
        e2range = e2.split("-")
        e11, e12 = int(e1range[0]), int(e1range[1])
        e21, e22 = int(e2range[0]), int(e2range[1])
        if (e11 <= e21 and e22 <= e12) or (e21 <= e11 and e12 <= e22):
            count += 1
    return count


def part2(data: List[str]) -> int:
    """Solve part 2 -- In how many assignment pairs do the ranges overlap?"""
    count = 0
    for pair in data:
        e1e2 = pair.split(",")
        e1, e2 = e1e2[0], e1e2[1]
        e1range = e1.split("-")
        e2range = e2.split("-")
        e11, e12 = int(e1range[0]), int(e1range[1])
        e21, e22 = int(e2range[0]), int(e2range[1])
        if e11 <= e21 <= e12 or e11 <= e22 <= e12 or e21 <= e11 <= e22 or e21 <= e12 <= e22:
            count += 1
    return count

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")