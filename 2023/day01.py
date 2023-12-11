import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- lines of text in the calibration document """
    return puzzle_input_str.splitlines()


def part1(data: List[str]) -> int:
    """
    Solve part 1 -- On each line, the calibration value can be found by combining the first digit
    and the last digit (in that order) to form a single two-digit number.
    Consider your entire calibration document. What is the sum of all the calibration values?
    """
    calibration_sum = 0

    for line in data:
        filtered = list(filter(lambda c: c.isdigit(), line))
        calibration_sum += (int(filtered[0]) * 10 + int(filtered[-1]))

    return calibration_sum


def part2(data: List[str]) -> int:
    """Solve part 2 -- It looks like some of the digits are actually spelled out with letters:
        one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
    Equipped with this new information, you now need to find the real first and last digit on each line.
    What is the sum of all of the calibration values?
    """
    calibration_sum = 0

    for line in data:
        filtered = ""
        n = len(line)
        for i in range(n):
            c = line[i]
            if c.isdigit():
                filtered += c
            else:
                if i < n - 2 and line[i:i+3] == "one":
                    filtered += "1"
                if i < n - 2 and line[i:i+3] == "two":
                    filtered += "2"
                if i < n - 4 and line[i:i+5] == "three":
                    filtered += "3"
                if i < n - 3 and line[i:i+4] == "four":
                    filtered += "4"
                if i < n - 3 and line[i:i+4] == "five":
                    filtered += "5"
                if i < n - 2 and line[i:i+3] == "six":
                    filtered += "6"
                if i < n - 4 and line[i:i+5] == "seven":
                    filtered += "7"
                if i < n - 4 and line[i:i+5] == "eight":
                    filtered += "8"
                if i < n - 3 and line[i:i+4] == "nine":
                    filtered += "9"

        calibration_sum += (int(filtered[0]) * 10 + int(filtered[-1]))

    return calibration_sum


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
