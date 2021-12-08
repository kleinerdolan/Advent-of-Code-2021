from util.fileReader import read_strings

sample = read_strings(open("sample"))
data = read_strings(open("input"))


def solve_part_1(digits):
    relevant_digits = []
    for line in digits:
        for digit in line.split(" | ")[1].split(" "):
            relevant_digits.append(digit)
    result = 0
    for entry in relevant_digits:
        if len(entry) == 2 or len(entry) == 3 or len(entry) == 4 or len(entry) == 7:
            result += 1
    return result


# print(solve_part_1(data))


# part 2:
def print_one(config):
    digit = ""
    digit += "    " + "\n"
    digit += "     "+config[2] + "\n"
    digit += "     "+config[2] + "\n"
    digit += "      " + "\n"
    digit += "     "+config[5] + "\n"
    digit += "     "+config[5] + "\n"
    digit += "      " + "\n"
    return digit


def print_two(config):
    digit = ""
    digit += " "+config[0]+config[0]+config[0]+config[0]+" " + "\n"
    digit += "     "+config[2] + "\n"
    digit += "     "+config[2] + "\n"
    digit += " "+config[3]+config[3]+config[3]+config[3]+" " + "\n"
    digit += config[4]+"     " + "\n"
    digit += config[4]+"     " + "\n"
    digit += " "+config[6]+config[6]+config[6]+config[6]+" " + "\n"
    return digit


def print_three(config):
    digit = ""
    digit += " "+config[0]+config[0]+config[0]+config[0]+" " + "\n"
    digit += "     "+config[2] + "\n"
    digit += "     "+config[2] + "\n"
    digit += " "+config[3]+config[3]+config[3]+config[3]+" " + "\n"
    digit += "     "+config[5] + "\n"
    digit += "     "+config[5] + "\n"
    digit += " "+config[6]+config[6]+config[6]+config[6]+" " + "\n"
    return digit


def print_four(config):
    digit = ""
    digit += "    " + "\n"
    digit += config[1]+"    "+config[2] + "\n"
    digit += config[1]+"    "+config[2] + "\n"
    digit += " "+config[3]+config[3]+config[3]+config[3]+" " + "\n"
    digit += "     "+config[5] + "\n"
    digit += "     "+config[5] + "\n"
    digit += "    " + "\n"
    return digit


def print_five(config):
    digit = ""
    digit += " "+config[0]+config[0]+config[0]+config[0]+" " + "\n"
    digit += config[1]+"     " + "\n"
    digit += config[1]+"     " + "\n"
    digit += " "+config[3]+config[3]+config[3]+config[3]+" " + "\n"
    digit += "     "+config[5] + "\n"
    digit += "     "+config[5] + "\n"
    digit += " "+config[6]+config[6]+config[6]+config[6]+" " + "\n"
    return digit


def print_six(config):
    digit = ""
    digit += " "+config[0]+config[0]+config[0]+config[0]+" " + "\n"
    digit += config[1]+"     " + "\n"
    digit += config[1]+"     " + "\n"
    digit += " "+config[3]+config[3]+config[3]+config[3]+" " + "\n"
    digit += config[4]+"    "+config[5] + "\n"
    digit += config[4]+"    "+config[5] + "\n"
    digit += " "+config[6]+config[6]+config[6]+config[6]+" " + "\n"
    return digit


def print_seven(config):
    digit = ""
    digit += " "+config[0]+config[0]+config[0]+config[0]+" " + "\n"
    digit += "     "+config[2] + "\n"
    digit += "     "+config[2] + "\n"
    digit += "      " + "\n"
    digit += "     "+config[5] + "\n"
    digit += "     "+config[5] + "\n"
    digit += "      " + "\n"
    return digit


def print_eight(config):
    digit = ""
    digit += " "+config[0]+config[0]+config[0]+config[0]+" " + "\n"
    digit += config[1]+"    "+config[2] + "\n"
    digit += config[1]+"    "+config[2] + "\n"
    digit += " "+config[3]+config[3]+config[3]+config[3]+" " + "\n"
    digit += config[4]+"    "+config[5] + "\n"
    digit += config[4]+"    "+config[5] + "\n"
    digit += " "+config[6]+config[6]+config[6]+config[6]+" " + "\n"
    return digit


def print_nine(config):
    digit = ""
    digit += " "+config[0]+config[0]+config[0]+config[0]+" " + "\n"
    digit += config[1]+"    "+config[2] + "\n"
    digit += config[1]+"    "+config[2] + "\n"
    digit += " "+config[3]+config[3]+config[3]+config[3]+" " + "\n"
    digit += "     "+config[5] + "\n"
    digit += "     "+config[5] + "\n"
    digit += " "+config[6]+config[6]+config[6]+config[6]+" " + "\n"
    return digit


def is_one(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[10] != " " and digit[31] != " ":
        if num_of_chars == 4:
            return True
    return False


def is_two(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[1] != " " and digit[12] != " " and digit[22] != " " and digit[28] != " " and digit[43] != " ":
        if num_of_chars == 16:
            return True
    return False


def is_three(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[1] != " " and digit[12] != " " and digit[22] != " " and digit[33] != " " and digit[43] != " ":
        if num_of_chars == 16:
            return True
    return False


def is_four(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[5] != " " and digit[10] != " " and digit[20] != " " and digit[31] != " ":
        if num_of_chars == 10:
            return True
    return False


def is_five(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[1] != " " and digit[7] != " " and digit[22] != " " and digit[33] != " " and digit[43] != " ":
        if num_of_chars == 16:
            return True
    return False


def is_six(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[1] != " " and digit[7] != " " and digit[22] != " " and digit[28] != " " and digit[33] != " " and digit[43] != " ":
        if num_of_chars == 18:
            return True
    return False


def is_seven(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[1] != " " and digit[12] != " " and digit[33] != " ":
        if num_of_chars == 8:
            return True
    return False


def is_eight(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[1] != " " and digit[7] != " " and digit[12] != " " and digit[22] != " " and digit[28] != " " and digit[33] != " " and digit[43] != " ":
        if num_of_chars == 20:
            return True
    return False


def is_nine(digit):
    num_of_chars = len(''.join(digit.split()))
    if digit[1] != " " and digit[7] != " " and digit[12] != " " and digit[22] != " " and digit[33] != " " and digit[43] != " ":
        if num_of_chars == 18:
            return True
    return False


def visualize_config(config):
    print(print_one(config))
    print(print_two(config))
    print(print_three(config))
    print(print_four(config))
    print(print_five(config))
    print(print_six(config))
    print(print_seven(config))
    print(print_eight(config))
    print(print_nine(config))


def validate_config(config):
    one = is_one(print_one(config))
    # print(one)
    two = is_two(print_two(config))
    # print(two)
    three = is_three(print_three(config))
    # print(three)
    four = is_four(print_four(config))
    # print(four)
    five = is_five(print_five(config))
    # print(five)
    six = is_six(print_six(config))
    # print(six)
    seven = is_seven(print_seven(config))
    # print(seven)
    eight = is_eight(print_eight(config))
    # print(eight)
    nine = is_nine(print_nine(config))
    # print(nine)
    config_valid = one and two and three and four and five and six and seven and eight and nine
    return config_valid


print(validate_config(["b", "c", "f", "a", "e", "d", "g"]))
