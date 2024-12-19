import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[List[str]]:
    return [list(elem) for elem in puzzle_input_str.splitlines()]


def part1(data: List[List[str]]) -> int:
    """Solve part 1 -- Take a look at the little Elf's word search. How many times does XMAS appear?"""
    xmas_count = 0
    rows = len(data)
    cols = len(data[0])

    for row in range(rows):
        for col in range(cols):
            cur_letter = data[row][col]

            if cur_letter != "X":
                continue

            for (diff_row, diff_col) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                max_row = row + (3 * diff_row)
                max_col = col + (3 * diff_col)

                if 0 <= max_row < rows and 0 <= max_col < cols and \
                        data[row + diff_row][col + diff_col] == "M" and \
                        data[row + (2 * diff_row)][col + (2 * diff_col)] == "A" and \
                        data[max_row][max_col] == "S":
                    xmas_count += 1

    return xmas_count


def part2(data: List[List[str]]) -> int:
    """Solve part 2 --- You're supposed to find two MAS in the shape of an X. How many times does an X-MAS appear?"""
    xmas_count = 0
    rows = len(data)
    cols = len(data[0])

    for row in range(rows):
        for col in range(cols):
            cur_letter = data[row][col]

            if cur_letter != "A":
                continue

            if 1 <= row < rows - 1 and 1 <= col < cols - 1 and \
                    (data[row - 1][col - 1] == "M" and data[row + 1][col + 1] == "S" or
                     data[row - 1][col - 1] == "S" and data[row + 1][col + 1] == "M") and \
                    (data[row - 1][col + 1] == "M" and data[row + 1][col - 1] == "S" or
                     data[row - 1][col + 1] == "S" and data[row + 1][col - 1] == "M"):
                xmas_count += 1

    return xmas_count


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
