import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- list of depth measurements"""
    return puzzle_input_str.split()


def part1(data: List[str]) -> int:
    """Solve part 1 -- count the number of times a depth measurement increases from the previous measurement"""
    count: int = 0
    if len(data) <= 1:
        return count

    previous: str = data[0]
    for measurement in data[1:]:
        if int(measurement) > int(previous):
            count += 1
        previous = measurement

    return count


def part2(data: List[str]) -> int:
    """Solve part 2 -- count how many times the sum of measurements in sliding window increases from previous sum"""
    count: int = 0
    if len(data) <= 4:
        return count

    previous: int = int(data[0]) + int(data[1]) + int(data[2])
    for i in range(1, len(data) - 2):
        measurement_sum = int(data[i]) + int(data[i + 1]) + int(data[i + 2])
        if measurement_sum > previous:
            count += 1
        previous = measurement_sum

    return count


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

