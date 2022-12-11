import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[List[int]]:
    """Parse input -- a map with the height of each tree"""
    return [(list(map(lambda el: int(el), list(row)))) for row in puzzle_input_str.splitlines()]


def part1(data: List[List[int]]) -> int:
    """Solve part 1 -- Consider your map; how many trees are visible from outside the grid?"""
    rows = len(data)
    cols = len(data[0])
    bool_mat = [[False for _ in range(cols)] for _ in range(rows)]

    # set the outer rows and columns
    for r in range(rows):
        bool_mat[r][0] = True
        bool_mat[r][-1] = True
    for c in range(cols):
        bool_mat[0][c] = True
        bool_mat[-1][c] = True

    # check from the left and right
    for r in range(1, rows - 1):
        l_max = data[r][0]
        for c in range(1, cols - 1):
            if data[r][c] > l_max:
                l_max = data[r][c]
                bool_mat[r][c] = True
        r_max = data[r][-1]
        for c in range(cols - 2, -1, -1):
            if data[r][c] > r_max:
                r_max = data[r][c]
                bool_mat[r][c] = True

    # check from the top and bottom
    for c in range(1, cols - 1):
        t_max = data[0][c]
        for r in range(1, rows - 1):
            if data[r][c] > t_max:
                t_max = data[r][c]
                bool_mat[r][c] = True
        b_max = data[-1][c]
        for r in range(rows - 2, -1, -1):
            if data[r][c] > b_max:
                b_max = data[r][c]
                bool_mat[r][c] = True

    res = 0
    for r in range(rows):
        for c in range(cols):
            if bool_mat[r][c]:
                res += 1

    return res


def part2(data: List[List[int]]) -> int:
    """Solve part 2 -- Consider each tree on your map.
    What is the highest scenic score possible for any tree?"""
    rows = len(data)
    cols = len(data[0])
    score_mat = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            t_dist = 0  # top distance
            for r1 in range(r - 1, -1, -1):
                t_dist += 1
                if data[r1][c] >= data[r][c]:
                    break
            l_dist = 0  # left distance
            for c1 in range(c - 1, -1, -1):
                l_dist += 1
                if data[r][c1] >= data[r][c]:
                    break
            b_dist = 0  # bottom distance
            for r1 in range(r + 1, rows):
                b_dist += 1
                if data[r1][c] >= data[r][c]:
                    break
            r_dist = 0  # right distance
            for c1 in range(c + 1, cols):
                r_dist += 1
                if data[r][c1] >= data[r][c]:
                    break
            score_mat[r][c] = t_dist * l_dist * b_dist * r_dist

    return max(list(map(lambda mr: max(mr), score_mat)))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

