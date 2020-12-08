import re


def process_line(line):
    outer_bag_color, inner_bags_str = line.split(' bags contain ')
    inner_bags_arr = inner_bags_str.split(', ')
    inner_bag_map = {}
    for inner_bag_str in inner_bags_arr:
        if inner_bag_str == 'no other bags.':
            continue
        result = re.match('^(\d) ([a-z ]+) bags?.?$', inner_bag_str)
        inner_bag_map[result.group(2)] = result.group(1)
    return outer_bag_color, inner_bag_map


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

def bags_that_can_contain_bag(bag_color, bag_maps):
    bags_that_can_contain = set()
    for outer_bag, inner_bag_map in bag_maps.items():
        if bag_color in inner_bag_map:
            bags_that_can_contain.add(outer_bag)
    return bags_that_can_contain

def solvep1(input):
    bag_maps = {
        i[0]: i[1]
        for i in input
    }
    latest_bags = {'shiny gold'}
    all_bags_matched = set()
    while latest_bags:
        new_latest_bags = set()
        for bag in latest_bags:
            bags_that_can_contain = bags_that_can_contain_bag(bag, bag_maps)
            new_latest_bags = new_latest_bags.union(bags_that_can_contain)
            all_bags_matched = all_bags_matched.union(bags_that_can_contain)
        latest_bags = new_latest_bags
    return len(all_bags_matched)


def solvep2(input):
    bag_maps = {
        i[0]: i[1]
        for i in input
    }
    latest_bags = ['shiny gold']
    bags_must_contain = []
    while latest_bags:
        new_latest_bags = []
        for bag in latest_bags:
            if not bag_maps[bag]:
                continue
            for inner_bag in bag_maps[bag]:
                for _ in range(int(bag_maps[bag][inner_bag])):
                    bags_must_contain.append(inner_bag)
                    new_latest_bags.append(inner_bag)
        latest_bags = new_latest_bags
    return len(bags_must_contain)


if __name__ == '__main__':
    processed_input = read_input('day07-input.txt')
    output1 = solvep1(processed_input)
    print(output1)
    output2 = solvep2(processed_input)
    print(output2)
