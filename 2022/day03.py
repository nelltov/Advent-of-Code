import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- list of contents from all rucksacks """
    return puzzle_input_str.splitlines()


def part1(data: List[str]) -> int:
    """Solve part 1 -- Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?"""
    priority_sum = 0
    for rucksack in data:
        n = len(rucksack)
        r1 = rucksack[:(n//2)]
        r2 = rucksack[(n//2):]
        item = (list((set(r1)).intersection(set(r2))))[0]
        if item.islower():
            priority_sum += ord(item) - 96
        else:
            priority_sum += ord(item) - 38
    return priority_sum


def part2(data: List[str]) -> int:
    """Solve part 2 -- Find the item type that corresponds to the badges of each three-Elf group.
    What is the sum of the priorities of those item types? """
    priority_sum = 0
    for i in range(0, len(data), 3):
        r1 = data[i]
        r2 = data[i + 1]
        r3 = data[i + 2]
        item = (list((set(r1)).intersection((set(r2)).intersection(set(r3)))))[0]
        if item.islower():
            priority_sum += ord(item) - 96
        else:
            priority_sum += ord(item) - 38
    return priority_sum

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

