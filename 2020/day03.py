import pathlib
import sys
from typing import List


def parse(puzzle_input_str):
    """Parse input -- map of the open squares (.) and trees (#) you can see"""
    return puzzle_input_str.splitlines()


def part1(data):
    """Solve part 1 -- Starting at the top-left corner of your map and following a slope of right 3 and down 1,
    how many trees would you encounter?"""
    tree_count = 0
    num_cols = len(data[0])
    col = 0
    for row in data[1:]:
        col = (col + 3) % num_cols
        if row[col] == "#":
            tree_count += 1
    return tree_count


def part2(data):
    """Solve part 2 -- What do you get if you multiply together the number of trees
    encountered on each of the listed slopes?"""
    slope1_treecount = 0
    slope2_treecount = part1(data)
    slope3_treecount = 0
    slope4_treecount = 0
    slope5_treecount = 0

    num_cols = len(data[0])
    col1 = 0
    col3 = 0
    col4 = 0
    col5 = 0
    for row_idx in range(1, len(data)):
        col1 = (col1 + 1) % num_cols
        if data[row_idx][col1] == "#":
            slope1_treecount += 1

        col3 = (col3 + 5) % num_cols
        if data[row_idx][col3] == "#":
            slope3_treecount += 1

        col4 = (col4 + 7) % num_cols
        if data[row_idx][col4] == "#":
            slope4_treecount += 1

        if row_idx % 2 == 0:
            col5 = (col5 + 1) % num_cols
            if data[row_idx][col5] == "#":
                slope5_treecount += 1

    return slope1_treecount * slope2_treecount * slope3_treecount * slope4_treecount * slope5_treecount


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
