def read_numbers(input_file):
    numbers = []
    for line in input_file:
        numbers.append(int((line.strip())))
    return numbers


def read_strings(input_file):
    lines = []
    for line in input_file:
        lines.append((line.strip()))
    return lines


def read_2d_list(text_list):
    list_2d = []
    for line in text_list:
        list_2d.append(list(filter(None, line.split(" "))))
    return list_2d
