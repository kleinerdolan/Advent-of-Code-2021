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
