import pathlib
import sys
from typing import List


def parse(puzzle_input_str: str) -> List[str]:
    """Parse input -- passport data in batch files"""
    batches = puzzle_input_str.split("\n\n")
    for i in range(len(batches)):
        batches[i] = batches[i].replace("\n", " ")
    return batches


def part1(data: List[str]) -> int:
    """Solve part 1 -- Count the number of valid passports - those that have all required fields. Treat cid as optional.
    In your batch file, how many passports are valid?"""
    valid_passport_count = 0
    for passport in data:
        is_valid_passport = True
        fields = passport.split()
        fields_provided = [field.split(':')[0] for field in fields]
        for required_field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if required_field not in fields_provided:
                is_valid_passport = False

        if is_valid_passport:
            valid_passport_count += 1

    return valid_passport_count


def part2(data: List[str]) -> int:
    """Solve part 2 -- Count the number of valid passports - those that have all required fields and valid values.
    Continue to treat cid as optional. In your batch file, how many passports are valid?"""
    valid_passport_count = 0
    for passport in data:

        is_valid_passport = True
        fields = passport.split()
        fields_provided = [field.split(':')[0] for field in fields]
        for required_field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if required_field not in fields_provided:
                is_valid_passport = False

        # If it has all the required fields, check that all values are valid
        if is_valid_passport:
            field_dict = dict()
            for field in fields:
                key = field.split(':')[0]
                value = field.split(':')[1]
                field_dict[key] = value

            # (Birth Year) - four digits; at least 1920 and at most 2002
            byr = field_dict['byr']
            if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
                is_valid_passport = False

            # (Issue Year) - four digits; at least 2010 and at most 2020
            iyr = field_dict['iyr']
            if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
                is_valid_passport = False

            # (Expiration Year) - four digits; at least 2020 and at most 2030
            eyr = field_dict['eyr']
            if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
                is_valid_passport = False

            # (Height) - a number followed by either cm or in
            # If cm, the number must be at least 150 and at most 193
            # If in, the number must be at least 59 and at most 76
            hgt = field_dict['hgt']
            if len(hgt) < 4 or hgt[-2:] not in ['cm', 'in']:
                is_valid_passport = False
            elif hgt[-2:] == 'cm':
                if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
                    is_valid_passport = False
            elif hgt[-2:] == 'in':
                if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                    is_valid_passport = False

            # (Hair Color) - a # followed by exactly six characters 0-9 or a-f
            hcl = field_dict['hcl']
            if len(hcl) != 7 or hcl[0] != '#':
                is_valid_passport = False
            else:
                for char in hcl[1:]:
                    if not (char.isdigit() or char in 'abcdef'):
                        is_valid_passport = False
                        break

            # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
            ecl = field_dict['ecl']
            if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                is_valid_passport = False

            # (Passport ID) - a nine-digit number, including leading zeroes
            pid = field_dict['pid']
            if len(pid) != 9 or not pid.isdigit():
                is_valid_passport = False

        # If passport is still valid, add it to the valid count
        if is_valid_passport:
            valid_passport_count += 1

    return valid_passport_count


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_data = parse(puzzle_input)
        print(f"solution 1: {part1(puzzle_data)}")
        print(f"solution 2: {part2(puzzle_data)}")
