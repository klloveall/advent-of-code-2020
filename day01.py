from typing import List


def read_input(file_name: str):
    input = []
    with open(file_name) as f:
        for line in f.readlines():
            if line:
                input.append(int(line))
    return input


def solvep1(input: List[int]):
    sorted_list = sorted(input)
    low_ptr = 0
    high_ptr = len(input) - 1
    while sorted_list[low_ptr] + sorted_list[high_ptr] != 2020:
        if sorted_list[low_ptr] + sorted_list[high_ptr] < 2020:
            low_ptr += 1
        else:
            high_ptr -= 1

    return sorted_list[low_ptr] * sorted_list[high_ptr]


def solvep2(input: List[int]):
    sorted_list = sorted(input)
    low_ptr = 0
    mid_ptr = 1
    high_ptr = len(input) - 1
    while sorted_list[low_ptr] + sorted_list[mid_ptr] + sorted_list[high_ptr] != 2020:
        if sorted_list[low_ptr] + sorted_list[mid_ptr] + sorted_list[high_ptr] > 2020:
            if low_ptr == mid_ptr -1:
                high_ptr -= 1
                low_ptr = 0
                mid_ptr = 1
            else:
                low_ptr += 1
                mid_ptr = low_ptr + 1
        elif mid_ptr == high_ptr - 1:
                low_ptr += 1
                mid_ptr = low_ptr + 1
        else:
            mid_ptr += 1

    return sorted_list[low_ptr] * sorted_list[mid_ptr] * sorted_list[high_ptr]


if __name__ == '__main__':
    input = read_input('day01-input.txt')
    output1 = solvep1(input)
    print(output1)
    output2 = solvep2(input)
    print(output2)
