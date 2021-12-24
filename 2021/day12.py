import pathlib
import sys
from typing import List, Optional

small_caves = set()


def parse(puzzle_input_str):
    """Parse input -- map of the caves"""
    result = dict()
    map_lines = puzzle_input_str.splitlines()
    for line in map_lines:
        start, end = line.split("-")[0], line.split("-")[1]

        if start not in result:
            result[start] = []
        if end not in result:
            result[end] = []

        result[start] += [end]
        result[end] += [start]

        # Finding the small caves
        if start.islower():
            small_caves.add(start)
        if end.islower():
            small_caves.add(end)

    return result


def count_valid_paths(path_dict, current_path: List[str], cave: str):
    """ part1 helper function """
    if cave == 'end':
        return 1
    paths = 0
    for next_cave in path_dict[cave]:
        if next_cave not in small_caves or next_cave not in current_path:
            paths += count_valid_paths(path_dict, current_path + [next_cave], next_cave)
    return paths


def part1(data):
    """ Solve part 1 -- How many paths through this cave system are there that visit small caves at most once? """
    return count_valid_paths(data, ["start"], "start")


def count_valid_paths_with_repetition(path_dict, current_path: List[str], cave: str, seen_twice: Optional[str]):
    """ part2 helper function """
    if cave == 'end':
        return 1
    paths = 0
    for next_cave in path_dict[cave]:
        # Coming across a large cave or a small cave not seen before
        if next_cave not in small_caves or next_cave not in current_path:
            paths += count_valid_paths_with_repetition(path_dict, current_path + [next_cave], next_cave, seen_twice)

        # This is a small cave that has been seen before exactly once
        elif next_cave not in {"start", "end"} and seen_twice is None:
            paths += count_valid_paths_with_repetition(path_dict, current_path + [next_cave], next_cave, next_cave)
    return paths


def part2(data):
    """Solve part 2 -- Now, a single small cave can be visited at most twice, and the remaining small caves can be
    visited at most once. However, the caves named start and end can only be visited exactly once each.
    Given these new rules, how many paths through this cave system are there?"""
    return count_valid_paths_with_repetition(data, ["start"], "start", None)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
