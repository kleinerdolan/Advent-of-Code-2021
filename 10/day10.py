from util.fileReader import read_strings

sample = read_strings(open("sample"))
data = read_strings(open("input"))


def determine_value(char):
    if char == ")":
        return 3
    elif char == "]":
        return 57
    elif char == "}":
        return 1197
    elif char == ">":
        return 25137


def check_line_corrupted(line):
    opening_braces = []
    for char in line:
        # opening braces
        if char == "(":
            opening_braces.append(char)
        elif char == "[":
            opening_braces.append(char)
        elif char == "{":
            opening_braces.append(char)
        elif char == "<":
            opening_braces.append(char)
        # closing braces:
        if char == ")":
            if opening_braces[-1] == "(":
                opening_braces.pop()
            else:
                # print("Unclosed",opening_braces[-1])
                return determine_value(char)
        elif char == "]":
            if opening_braces[-1] == "[":
                opening_braces.pop()
            else:
                # print("Unclosed",opening_braces[-1])
                return determine_value(char)
        elif char == "}":
            if opening_braces[-1] == "{":
                opening_braces.pop()
            else:
                # print("Unclosed",opening_braces[-1])
                return determine_value(char)
        elif char == ">":
            if opening_braces[-1] == "<":
                opening_braces.pop()
            else:
                # print("Unclosed",opening_braces[-1])
                return determine_value(char)
    return 0


def check_all_corrupted(list):
    result = 0
    for line in list:
        result += check_line_corrupted(line)
    return result

# solution part 1:
# print(check_all_corrupted(data))


# part 2:
def remove_corrupted_lines(list):
    uncomplete_list = []
    for line in list:
        if check_line_corrupted(line) == 0:
            uncomplete_list.append(line)
    return uncomplete_list


def complete_line(line):
    opening_braces = []
    for char in line:
        # opening braces
        if char == "(":
            opening_braces.append(char)
        elif char == "[":
            opening_braces.append(char)
        elif char == "{":
            opening_braces.append(char)
        elif char == "<":
            opening_braces.append(char)
        # closing braces:
        if char == ")":
            if opening_braces[-1] == "(":
                opening_braces.pop()
        elif char == "]":
            if opening_braces[-1] == "[":
                opening_braces.pop()
        elif char == "}":
            if opening_braces[-1] == "{":
                opening_braces.pop()
        elif char == ">":
            if opening_braces[-1] == "<":
                opening_braces.pop()
    return opening_braces


def determine_incomplete_value(open_backets):
    open_backets.reverse()
    total = 0
    for char in open_backets:
        total *= 5
        if char == "(":
            total += 1
        elif char == "[":
            total += 2
        elif char == "{":
            total += 3
        elif char == "<":
            total += 4
    return total


def check_all_incomplete(list):
    list = remove_corrupted_lines(list)
    results = []
    for line in list:
        results.append(determine_incomplete_value(complete_line(line)))
    results.sort()
    middle_index = int(len(results) / 2)
    return results[middle_index]


# solution part 2:
print(check_all_incomplete(data))
