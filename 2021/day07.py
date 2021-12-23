import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[int]:
    """Parse input -- the horizontal position of each crab"""
    str_list = puzzle_input_str.split(',')
    result = []
    for pos in str_list:
        result += [int(pos)]
    return result


def part1(data: List[int]) -> int:
    """Solve part 1 -- Determine the horizontal position that the crabs can align to using the least fuel possible.
    How much fuel must they spend to align to that position?"""
    min_fuel_cost = None
    for pos in range(min(data), max(data)):
        cur_fuel_cost = 0
        for i in range(len(data)):
            cur_fuel_cost += abs(data[i] - pos)
            if min_fuel_cost is not None and cur_fuel_cost > min_fuel_cost:
                break

        if min_fuel_cost is None or cur_fuel_cost < min_fuel_cost:
            min_fuel_cost = cur_fuel_cost

    return min_fuel_cost


def part2(data: List[int]) -> int:
    """Solve part 2 -- Determine the horizontal position that the crabs can align to using the least fuel possible
    so they can make you an escape route! How much fuel must they spend to align to that position?"""
    min_fuel_cost = None
    for pos in range(min(data), max(data)):
        cur_fuel_cost = 0
        for i in range(len(data)):
            n = abs(int(data[i]) - int(pos))
            cur_fuel_cost += (n * (n + 1)) // 2
            if min_fuel_cost is not None and cur_fuel_cost > min_fuel_cost:
                break

        if min_fuel_cost is None or cur_fuel_cost < min_fuel_cost:
            min_fuel_cost = cur_fuel_cost

    return min_fuel_cost


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
