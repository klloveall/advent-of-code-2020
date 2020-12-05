import re
import string
from typing import List


def process_line(line):
    passport_parts = line.strip().split(" ")
    if passport_parts == ['']:
        return {}
    ret_val = {}
    for part in passport_parts:
        key,value = part.split(":")
        ret_val[key] = value
    return ret_val


def read_input(file_name: str):
    input = []
    with open(file_name) as f:
        passport_data = {}
        for line in f.readlines():
            if not line.strip():
                input.append(passport_data)
                passport_data = {}
            passport_data.update(**process_line(line))
        if passport_data:
            input.append(passport_data)
    return input


def solvep1(input):
    valid = 0
    print(len(input))
    for passport in input:
        if 'byr' not in passport:
            continue
        if not re.match('[0-9]{4}', passport['byr']):
            continue
        try:
            birth_year = int(passport['byr'])
        except ValueError:
            continue
        if not (1920 <= birth_year <= 2002):
            continue

        if 'iyr' not in passport:
            continue
        if not re.match('[0-9]{4}', passport['iyr']):
            continue
        try:
            issue_year = int(passport['iyr'])
        except ValueError:
            continue
        if not (2010 <= issue_year <= 2020):
            continue

        if 'eyr' not in passport:
            continue
        if not re.match('[0-9]{4}', passport['eyr']):
            continue
        try:
            expiration_year = int(passport['eyr'])
        except ValueError:
            continue
        if not (2020 <= expiration_year <= 2030):
            continue

        if 'hgt' not in passport:
            continue
        if not re.match('1?[0-9]{2}[cm|in]', passport['hgt']):
            continue
        try:
            height_val = int(passport['hgt'][:-2])
            height_units = passport['hgt'][-2:]
        except ValueError:
            continue
        if height_units == 'cm':
            if not (150 <= height_val <= 193):
                continue
        elif height_units == "in":
            if not (59 <= height_val <= 76):
                continue
        else:
            continue

        if 'hcl' not in passport:
            continue
        m = re.match('^#[0-9a-f]{6}$', passport['hcl'])
        if not m:
            continue

        if 'ecl' not in passport:
            continue
        if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue

        if 'pid' not in passport:
            continue

        m = re.match('^[0-9]{9}$', passport['pid'])
        if not m:
            continue

        valid += 1
    return valid


def solvep2(input):
    return input


if __name__ == '__main__':
    input = read_input('day04-input.txt')
    output1 = solvep1(input)
    print(output1)
    output2 = solvep2(input)
    print(output2)
