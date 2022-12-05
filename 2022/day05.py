import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str):
    """Parse input -- starting stacks of crates and the rearrangement procedure"""
    moves = ((puzzle_input_str.split("\n\n"))[1]).splitlines()
    dirs = list(map(lambda s: s.split(" "), moves))
    return list(map(lambda l: (int(l[1]), int(l[3]), int(l[5])), dirs))


init_stack = [['D', 'B', 'J', 'V'],
              ['P', 'V', 'B', 'W', 'R', 'D', 'F'],
              ['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q'],
              ['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B'],
              ['H', 'N', 'B', 'P', 'C', 'S', 'Q'],
              ['R', 'D', 'B', 'S', 'N', 'G'],
              ['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H'],
              ['W', 'L', 'F'],
              ['S', 'V', 'F', 'M', 'R']]


def part1(data) -> str:
    """Solve part 1 -- After the rearrangement procedure completes, what crate ends up on top of each stack?"""
    cur_stack = init_stack
    for (n, s, d) in data:
        for _ in range(n):
            cur_src = cur_stack[s - 1]
            cur_val = cur_src.pop()
            (cur_stack[d - 1]).append(cur_val)
    res = ""
    for st in cur_stack:
        res += st[-1]
    return res


init_stack2 = [['D', 'B', 'J', 'V'],
              ['P', 'V', 'B', 'W', 'R', 'D', 'F'],
              ['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q'],
              ['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B'],
              ['H', 'N', 'B', 'P', 'C', 'S', 'Q'],
              ['R', 'D', 'B', 'S', 'N', 'G'],
              ['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H'],
              ['W', 'L', 'F'],
              ['S', 'V', 'F', 'M', 'R']]


def part2(data) -> str:
    """Solve part 2 -- After the rearrangement procedure completes, what crate ends up on top of each stack?"""
    cur_stack = init_stack2
    for (n, s, d) in data:
        cur_src = cur_stack[s - 1]
        cur_arr = cur_src[-n:]
        cur_stack[s - 1] = cur_src[:-n]
        cur_stack[d - 1] += cur_arr
    res = ""
    for st in cur_stack:
        res += st[-1]
    return res


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
