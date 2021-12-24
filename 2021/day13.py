import pathlib
import sys
from typing import List


def parse(puzzle_input_str):
    """Parse input --the transparent paper marked with random dots and including instructions on how to fold it up"""
    return puzzle_input_str.split("\n\n")[0], puzzle_input_str.split("\n\n")[1]


def fold_up(paper, line: int):
    cols = len(paper[0])
    rows = len(paper)

    folded_paper = [["."] * cols for _ in range(line)]

    for r in range(rows):
        for c in range(cols):
            if paper[r][c] == "#":
                if r < line:
                    folded_paper[r][c] = "#"
                elif r > line:
                    folded_paper[(2 * line) - r][c] = "#"

    return folded_paper


def fold_left(paper, line):
    cols = len(paper[0])
    rows = len(paper)

    folded_paper = [["."] * line for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if paper[r][c] == "#":
                if c < line:
                    folded_paper[r][c] = "#"
                elif c > line:
                    folded_paper[r][(2 * line) - c] = "#"

    return folded_paper


def part1(data):
    """Solve part 1 -- How many dots are visible
    after completing just the first fold instruction on your transparent paper? """
    dots, fold_instructions = data
    fold_dir = fold_instructions.splitlines()[0].split()[2].split("=")[0]
    fold_line = fold_instructions.splitlines()[0].split()[2].split("=")[1]

    x_cds = []
    y_cds = []
    for cd in dots.splitlines():
        x_cds += [int(cd.split(",")[0])]
        y_cds += [int(cd.split(",")[1])]

    max_rows = max(y_cds) + 1
    max_cols = max(x_cds) + 1

    transparent_paper = [["."] * max_cols for _ in range(max_rows)]

    for i in range(len(x_cds)):
        transparent_paper[y_cds[i]][x_cds[i]] = "#"

    if fold_dir == 'x':
        folded_paper = fold_left(transparent_paper, int(fold_line))
    else:
        folded_paper = fold_up(transparent_paper, int(fold_line))

    visible_dots = 0
    for row in range(len(folded_paper)):
        for col in range(len(folded_paper[0])):
            if folded_paper[row][col] == "#":
                visible_dots += 1

    return visible_dots


def part2(data):
    """Solve part 2 -- Finish folding the transparent paper according to the instructions.
    The manual says the code is always eight capital letters.
    What code do you use to activate the infrared thermal imaging camera system?"""
    dots, fold_instructions = data

    x_cds = []
    y_cds = []
    for cd in dots.splitlines():
        x_cds += [int(cd.split(",")[0])]
        y_cds += [int(cd.split(",")[1])]

    max_rows = max(y_cds) + 1
    max_cols = max(x_cds) + 1

    transparent_paper = [["."] * max_cols for _ in range(max_rows)]

    for i in range(len(x_cds)):
        transparent_paper[y_cds[i]][x_cds[i]] = "#"

    folded_paper = transparent_paper
    fold_directions = fold_instructions.splitlines()
    for direction in fold_directions:
        fold_dir = direction.split()[2].split("=")[0]
        fold_line = direction.split()[2].split("=")[1]

        if fold_dir == 'x':
            folded_paper = fold_left(folded_paper, int(fold_line))
        else:
            folded_paper = fold_up(folded_paper, int(fold_line))

    for row in folded_paper:
        print(row)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
