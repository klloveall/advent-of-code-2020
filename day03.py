import string
from typing import List

def process_line(line):
    return line.strip()

def read_input(file_name: str):
    input = []
    with open(file_name) as f:
        for line in f.readlines():
            if line:
                input.append(process_line(line))
    return input


def solvep1(input):
    right_plus = 3
    down_plus = 1
    row = 0
    col = 0
    trees = 0
    while row < len(input):
        if input[row][col%len(input[row])] == '#':
            trees += 1
        row += down_plus
        col += right_plus
    return trees


def solvep2(input):
    plus_pairs = [
        (1,1),
        (1,3),
        (1,5),
        (1,7),
        (2,1)
    ]
    res = 1
    for down_plus, right_plus in plus_pairs:
        row = 0
        col = 0
        trees = 0
        while row < len(input):
            if input[row][col%len(input[row])] == '#':
                trees += 1
            row += down_plus
            col += right_plus
        res *= trees
    return res

if __name__ == '__main__':
    input = read_input('day03-input.txt')
    output1 = solvep1(input)
    print(output1)
    output2 = solvep2(input)
    print(output2)
