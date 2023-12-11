import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- record of games """
    return puzzle_input_str.splitlines()


def part1(data: List[str]) -> int:
    """
    Solve part 1 --
    Determine which games would have been possible if the bag had been loaded with only 12 red cubes,
    13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
    """
    id_sum = 0
    cube_amounts = {"red": 12, "green": 13, "blue": 14}

    # Game 1: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green
    for game in data:
        possible_game = True

        # game ID
        game_number = game.split(":")[0]
        current_id = game_number.split(" ")[1]

        # looking at the set information
        game_sets = game.split(":")[1][1:].split("; ")
        for current_set in game_sets:
            cube_colors = current_set.split(", ")
            for cube_color in cube_colors:
                current_count = int(cube_color.split(" ")[0])
                current_color = cube_color.split(" ")[1]
                if current_count > cube_amounts[current_color]:
                    possible_game = False

        if possible_game:
            id_sum += int(current_id)

    return id_sum


def part2(data: List[str]) -> int:
    """
    Solve part 2 --
    For each game, find the minimum set of cubes that must have been present.
    What is the sum of the power of these sets?
    """
    power_sum = 0

    for game in data:
        min_amounts = {"red": None, "green": None, "blue": None}

        # looking at all the set information for the current game
        game_sets = game.split(":")[1][1:].split("; ")
        for current_set in game_sets:
            cube_colors = current_set.split(", ")
            for cube_color in cube_colors:
                current_count = int(cube_color.split(" ")[0])
                current_color = cube_color.split(" ")[1]
                if min_amounts[current_color] is None or current_count > min_amounts[current_color]:
                    min_amounts[current_color] = current_count

        power_sum += min_amounts["red"] * min_amounts["green"] * min_amounts["blue"]

    return power_sum


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
