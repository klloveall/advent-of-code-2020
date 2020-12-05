import re
import string
from typing import List


def process_line(line):
    passport_parts = line.strip().split(" ")
    if passport_parts == ['']:  # Can't just do not passport_parts; `not ['']` == False, not True like we need
        return {}
    ret_val = {}
    for part in passport_parts:
        key, value = part.split(":")
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
    for passport in input:
        if 'byr' not in passport:
            continue
        if 'iyr' not in passport:
            continue
        if 'eyr' not in passport:
            continue
        if 'hgt' not in passport:
            continue
        if 'hcl' not in passport:
            continue
        if 'ecl' not in passport:
            continue
        if 'pid' not in passport:
            continue
        valid += 1
    return valid


def is_birth_year_valid(birth_year_str: str):
    if not re.match('[0-9]{4}', birth_year_str):
        return False
    try:
        birth_year = int(birth_year_str)
    except ValueError:
        return False
    if not (1920 <= birth_year <= 2002):
        return False
    return True


def is_issue_year_valid(issue_year_str: str):
    if not re.match('[0-9]{4}', issue_year_str):
        return False
    try:
        issue_year = int(issue_year_str)
    except ValueError:
        return False
    if not (2010 <= issue_year <= 2020):
        return False
    return True


def is_expire_year_valid(expire_year_str: str):
    if not re.match('[0-9]{4}', expire_year_str):
        return False
    try:
        expiration_year = int(expire_year_str)
    except ValueError:
        return False
    if not (2020 <= expiration_year <= 2030):
        return False
    return True


def is_height_valid(height_str: str):
    regex_result = re.match('^(1?[0-9]{2})((cm)|(in))$', height_str)
    if not regex_result:
        return False
    height_val = int(regex_result.group(1))
    height_units = regex_result.group(2)
    if height_units == 'cm':
        if not (150 <= height_val <= 193):
            return False
    elif height_units == "in":
        if not (59 <= height_val <= 76):
            return False
    else:
        raise RuntimeError
    return True


def is_hair_color_valid(hair_color_str: str):
    return bool(re.match('^#[0-9a-f]{6}$', hair_color_str))


def is_eye_color_valid(eye_color_str: str):
    return bool(eye_color_str in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))


def is_passport_id_valid(passport_id_str: str):
    return bool(re.match('^[0-9]{9}$', passport_id_str))


def solvep2(input):
    valid = 0
    for passport in input:
        if 'byr' not in passport or not is_birth_year_valid(passport['byr']):
            continue
        if 'iyr' not in passport or not is_issue_year_valid(passport['iyr']):
            continue
        if 'eyr' not in passport or not is_expire_year_valid(passport['eyr']):
            continue
        if 'hgt' not in passport or not is_height_valid(passport['hgt']):
            continue
        if 'hcl' not in passport or not is_hair_color_valid(passport['hcl']):
            continue
        if 'ecl' not in passport or not is_eye_color_valid(passport['ecl']):
            continue
        if 'pid' not in passport or not is_passport_id_valid(passport['pid']):
            continue
        valid += 1
    return valid


if __name__ == '__main__':
    input = read_input('day04-input.txt')
    output1 = solvep1(input)
    print(output1)
    output2 = solvep2(input)
    print(output2)
