import pathlib
import sys
from typing import List, Tuple
from collections import defaultdict


def parse(puzzle_input_str: str) -> Tuple[List[int], List[int]]:
    """Parse input -- Returning a tuple of the two lists """
    res_left = []
    res_right = []

    for line in puzzle_input_str.splitlines():
        cur_line = line.split("   ")
        res_left.append(int(cur_line[0]))
        res_right.append(int(cur_line[1]))

    return res_left, res_right


def part1(data: Tuple[List[int], List[int]]) -> int:
    """ Solve part 1 -- Pair up the numbers and measure how far apart they are.
    Pair up the smallest number in the left list with the smallest number in the right list,
    then the second-smallest left number with the second-smallest right number, and so on.
    Within each pair, figure out how far apart the two numbers are; add up all of those distances."""
    list_left, list_right = data
    list_left.sort()
    list_right.sort()

    distance = 0
    for i in range(len(list_left)):
        distance += abs(list_left[i] - list_right[i])

    return distance


def part2(data: Tuple[List[int], List[int]]) -> int:
    """Solve part 2 -- Calculate a total similarity score by adding up each number in the left list
    after multiplying it by the number of times that number appears in the right list."""
    list_left, list_right = data
    right_list_dict = defaultdict(int)
    for i in range(len(list_right)):
        right_list_dict[list_right[i]] += 1

    similarity_score = 0
    for i in range(len(list_left)):
        similarity_score += list_left[i] * right_list_dict[list_left[i]]

    return similarity_score


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

