def process_line(line):
    return line.split(" ")


class DO_NOT_SPLIT:
    pass


def read_input(file_name: str,
               first_delimiter: str or None or DO_NOT_SPLIT = '\n',
               second_delimiter: str or None or DO_NOT_SPLIT=DO_NOT_SPLIT,
               third_delimiter: str or None or DO_NOT_SPLIT=DO_NOT_SPLIT,
               final_group_processor=process_line):
    with open(file_name) as f:
        processed_input = f.read()
        if first_delimiter is not DO_NOT_SPLIT:
            first_split = processed_input.split(first_delimiter)
            if second_delimiter is not DO_NOT_SPLIT:
                second_split = [x.split(second_delimiter) for x in first_split]

                if third_delimiter is not DO_NOT_SPLIT:
                    output = [[[final_group_processor(group) for group in x.split(third_delimiter)] for x in inner_split] for inner_split in second_split]
                else:
                    output = [[final_group_processor(x) for x in inner_split] for inner_split in second_split]
            else:
                output = [final_group_processor(group) for group in first_split]
        else:
            output = final_group_processor(processed_input)
    return output

class Exc(Exception):
    pass

def solvep1(input):
    instruction_line = 0
    accum = 0
    visited_lines = set()
    while True:
        if instruction_line in visited_lines:
            break
        else:
            visited_lines.add(instruction_line)

        try:
            instruction = input[instruction_line]
        except IndexError:
            exc = Exc()
            exc.instruction_line = instruction_line
            exc.accum = accum
            raise exc

        if instruction[0] == "nop":
            instruction_line += 1

        elif instruction[0] == "acc":
            accum += int(instruction[1])
            instruction_line += 1

        elif instruction[0] == "jmp":
            instruction_line += int(instruction[1])

        else:
            raise RuntimeError()

    return accum


def solvep2(input):
    for i in range(len(input)):
        if input[i][0] in ('jmp', 'nop'):
            old_val = input[i][0]
            if old_val == 'jmp':
                input[i][0] = 'nop'
            else:
                input[i][0] = 'jmp'

            try:
                solvep1(input)
            except Exc as e:
                if e.instruction_line == len(input):
                    return e.accum
            input[i][0] = old_val



if __name__ == '__main__':
    processed_input = read_input('day08-input.txt')
    output1 = solvep1(processed_input)
    print(output1)
    output2 = solvep2(processed_input)
    print(output2)
