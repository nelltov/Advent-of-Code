import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[List[int]]:
    """Parse input -- the energy level of each octopus"""
    result = puzzle_input_str.splitlines()
    result = [[int(energy) for energy in result[i]] for i in range(len(result))]
    return result


def part1(data: List[List[int]]) -> int:
    """Solve part 1 -- How many total flashes are there after 100 steps? """
    total_flashes = 0
    steps = 100

    rows = len(data)
    cols = len(data[0])
    part1_data = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            part1_data[row][col] = data[row][col]

    for _ in range(steps):  # change this to 100
        to_flash = []
        flashed = []

        for row in range(rows):
            for col in range(cols):
                part1_data[row][col] += 1
                if part1_data[row][col] > 9:
                    to_flash += [(row, col)]

        # completing flashes if needed
        if len(to_flash) > 0:
            while len(to_flash) != len(flashed):
                # going through the rows and columns that still need to flash
                for r, c in to_flash:
                    if (r, c) not in flashed:
                        for dr in [-1, 0, 1]:  # going through adjacent rows and columns
                            for dc in [-1, 0, 1]:
                                if dr != 0 or dc != 0:
                                    new_r = r + dr
                                    new_c = c + dc
                                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in to_flash:
                                        part1_data[new_r][new_c] += 1
                                        if part1_data[new_r][new_c] > 9:
                                            to_flash += [(new_r, new_c)]

                        flashed += [(r, c)]

        # setting energy of octopi that flashed to 0
        if len(flashed) > 0:
            for r, c in flashed:
                part1_data[r][c] = 0

        total_flashes += len(flashed)

    return total_flashes


def part2(data):
    """Solve part 2 -- What is the first step during which all octopuses flash?"""
    rows = len(data)
    cols = len(data[0])
    part2_data = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            part2_data[row][col] = data[row][col]

    step = 0

    while True:
        step += 1
        to_flash = []
        flashed = []

        for row in range(rows):
            for col in range(cols):
                part2_data[row][col] += 1
                if part2_data[row][col] > 9:
                    to_flash += [(row, col)]

        # completing flashes if needed
        if len(to_flash) > 0:
            while len(to_flash) != len(flashed):
                # going through the rows and columns that still need to flash
                for r, c in to_flash:
                    if (r, c) not in flashed:
                        for dr in [-1, 0, 1]:  # going through adjacent rows and columns
                            for dc in [-1, 0, 1]:
                                if dr != 0 or dc != 0:
                                    new_r = r + dr
                                    new_c = c + dc
                                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in to_flash:
                                        part2_data[new_r][new_c] += 1
                                        if part2_data[new_r][new_c] > 9:
                                            to_flash += [(new_r, new_c)]

                        flashed += [(r, c)]

        # setting energy of octopi that flashed to 0
        if len(flashed) > 0:
            for r, c in flashed:
                part2_data[r][c] = 0

        # returning when all the octopi flash at the same time
        if len(flashed) == rows * cols:
            return step


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
