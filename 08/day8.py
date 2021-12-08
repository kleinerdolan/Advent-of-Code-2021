from util.fileReader import read_strings
from day8_first_try import visualize_config

sample = read_strings(open("sample"))
data = read_strings(open("input"))


def parse_input(input_string):
    first_part = []
    second_part = []
    for line in input_string:
        first_part.append(line.split(" | ")[0].split(" "))
        second_part.append(line.split(" | ")[1].split(" "))
    return first_part, second_part


def find_one(encrypted_digits):
    for digit in encrypted_digits:
        if len(digit) == 2:
            return digit


def find_four(encrypted_digits):
    for digit in encrypted_digits:
        if len(digit) == 4:
            return digit


def find_seven(encrypted_digits):
    for digit in encrypted_digits:
        if len(digit) == 3:
            return digit


def find_eight(encrypted_digits):
    for digit in encrypted_digits:
        if len(digit) == 7:
            return digit


# three has length 5 is a seven + two more entries
def find_three(encrypted_digits, seven):
    for digit in encrypted_digits:
        if len(digit) == 5:
            is_three = True
            for letter in seven:
                if letter not in digit:
                    is_three = False
                    break
            if is_three:
                return digit


# nine is length 6 and contains 4
def find_nine(encrypted_digits, four):
    for digit in encrypted_digits:
        if len(digit) == 6:
            is_nine = True
            for letter in four:
                if letter not in digit:
                    is_nine = False
                    break
            if is_nine:
                return digit


# has 6 letters and does contain exactly one letter of 'one'
def find_six(encrypted_digits, one):
    for digit in encrypted_digits:
        if len(digit) == 6:
            not_in_digit = 0
            for letter in one:
                if letter not in digit:
                    not_in_digit += 1
            if not_in_digit == 1:
                return digit


# zero has 6 letters and it does contain all letters from 3 except for one
def find_zero(encrypted_digits, three):
    for digit in encrypted_digits:
        if len(digit) == 6:
            not_in_digit = 0
            for letter in three:
                if letter not in digit:
                    not_in_digit += 1
            if not_in_digit == 1:
                return digit


# five has 5 letters and contains all letters from six except one
def find_five(encrypted_digits, six):
    for digit in encrypted_digits:
        if len(digit) == 5:
            is_five = False
            for letter in six:
                if letter not in digit:
                    return digit
                else:
                    is_five = False
            if is_five:
                return digit


def determine_config(keys):
    config = []
    # a is in 7 but not in 1
    # b is in 4 but not in 3
    # c is in 8 but not in 6
    # d is in 8 but not in 0
    # e is in 8 but not in 9
    # f is in 1 but not in 2
    # g is in 9 but not in 4 and not in 7
    config.append(keys[7].difference(keys[1]))
    config.append(keys[4].difference(keys[3]))
    config.append(keys[8].difference(keys[6]))
    config.append(keys[8].difference(keys[0]))
    config.append(keys[8].difference(keys[9]))
    config.append(keys[1].difference(keys[2]))
    config.append(keys[9].difference(keys[4], keys[7]))
    config_list = []
    for entry in config:
        config_list.append(list(entry)[0])
    return config_list


def decrypt_row(encrypted):
    input_copy = encrypted.copy()
    one = find_one(input_copy)
    input_copy.remove(one)
    four = find_four(input_copy)
    input_copy.remove(four)
    seven = find_seven(input_copy)
    input_copy.remove(seven)
    eight = find_eight(input_copy)
    input_copy.remove(eight)
    three = find_three(input_copy, seven)
    input_copy.remove(three)
    nine = find_nine(input_copy, four)
    input_copy.remove(nine)
    six = find_six(input_copy, one)
    input_copy.remove(six)
    zero = find_zero(input_copy, three)
    input_copy.remove(zero)
    five = find_five(input_copy, six)
    input_copy.remove(five)
    two = input_copy[0]
    config = determine_config([set(zero), set(one), set(two), set(three), set(four), set(five), set(six), set(seven), set(eight), set(nine)])
    visualize_config(config)
    return [set(zero), set(one), set(two), set(three), set(four), set(five), set(six), set(seven), set(eight), set(nine)]
    # return config


def decrypt_value(second_part, key):
    value_string = ""
    print(key)

    for entry in second_part:
        print("entry:",entry)
        entry_set = set(entry)
        if entry_set == key[0]:
            value_string += "0"
        elif entry_set == key[1]:
            value_string += "1"
        elif entry_set == key[2]:
            value_string += "2"
        elif entry_set == key[3]:
            value_string += "3"
        elif entry_set == key[4]:
            value_string += "4"
        elif entry_set == key[5]:
            value_string += "5"
        elif entry_set == key[6]:
            value_string += "6"
        elif entry_set == key[7]:
            value_string += "7"
        elif entry_set == key[8]:
            value_string += "8"
        elif entry_set == key[9]:
            value_string += "9"
    print(int(value_string))
    return int(value_string, 10)


def decrypt_all(first_part, second_part):
    sum = 0
    for index in range(len(first_part)):
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(first_part[index]," | ",second_part[index])
        key = decrypt_row(first_part[index])
        value = decrypt_value(second_part[index], key)
        sum += value
    print(len(first_part))
    print(len(second_part))
    return sum


first_part, second_part = parse_input(data)
print(decrypt_all(first_part, second_part))
# 1080272 too high
# right answer: 1063760