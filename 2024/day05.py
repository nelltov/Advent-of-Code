import pathlib
import sys
from typing import List, Tuple


def parse(puzzle_input_str: str) -> Tuple[List[str], List[List[str]]]:
    """Parse input -- page ordering rules and the pages to produce in each update"""
    return puzzle_input_str.split("\n\n")[0].splitlines(), [elem.split(",") for elem in puzzle_input_str.split("\n\n")[1].splitlines()]


def follows_rules(update: List[str], rules: List[str]) -> Tuple[bool, str]:
    cur_dictionary = dict()
    for i in range(len(update)):
        cur_dictionary[update[i]] = i

    rules_broken = False
    broken_rule = ''

    for rule in rules:
        [left_page, right_page] = rule.split("|")
        if (left_page in cur_dictionary and right_page in cur_dictionary and
                cur_dictionary[left_page] > cur_dictionary[right_page]):
            rules_broken = True
            broken_rule = f'{cur_dictionary[left_page]}|{cur_dictionary[right_page]}'
            break

    return rules_broken, broken_rule


def part1(data: Tuple[List[str], List[List[str]]]) -> int:
    """Solve part 1 -- Determine which updates are already in the correct order.
    What do you get if you add up the middle page number from those correctly-ordered updates?"""
    page_ordering_rules, update_pages = data
    middle_sum = 0

    for update in update_pages:
        rules_broken, _ = follows_rules(update, page_ordering_rules)

        if not rules_broken:
            middle_page_number = int(update[len(update)//2])
            middle_sum += middle_page_number

    return middle_sum


def part2(data: Tuple[List[str], List[List[str]]]):
    """Solve part 2 -- Find the updates which are not in the correct order.
    What do you get if you add up the middle page numbers after correctly ordering just those updates?"""
    page_ordering_rules, update_pages = data
    middle_sum = 0

    for update in update_pages:
        rules_broken, broken_rule = follows_rules(update, page_ordering_rules)

        # ignore the updates in the correct order
        if not rules_broken:
            continue

        # swapping values until all rules pass
        while rules_broken:
            [i, j] = broken_rule.split("|")
            update[int(i)], update[int(j)] = update[int(j)], update[int(i)]

            rules_broken, broken_rule = follows_rules(update, page_ordering_rules)

        middle_page_number = int(update[len(update) // 2])
        middle_sum += middle_page_number

    return middle_sum


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")

