import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[tuple[str, int]]:
    """Parse input -- hypothetical series of motions"""
    return list(((s.split(" "))[0], int((s.split(" "))[1])) for s in puzzle_input_str.splitlines())


def move_tail(direction, h_pos, t_pos):
    hx, hy = h_pos
    tx, ty = t_pos
    ohx, ohy = h_pos
    match direction:
        case "U":
            dx, dy = 0, 1
        case "R":
            dx, dy = 1, 0
        case "D":
            dx, dy = 0, -1
        case "L":
            dx, dy = -1, 0
        case _:
            dx, dy = 0, 0
    hx += dx
    hy += dy
    if abs(hx - tx) > 1 or abs(hy - ty) > 1:  # need to move tail
        tx, ty = ohx, ohy
    return (hx, hy), (tx, ty)


def part1(data: List[tuple[str, int]]) -> int:
    """Solve part 1 -- Simulate your complete hypothetical series of motions.
    How many positions does the tail of the rope visit at least once?"""
    h_pos, t_pos = (0, 0), (0, 0)
    t_pos_set = {(0, 0)}
    for (direction, steps) in data:
        for i in range(steps):
            h_pos, t_pos = move_tail(direction, h_pos, t_pos)
            t_pos_set.add(t_pos)
    return len(t_pos_set)


def part2(data: List[tuple[str, int]]) -> int:
    """Solve part 2 -- Simulate your complete series of motions on a larger rope with ten knots.
    How many positions does the tail of the rope visit at least once?"""
    knots_pos = [(0, 0) for _ in range(10)]
    t_pos_set = {(0, 0)}
    for (direction, steps) in data:
        for i in range(steps):
            print(i)
            # moving the head and the first knot
            (ohx, ohy) = knots_pos[1]
            knots_pos[0], knots_pos[1] = move_tail(direction, knots_pos[0], knots_pos[1])
            # moving all the subsequent knots
            for j in range(2, 10):
                (hx, hy), (tx, ty) = knots_pos[j-1], knots_pos[j]
                print((ohx, ohy), (hx, hy), (tx, ty))
                if abs(hx - tx) > 1 or abs(hy - ty) > 1:  # need to move tail
                    (n_ohx, n_ohy) = knots_pos[j]
                    knots_pos[j] = (ohx, ohy)
                    (ohx, ohy) = (n_ohx, n_ohy)
                else:
                    break
            t_pos_set.add(knots_pos[-1])
            print(knots_pos)
    return len(t_pos_set)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
