import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    return puzzle_input_str.splitlines()


def part1(data: List[str]) -> int:
    total_worth = 0

    for card in data:
        winning_numbers = set([int(x) for x in card.split(" | ")[0].split(": ")[1].strip().replace("  ", " ").split(" ")])
        numbers_had = [int(x) for x in card.split(" | ")[1].strip().replace("  ", " ").split(" ")]
        winning_numbers_had = 0

        for number in numbers_had:
            if number in winning_numbers:
                winning_numbers_had += 1

        if winning_numbers_had > 0:
            total_worth += 2 ** (winning_numbers_had - 1)

    return total_worth


def part2(data: List[str]) -> int:
    scratchcard_copies = dict()
    for i in range(1, len(data) + 1):
        scratchcard_copies[i] = 1

    card_number = 1
    for card in data:
        winning_numbers = set([int(x) for x in card.split(" | ")[0].split(": ")[1].strip().replace("  ", " ").split(" ")])
        numbers_had = [int(x) for x in card.split(" | ")[1].strip().replace("  ", " ").split(" ")]
        winning_numbers_had = 0

        for number in numbers_had:
            if number in winning_numbers:
                winning_numbers_had += 1

        if winning_numbers_had > 0:
            for i in range(winning_numbers_had):
                scratchcard_copies[card_number + i + 1] += scratchcard_copies[card_number]

        card_number += 1

    return sum(scratchcard_copies.values())


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

