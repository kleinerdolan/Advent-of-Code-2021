from re import match

from util.fileReader import read_strings

sample = read_strings(open("sample"))
data = read_strings(open("input"))


# part 1
def determine_position(steps):
    forward = depth = 0
    for step in steps:
        command, value = step.split()
        value = int(value)
        if command == "forward":
            forward += value
        elif command == "up":
            depth -= value
        elif command == "down":
            depth += value
    return forward * depth


# solution part 1:
print(determine_position(data))


# part 2
def determine_real_position(steps):
    aim = forward = depth = 0
    for step in steps:
        match step.split():
            case "forward", value:
                forward += int(value)
                depth += aim * int(value)
            case "up", value:
                aim -= int(value)
            case "down", value:
                aim += int(value)
    return forward * depth


# solution part 2:
print(determine_real_position(data))
# 1868935
# 1965970888