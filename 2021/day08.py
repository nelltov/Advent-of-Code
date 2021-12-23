import pathlib
import sys


def parse(puzzle_input_str):
    """Parse input -- unique signal patterns, a | delimiter, and  the four digit output value"""
    entry = puzzle_input_str.splitlines()
    return entry


def part1(data):
    """Solve part 1 -- In the output values, how many times do digits 1, 4, 7, or 8 appear?
    Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which
    combinations of signals correspond to those digits."""
    count = 0

    for entry in data:
        output_values = entry.split(" | ")[1]
        for output in output_values.split(" "):
            if len(output) in [2, 4, 3, 7]:  # unique numbers of segments
                count += 1

    return count


def part2(data):
    """Solve part 2 -- For each entry, determine all of the wire/segment connections and decode the four-digit output
    values. What do you get if you add up all of the output values?"""
    count = 0

    for entry in data:
        input_values = entry.split(" | ")[0]
        output_values = entry.split(" | ")[1]
        decoded_dict = dict()
        for i in range(10):
            decoded_dict[str(i)] = ''

        pos_dict = dict()
        for char in "abcdefg":
            pos_dict["pos_" + char] = ''

        letter_count_dict = dict()
        for char in "abcdefg":
            letter_count_dict[char] = 0

        cf_values = ''

        # Initial input interpretation
        for input_value in input_values.split(" "):
            for char in input_value:
                letter_count_dict[char] += 1

            if len(input_value) == 2:
                decoded_dict['1'] = input_value
                cf_values = input_value
            elif len(input_value) == 3:
                decoded_dict['7'] = input_value
            elif len(input_value) == 4:
                decoded_dict['4'] = input_value
            elif len(input_value) == 7:
                decoded_dict['8'] = input_value

        # Decoding
        ac_values = ''
        dg_values = ''
        for letter in letter_count_dict:
            if letter_count_dict[letter] == 4:
                pos_dict['pos_e'] = letter
            elif letter_count_dict[letter] == 6:
                pos_dict['pos_b'] = letter
            elif letter_count_dict[letter] == 7:
                dg_values += letter
            elif letter_count_dict[letter] == 8:
                ac_values += letter
            elif letter_count_dict[letter] == 9:
                pos_dict['pos_f'] = letter
                for cf_char in cf_values:
                    if cf_char != letter:
                        pos_dict['pos_c'] = cf_char

        for ac_char in ac_values:
            if ac_char != pos_dict['pos_c']:
                pos_dict['pos_a'] = ac_char

        for segment in decoded_dict['4']:
            if segment not in [pos_dict['pos_b'], pos_dict['pos_c'], pos_dict['pos_f']]:
                pos_dict['pos_d'] = segment

        for dg_char in dg_values:
            if dg_char != pos_dict['pos_d']:
                pos_dict['pos_g'] = dg_char

        # Second input interpretation
        for input_value in input_values.split(" "):
            if len(input_value) == 5:
                if pos_dict['pos_b'] in input_value:
                    decoded_dict['5'] = input_value
                else:
                    if pos_dict['pos_e'] in input_value:
                        decoded_dict['2'] = input_value
                    if pos_dict['pos_f'] in input_value:
                        decoded_dict['3'] = input_value
            elif len(input_value) == 6:
                if pos_dict['pos_d'] not in input_value:
                    decoded_dict['0'] = input_value
                elif pos_dict['pos_c'] not in input_value:
                    decoded_dict['6'] = input_value
                elif pos_dict['pos_e'] not in input_value:
                    decoded_dict['9'] = input_value

        # Output interpretation
        entry_output = ''
        for output in output_values.split(" "):
            for number in decoded_dict:
                is_number = True
                if len(output) != len(decoded_dict[number]):
                    is_number = False
                for char in decoded_dict[number]:
                    if char not in output:
                        is_number = False
                if is_number:
                    entry_output += number

        count += int(entry_output)

    return count


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
