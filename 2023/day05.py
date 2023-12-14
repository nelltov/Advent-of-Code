import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    return puzzle_input_str.split("\n\n")


def helper(data: List[str], seeds: List[int]) -> int:
    location_list = []

    maps = data[1:]

    for seed in seeds:
        current_location_number = seed

        # read every map to update location number accordingly
        for current_map in maps:
            map_lines = current_map.split(":\n")[1].split("\n")

            for line in map_lines:
                split_line = line.split(" ")
                destination_range_start = int(split_line[0])
                source_range_start = int(split_line[1])
                range_length = int(split_line[2])

                if source_range_start <= current_location_number < source_range_start + range_length:
                    current_location_number = destination_range_start + (current_location_number - source_range_start)
                    break  # only change the location number once per map

        location_list.append(current_location_number)

    try:
        return min(location_list)
    except:
        return 0


def part1(data: List[str]) -> int:
    """ Solve part 1 -- What is the lowest location number that corresponds to any of the initial seed numbers? """
    return helper(data, list(map(lambda x: int(x), data[0].split(": ")[1].split(" "))))


def part2(data: List[str]) -> int:
    """
    Solve part 2
    Consider all of the initial seed numbers listed in the ranges on the first line of the almanac.
    What is the lowest location number that corresponds to any of the initial seed numbers?
    """
    pass


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
