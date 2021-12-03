from util.fileReader import read_strings

sample = read_strings(open("sample"))
data = read_strings(open("input"))


def create_inverse(lines):
    inverse_list = [""] * len(lines[0])
    for line in lines:
        for i in range(len(line)):
            inverse_list[i] += line[i]
    return inverse_list


def generate_gamma_or_epsilon(lines, gamma):
    output = ""
    for line in lines:
        if line.count("1") > line.count("0"):
            if gamma:
                output += "1"
            else:
                output += "0"
        else:
            if gamma:
                output += "0"
            else:
                output += "1"
    return output


def calculate_power_consumption(lines):
    inverse = create_inverse(lines)
    gamma = int(generate_gamma_or_epsilon(inverse, True), 2)
    epsilon = int(generate_gamma_or_epsilon(inverse, False), 2)
    return gamma * epsilon


# solution part 1:
print(calculate_power_consumption(data))


# part 2:
def determine_least_common(lines, index):
    delete_these_lines = []
    if lines[index].count("1") > lines[index].count("0"):
        for letter_index in range(len(lines[index])):
            if lines[index][letter_index] == "0":
                delete_these_lines.append(letter_index)
    else:
        for letter_index in range(len(lines[index])):
            if lines[index][letter_index] == "1":
                delete_these_lines.append(letter_index)
    return delete_these_lines


def remove_lines(list, to_be_removed):
    # reversed, so we dont have to modify indexes after deleting lines
    to_be_removed.reverse()
    for index in to_be_removed:
        del list[index]
    return list


def keep_wanted(list, index, wanted_value):
    delete_these_lines = []
    for i in range(len(list)):
        if list[i][index] != wanted_value:
            delete_these_lines.append(i)
    return delete_these_lines


def get_remaining_indexes(list, indexes_to_remain):
    indexes_to_delete = []
    for i in range(len(list)):
        if i not in indexes_to_remain:
            indexes_to_delete.append(i)
    return indexes_to_delete


def determine_oxygen(list):
    word_length = len(list[0])
    for i in range(word_length):
        if len(list) == 1:
            break
        inverse = create_inverse(list)
        delete_these_lines = determine_least_common(inverse, i)
        # catch the special case: equal count of 1 & 0. In that case keep the 1
        if len(delete_these_lines) == len(list) / 2:
            list = remove_lines(list, keep_wanted(list, i, "1"))
        else:
            list = remove_lines(list, delete_these_lines)
    return int(list[0], 2)


def determine_co2(list):
    word_length = len(list[0])
    for i in range(word_length):
        if len(list) == 1:
            break
        inverse = create_inverse(list)
        delete_these_lines = get_remaining_indexes(list, determine_least_common(inverse, i))
        # catch the special case: equal count of 1 & 0. In that case keep the 0)
        if len(delete_these_lines) == len(list) / 2:
            list = remove_lines(list, keep_wanted(list, i, "0"))
        else:
            list = remove_lines(list, delete_these_lines)
    return int(list[0], 2)


def determine_life_support_rating(list):
    return determine_oxygen(list.copy()) * determine_co2(list.copy())


# solution part 2:
print(determine_life_support_rating(data))
