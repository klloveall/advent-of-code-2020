def process_line(line):
    return set(line.strip())


def read_input(file_name: str):
    input = []
    with open(file_name) as f:
        group_sets = []
        for line in f.readlines():
            if not line.strip():
                input.append(group_sets)
                group_sets = []
                continue
            question_set = process_line(line)
            group_sets.append(question_set)
        if group_sets:
            input.append(group_sets)
    return input


def solvep1(input):
    count = 0
    for group in input:
        group_set = group[0]
        for s in group:
            group_set = group_set.union(s)
        count += len(group_set)
    return count


def solvep2(input):
    count = 0
    for group in input:
        group_set = group[0]
        for s in group:
            group_set = group_set.intersection(s)
        count += len(group_set)
    return count


if __name__ == '__main__':
    input = read_input('day06-input.txt')
    output1 = solvep1(input)
    print(output1)
    output2 = solvep2(input)
    print(output2)
