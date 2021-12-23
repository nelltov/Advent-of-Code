import pathlib
import sys
from typing import List, Optional


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input --  copy of the navigation subsystem"""
    return puzzle_input_str.splitlines()


expected_end = {'(': ')', '[': ']', '{': '}', '<': '>'}
part1_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
part2_points = {')': 1, ']': 2, '}': 3, '>': 4}


def find_first_illegal_char(line: str):
    """ Returns the first illegal char found in a line (returns ending punctuation mark) """
    found_chars = []
    expected_chars = []
    for char in line:
        # encountering an opening punctuation mark
        if char in expected_end:
            found_chars += [char]
            expected_chars += [expected_end[char]]

        # encountering an ending punctuation mark
        else:
            if len(expected_chars) == 0:
                return char
            else:
                if char != expected_chars[-1]:
                    return char

                else:  # the punctuation marks match
                    found_chars = found_chars[:-1]
                    expected_chars = expected_chars[:-1]

    return None


def part1(data: List[str]) -> int:
    """Solve part 1 -- Find the first illegal character in each corrupted line of the navigation subsystem.
    What is the total syntax error score for those errors?"""
    illegal_chars: List[str] = []
    syntax_error_score = 0

    for line in data:
        if find_first_illegal_char(line) is not None:
            illegal_chars += [find_first_illegal_char(line)]

    for illegal_char in illegal_chars:
        syntax_error_score += part1_points[illegal_char]

    return syntax_error_score


def part2(data):
    """Solve part 2 -- Find the completion string for each incomplete line,
    score the completion strings, and sort the scores. What is the middle score?"""

    score_list = []

    for line in data:
        completion_string = []
        score = 0

        if find_first_illegal_char(line) is None:
            incomplete_chars = []
            expected_chars = []

            for char in line:
                # encountering an opening punctuation mark
                if char in expected_end:
                    incomplete_chars += [char]
                    expected_chars += [expected_end[char]]

                # encountering an ending punctuation mark
                else:
                    incomplete_chars = incomplete_chars[:-1]
                    expected_chars = expected_chars[:-1]

            # Finding the completion string
            for opening_char in incomplete_chars:
                completion_string += [expected_end[opening_char]]

            # have to traverse the list backwards to get the correct completion string
            for end_idx in range(len(completion_string) - 1, -1, -1):
                score = (score * 5) + part2_points[completion_string[end_idx]]

            score_list += [score]

    score_list.sort()
    idx = len(score_list) // 2
    return score_list[idx]


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
