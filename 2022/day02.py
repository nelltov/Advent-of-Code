import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- Strategy guide to individual moves"""
    return puzzle_input_str.splitlines()


def part1(data: List[str]) -> int:
    """Solve part 1 -- What would your total score be if everything goes exactly according to your strategy guide?"""
    total_score = 0
    for cur_round in data:
        p1p2 = cur_round.split(" ")
        p1 = p1p2[0]
        p2 = p1p2[1]

        # adding the shape score
        if p2 == "X":
            total_score += 1
        elif p2 == "Y":
            total_score += 2
        else:
            total_score += 3

        # adding the outcome score
        if (p1 == "A" and p2 == "Y") or \
           (p1 == "B" and p2 == "Z") or \
           (p1 == "C" and p2 == "X"):
            total_score += 6
        elif (p1 == "A" and p2 == "X") or \
             (p1 == "B" and p2 == "Y") or \
             (p1 == "C" and p2 == "Z"):
            total_score += 3

    return total_score


class Rock(object):
    def __init__(self):
        self.win_score = 2 + 6   # pick paper and win
        self.draw_score = 1 + 3  # pick rock and draw
        self.lose_score = 3 + 0  # pick scissors and lose


class Paper(object):
    def __init__(self):
        self.win_score = 3 + 6   # pick scissors and win
        self.draw_score = 2 + 3  # pick paper and draw
        self.lose_score = 1 + 0  # pick rock and lose


class Scissors(object):
    def __init__(self):
        self.win_score = 1 + 6   # pick rock and win
        self.draw_score = 3 + 3  # pick scissors and draw
        self.lose_score = 2 + 0  # pick paper and lose


def part2(data: List[str]) -> int:
    """Solve part 2 -- Following the Elf's instructions for the second column,
    what would your total score be if everything goes exactly according to your strategy guide? """
    total_score = 0
    for cur_round in data:
        p1p2 = cur_round.split(" ")
        p1 = p1p2[0]
        p2 = p1p2[1]

        # instantiating the class for the first player's move
        if p1 == "A":
            p1obj = Rock()
        elif p1 == "B":
            p1obj = Paper()
        else:
            p1obj = Scissors()

        # adding in the score based on what the second player did
        if p2 == "X":
            total_score += p1obj.lose_score
        elif p2 == "Y":
            total_score += p1obj.draw_score
        else:
            total_score += p1obj.win_score

    return total_score


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
