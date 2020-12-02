from typing import List

def process_line(line):
    space_split = line.split(' ')
    range_start = int(space_split[0].split('-')[0])
    range_end = int(space_split[0].split('-')[1])
    expected_char = space_split[1][0]
    given_pwd = space_split[2]
    return (range_start, range_end, expected_char, given_pwd)

def read_input(file_name: str):
    input = []
    with open(file_name) as f:
        for line in f.readlines():
            if line:
                input.append(process_line(line))
    return input


def solvep1(input):
    valid_password_count = 0
    for range_start, range_end, expected_character, password in input:
        count = 0
        for char in password:
            if char == expected_character:
                count += 1

        if range_start <= count <= range_end:
            valid_password_count += 1
    return valid_password_count


def solvep2(input):
    valid_password_count = 0
    for range_start, range_end, expected_character, password in input:
        count = 0
        if password[range_start - 1] == expected_character:
            count += 1
        if password[range_end - 1] == expected_character:
            count += 1
        if count == 1:
            valid_password_count += 1
    return valid_password_count


if __name__ == '__main__':
    input = read_input('day02-input.txt')
    output1 = solvep1(input)
    print(output1)
    output2 = solvep2(input)
    print(output2)
