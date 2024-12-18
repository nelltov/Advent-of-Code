import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- """
    return puzzle_input_str.splitlines()


def helper(data: List[str]) -> bool:
    increasing = True if int(data[1]) > int(data[0]) else False
    safe = True
    for i in range(len(data) - 1):
        current_level = int(data[i])
        next_level = int(data[i + 1])
        if (increasing and (next_level - current_level < 1) or (next_level - current_level > 3)) \
            or (not increasing and (current_level - next_level < 1) or (current_level - next_level > 3)):
            safe = False
            break

    return safe


def part1(data: List[str]) -> int:
    """Solve part 1 -- """
    safe_reports = 0
    for report in data:
        levels = report.split(" ")
        safe = helper(levels)
        if safe:
            safe_reports += 1

    return safe_reports


def part2(data: List[str]) -> int:
    """Solve part 2 -- """
    safe_reports = 0
    for report in data:
        levels = report.split(" ")

        safe = helper(levels)

        if not safe:
            for j in range(len(levels)):
                new_list = levels.copy()
                new_list.pop(j)
                current_variation_safe = helper(new_list)

                if current_variation_safe:
                    safe = True
                    break

        if safe:
            safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")



