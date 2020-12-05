import re
import string
from typing import List


def process_line(line):
    return line


def read_input(file_name: str):
    input = []
    with open(file_name) as f:
        for line in f.readlines():
            input.append(process_line(line.strip()))
    return input


def seat_string_to_row_and_seat(seat):
    row_low = 0
    row_high = 127
    seat_low = 0
    seat_high = 7
    for char in seat:
        row_partition = (row_high - row_low + 1) / 2
        seat_partition = (seat_high - seat_low + 1) / 2
        if char == "F":
            row_high -= row_partition
        elif char == "B":
            row_low += row_partition
        elif char == "L":
            seat_high -= seat_partition
        elif char == "R":
            seat_low += seat_partition
        else:
            raise RuntimeError
    if row_low != row_high or seat_low != seat_high:
        raise RuntimeError
    return row_low, seat_low


def get_seat_id(row, seat):
    return row * 8 + seat


def solvep1(input):
    highest = 0
    for row in input:
        row, seat = seat_string_to_row_and_seat(row)
        seat_id = get_seat_id(row, seat)
        if seat_id > highest:
            highest = seat_id
    return highest


def solvep2(input):
    seat_ids = []
    for row in input:
        row, seat = seat_string_to_row_and_seat(row)
        seat_id = get_seat_id(row, seat)
        seat_ids.append(seat_id)
    seat_ids.sort()
    last_seat_id = seat_ids[0]
    for seat_id in seat_ids:
        if seat_id == last_seat_id + 2:
            return seat_id - 1
        else:
            last_seat_id = seat_id


if __name__ == '__main__':
    input = read_input('day05-input.txt')

    output1 = solvep1(input)
    print(output1)

    output2 = solvep2(input)
    print(output2)
