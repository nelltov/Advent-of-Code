import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> list[list[str]]:
    """Parse input -- """
    return [[c for c in line] for line in puzzle_input_str.splitlines()]


def part1(data: list[list[str]]) -> int:
    """Solve part 1 -- What is the sum of all of the part numbers in the engine schematic? """
    part_number_sum = 0
    rows = len(data)
    cols = len(data[0])

    current_number = 0
    is_part_number = False

    for row in range(rows):
        # account for any number that was at the end of the previous row and needs to be counted
        if current_number != 0 and is_part_number:
            part_number_sum += current_number

        # reset the number at the start of each row
        current_number = 0
        is_part_number = False

        for col in range(cols):
            cur_symbol = data[row][col]

            # hit the end of the current number being evaluated, add it to sum if needed and reset
            if not cur_symbol.isdigit():
                if is_part_number:
                    part_number_sum += current_number

                current_number = 0
                is_part_number = False

            # hit a digit, tack on to the current digit being evaluated
            else:
                current_number = (current_number * 10) + int(cur_symbol)

                # check if there are any new symbols being added by this new number to make it a part number
                if not is_part_number:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if 0 < row + dy < rows and 0 < col + dx < cols \
                                    and not data[row + dy][col + dx].isdigit() and data[row + dy][col + dx] != ".":
                                is_part_number = True

    # account for any number that was at the end of the whole table and needs to be counted
    if current_number != 0 and is_part_number:
        part_number_sum += current_number

    return part_number_sum


def part2(data: List[str]) -> int:
    """Solve part 2 -- What is the sum of all of the gear ratios in your engine schematic? """
    gear_ratio_sum = 0
    rows = len(data)
    cols = len(data[0])

    for row in range(rows):
        for col in range(cols):
            if data[row][col] != "*":
                continue

            # figure out if it's a gear (adjacent to exactly two part numbers)
            gear_coords = []

            # left number
            if 0 < col and data[row][col - 1].isdigit():
                gear_coords.append((-1, 0))

            # right number
            if col < cols - 1 and data[row][col + 1].isdigit():
                gear_coords.append((1, 0))

            # up number
            if 0 < row:
                if data[row - 1][col].isdigit():
                    gear_coords.append((0, -1))
                else:
                    if 0 < col and data[row - 1][col - 1].isdigit():
                        gear_coords.append((-1, -1))
                    if col < cols - 1 and data[row - 1][col + 1].isdigit():
                        gear_coords.append((1, -1))

            # down number
            if row < rows:
                if data[row + 1][col].isdigit():
                    gear_coords.append((0, 1))
                else:
                    if 0 < col and data[row + 1][col - 1].isdigit():
                        gear_coords.append((-1, 1))
                    if col < cols - 1 and data[row + 1][col + 1].isdigit():
                        gear_coords.append((1, 1))

            if len(gear_coords) != 2:  # make sure it is exactly two adjacent and ignore otherwise
                continue

            # find the full part numbers that are adjacent to the gear and multiply them
            gear_ratio = 1
            for (dx, dy) in gear_coords:
                start_row = row + dy
                start_col = col + dx
                while start_col > 0 and data[start_row][start_col - 1].isdigit():
                    start_col -= 1  # move left until the first digit of the number

                # build up the entire part number from left to right
                current_part_number = 0
                while start_col < cols and data[start_row][start_col].isdigit():
                    current_part_number = (current_part_number * 10) + int(data[start_row][start_col])
                    start_col += 1

                gear_ratio *= current_part_number   # multiply the part numbers together

            gear_ratio_sum += gear_ratio            # add current gear ratio to the accumulator sum

    return gear_ratio_sum


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
