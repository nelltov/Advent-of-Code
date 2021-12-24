import pathlib
import sys
from typing import List
from collections import Counter

"""
Influenced by u/4HbQ on r/adventofcode
Tracking pair and character counts in two Counter dictionaries.
For each replacement:
- decrease the count of the original pair
- increase the count of the two replacement pairs
- increase the count of the new character

Optimization compared to my initial implementation:
- Rather than incrementing the counts of each pair one at a time, accounting for repeated
pairs by taking their counts all at once. That way, runs in proportion to the number of
unique pairs rather than the total number of pairs.
"""


def parse(puzzle_input_str):
    """Parse input -- a polymer template and a list of pair insertion rules"""
    parsed_input = puzzle_input_str.split("\n\n")
    template = parsed_input[0]

    pair_insertion_rules = dict(rule.split(" -> ") for rule in parsed_input[1].splitlines())

    pair_count = Counter(map(str.__add__, template, template[1:]))  # NNCB --> {'NN': 1, 'NC': 1, 'CB': 1}
    elem_count = Counter(template)

    return pair_insertion_rules, pair_count, elem_count


def solve(data, steps):
    """Apply input number of steps of pair insertions to the polymer template and find the most and least common
    elements in the result. What do you get if you take the quantity of the most common element and subtract the
    quantity of the least common element? """
    pair_insertion_rules, pair_count, elem_count = data

    for _ in range(steps):
        for pair, count in pair_count.copy().items():
            insertion = pair_insertion_rules[pair]
            pair_count[pair] -= count
            pair_count[pair[0] + insertion] += count
            pair_count[insertion + pair[1]] += count
            elem_count[insertion] += count

    return max(elem_count.values()) - min(elem_count.values())


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {solve(puzzle_data, 10)}")
        puzzle_data = parse(puzzle_input)  # Need to reset the puzzle data before calling part 2
        print(f"solution 2: {solve(puzzle_data, 40)}")
