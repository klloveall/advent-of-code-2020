def process_line(line):
    return int(line)


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

def num_is_sum_of_two_numbers_in_list(target_number, list_of_nums):
    list_of_nums.sort()
    low_ptr = 0
    high_ptr = len(list_of_nums) - 1
    while low_ptr != high_ptr and list_of_nums[low_ptr] + list_of_nums[high_ptr] != target_number:
        if list_of_nums[low_ptr] + list_of_nums[high_ptr] > target_number:
            high_ptr -=1
        else:
            low_ptr += 1
    if low_ptr == high_ptr:
        return None, None
    else:
        return list_of_nums[low_ptr], list_of_nums[high_ptr]

def solvep1(input):
    for i, num in enumerate(input[25:]):
        start_i = i
        end_i = i + 25
        num_1, num_2 = num_is_sum_of_two_numbers_in_list(num, input[start_i:end_i])
        if num_1 is None:
            return num

def solvep2(input):
    target_num = solvep1(input)
    low_ptr = 0
    high_ptr = 1
    range_sum = sum(input[low_ptr:high_ptr])
    while range_sum != target_num:
        if range_sum > target_num or high_ptr == len(input) + 1:
            low_ptr += 1
            high_ptr = low_ptr + 1
        else:
            high_ptr += 1
        range_sum = sum(input[low_ptr:high_ptr])
    return min(input[low_ptr:high_ptr]) + max(input[low_ptr:high_ptr])



if __name__ == '__main__':
    processed_input = read_input('day09-input.txt')
    output1 = solvep1(processed_input)
    print(output1)
    output2 = solvep2(processed_input)
    print(output2)
