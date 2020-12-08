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
    return input


def solvep2(input):
    return input



if __name__ == '__main__':
    processed_input = read_input('day09-input.txt')
    output1 = solvep1(processed_input)
    print(output1)
    output2 = solvep2(processed_input)
    print(output2)
