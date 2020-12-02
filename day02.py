from typing import List

def process_line(line):
    return line
    ...

def read_input(file_name: str):
    input = []
    with open(file_name) as f:
        for line in f.readlines():
            if line:
                input.append(process_line(line))
    return input


def solvep1(input: List[int]):
    ...


def solvep2(input: List[int]):
    ...


if __name__ == '__main__':
    input = read_input('day02-input.txt')
    output1 = solvep1(input)
    print(output1)
    output2 = solvep2(input)
    print(output2)
