from util.fileReader import read_strings

sample = read_strings(open("sample"))
data = read_strings(open("input"))


# part 1
def determine_position(steps):
    forward = 0
    depth = 0
    for step in steps:
        if step.startswith("forward"):
            forward += int(step.split(" ")[1])
        elif step.startswith("up"):
            depth -= int(step.split(" ")[1])
        elif step.startswith("down"):
            depth += int(step.split(" ")[1])
    return forward * depth


# solution part 1:
print(determine_position(data))


# part 2
def determine_real_position(steps):
    aim = 0
    forward = 0
    depth = 0
    for step in steps:
        units = int(step.split(" ")[1])
        if step.startswith("forward"):
            forward += units
            depth += aim * units
        elif step.startswith("up"):
            aim -= units
        elif step.startswith("down"):
            aim += units
    return forward * depth


# solution part 2:
print(determine_real_position(data))
