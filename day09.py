import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[List[int]]:
    """Parse input -- heightmap of the floor of the nearby caves for you"""
    rows = puzzle_input_str.splitlines()
    data = [[int(num) for num in row] for row in rows]
    return data


def part1(data: List[List[int]]) -> int:
    """Solve part 1 -- Find all of the low points on your heightmap.
    What is the sum of the risk levels of all low points on your heightmap?"""
    rows = len(data)
    cols = len(data[0])
    risk_level_sum = 0
    for row in range(rows):
        for col in range(cols):
            is_lowpoint = True
            if (row > 0 and data[row][col] >= data[row - 1][col]) \
                    or (col > 0 and data[row][col] >= data[row][col - 1]) \
                    or (row < rows - 1 and data[row][col] >= data[row + 1][col]) \
                    or (col < cols - 1 and data[row][col] >= data[row][col + 1]):
                is_lowpoint = False

            if is_lowpoint:
                risk_level_sum += data[row][col] + 1

    return risk_level_sum


def calculate_basin_size(row: int, col: int, marked_table: List[List[int]], data: List[List[int]]):
    rows = len(data)
    cols = len(data[0])

    # checking that cell is in range and that it is not already counted or a basin boundary
    if row < 0 or row >= rows or col < 0 or col >= cols or marked_table[row][col] != -1:
        return 0, marked_table

    else:
        marked_table[row][col] = 1  # marking the current cell as counted
        left, marked_table = calculate_basin_size(row, col - 1, marked_table, data)
        right, marked_table = calculate_basin_size(row, col + 1, marked_table, data)
        up, marked_table = calculate_basin_size(row - 1, col, marked_table, data)
        down, marked_table = calculate_basin_size(row + 1, col, marked_table, data)
        return 1 + left + right + up + down, marked_table


def part2(data: List[List[int]]) -> int:
    """Solve part 2 -- What do you get if you multiply together the sizes of the three largest basins?"""

    basin_sizes = []
    rows = len(data)
    cols = len(data[0])

    marked_table = [[-1 for _ in range(cols)] for _ in range(rows)]

    # mark all locations of height 9 as not part of any basin
    for row in range(rows):
        for col in range(cols):
            if data[row][col] == 9:
                marked_table[row][col] = 0

    # for any non-traversed basin, calculate its size and add it to the list of basin sizes
    for row in range(rows):
        for col in range(cols):
            if marked_table[row][col] == -1:
                basin_size, marked_table = calculate_basin_size(row, col, marked_table, data)
                basin_sizes += [basin_size]

    if len(basin_sizes) < 3:
        return 0
    basin_sizes.sort()
    basin_sizes.reverse()
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
