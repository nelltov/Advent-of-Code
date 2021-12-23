import pathlib
import sys
from typing import List, Tuple


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- list of commands and units"""
    return puzzle_input_str.splitlines()


def part1(data: List[str]) -> int:
    """Solve part 1 -- Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate,
    then multiply them together. What is the power consumption of the submarine?"""
    gamma_rate = ''  # The most common bit from each position in the diagnostic report
    epsilon_rate = ''  # The least common bit from each position in the diagnostic report

    if len(data) <= 1:
        return 0

    zero_count = [0 for _ in range(len(data[0]))]
    one_count = [0 for _ in range(len(data[0]))]

    # Calculating the counts of each bit in each position and storing values in corresponding lists
    for number in data:
        for bit_index in range(len(number)):
            if number[bit_index] == '0':
                zero_count[bit_index] += 1
            else:
                one_count[bit_index] += 1

    # Determining the gamma and epsilon rates based on bit frequencies in each position
    for i in range(len(zero_count)):
        if zero_count[i] > one_count[i]:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    # Converting to binary and then multiplying them together
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(data: List[str]) -> int:
    """Solve part 2 -- Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and
    CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine?"""
    oxygen_generator_rating: List[str] = data
    co2_scrubber_rating: List[str] = data

    for i in range(len(data[0])):
        # Lists will store which numbers are kept after each round of filtering for each rating
        oxygen_generator_candidates = []
        co2_scrubbing_candidates = []

        # Determining which values to keep as possible oxygen generator ratings based on gamma rate
        if len(oxygen_generator_rating) > 1:
            zero_count = 0
            one_count = 0
            # Recalculating the counts of the bits in the next position
            for number in oxygen_generator_rating:
                if number[i] == '0':
                    zero_count += 1
                else:
                    one_count += 1

            # Determining the most common bit
            if one_count >= zero_count:
                most_common_bit = '1'
            else:
                most_common_bit = '0'

            # Going back through the list and keeping only the numbers with the correct bit
            for number in oxygen_generator_rating:
                if number[i] == most_common_bit:
                    oxygen_generator_candidates += [number]
            oxygen_generator_rating = oxygen_generator_candidates

        # Determining which values to keep as possible co2 scrubber ratings based on epsilon rate
        if len(co2_scrubber_rating) > 1:
            zero_count = 0
            one_count = 0
            # Recalculating the counts of the bits in the next position
            for number in co2_scrubber_rating:
                if number[i] == '0':
                    zero_count += 1
                else:
                    one_count += 1

            # Determining the least common bit
            if zero_count <= one_count:
                least_common_bit = '0'
            else:
                least_common_bit = '1'

            # Going back through the list and keeping only the numbers with the correct bit
            for number in co2_scrubber_rating:
                if number[i] == least_common_bit:
                    co2_scrubbing_candidates += [number]
            co2_scrubber_rating = co2_scrubbing_candidates

    assert(len(oxygen_generator_rating) == 1 and len(co2_scrubber_rating) == 1)

    # Calculating the life support rating
    return int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

