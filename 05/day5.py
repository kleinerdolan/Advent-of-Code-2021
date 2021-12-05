from util.fileReader import read_strings

sample = read_strings(open("sample"))
data = read_strings(open("input"))


def print_map(map):
    for y in range(len(map)):
        row_string = ""
        for x in range(len(map)):
            if map[x][y] == 0:
                row_string += ". "
            else:
                row_string += str(map[x][y])
                row_string += " "
        print(row_string)


def determine_dimensions(coordinates):
    all_instructions = []
    max = 0
    for instruction in coordinates:
        for point in instruction.split(" -> "):
            all_instructions.append(point)
    for point in all_instructions:
        for coordinate in point.split(","):
            if int(coordinate) > max:
                max = int(coordinate)

    # +1 since the map starts at coordinate 0,0
    return max + 1


def initialize_map(max):
    list_2d = [[0] * max for i in range(max)]
    return list_2d


# a line is valid if it is straight
def validate_line(start_string, end_string):
    start = convert_to_numbers(start_string)
    end = convert_to_numbers(end_string)
    if start[0] == end[0] or start[1] == end[1]:
        return True
    return False


def convert_to_numbers(string_point):
    string_point = string_point.split(",")
    x = int(string_point[0])
    y = int(string_point[1])
    return [x, y]


def determine_line_coordinates(start_string, end_string):
    start = convert_to_numbers(start_string)
    end = convert_to_numbers(end_string)
    line_coordinates = []
    # vertical line
    if start[0] == end[0]:
        if end[1] > start[1]:
            for y in range(start[1], end[1] + 1):
                line_coordinates.append([start[0], y])
        else:
            for y in range(end[1], start[1] + 1):
                line_coordinates.append([end[0], y])
    # horizontal line
    else:
        if end[0] > start[0]:
            for x in range(start[0], end[0] + 1):
                line_coordinates.append([x, start[1]])
        else:
            for x in range(end[0], start[0] + 1):
                line_coordinates.append([x, end[1]])
    return line_coordinates


def enter_instructions(map, instructions):
    for line in instructions:
        start, end = line.split(" -> ")
        if validate_line(start, end):
            line_coordinates = determine_line_coordinates(start, end)
            for coordinate in line_coordinates:
                map[coordinate[0]][coordinate[1]] += 1


def determine_overlaps(map):
    overlaps = 0
    for row in map:
        for column in row:
            if column > 1:
                overlaps += 1
    return overlaps


# solution part 1:
# map = initialize_map(determine_dimensions(data))
# enter_instructions(map, data)
# print(determine_overlaps(map))

# part 2:
def validate_line_with_diagonal(start_string, end_string):
    start = convert_to_numbers(start_string)
    end = convert_to_numbers(end_string)
    if start[0] == end[0] or start[1] == end[1]:
        return True
    elif abs(start[0] - end[0]) == abs(start[1] - end[1]):
        print("diagonal: ", start, " -> ", end)
        return True
    return False


def enter_instructions_with_diagonals(map, instructions):
    for line in instructions:
        start, end = line.split(" -> ")
        if validate_line_with_diagonal(start, end):
            line_coordinates = determine_line_coordinates_with_diagonals(start, end)
            for coordinate in line_coordinates:
                map[coordinate[0]][coordinate[1]] += 1


def determine_line_coordinates_with_diagonals(start_string, end_string):
    start = convert_to_numbers(start_string)
    end = convert_to_numbers(end_string)
    line_coordinates = []
    # vertical line
    if start[0] == end[0]:
        if end[1] > start[1]:
            for y in range(start[1], end[1] + 1):
                line_coordinates.append([start[0], y])
        else:
            for y in range(end[1], start[1] + 1):
                line_coordinates.append([end[0], y])
    # horizontal line
    elif start[1] == end[1]:
        if end[0] > start[0]:
            for x in range(start[0], end[0] + 1):
                line_coordinates.append([x, start[1]])
        else:
            for x in range(end[0], start[0] + 1):
                line_coordinates.append([x, end[1]])
    # right up (x+, Y-)
    elif start[0] < end[0] and start[1] < end[1]:
        cur_x = end[0]
        cur_y = end[1]
        while cur_x > start[0] - 1 and cur_y > start[1] - 1:
            line_coordinates.append([cur_x, cur_y])
            cur_x -= 1
            cur_y -= 1
    # right down (x+, y+)
    elif start[0] < end[0] and start[1] > end[1]:
        cur_x = end[0]
        cur_y = end[1]
        while cur_x > start[0] - 1 and cur_y < start[1] + 1:
            line_coordinates.append([cur_x, cur_y])
            cur_x -= 1
            cur_y += 1
    # left down (x-, Y+)
    elif start[0] > end[0] and start[1] < end[1]:
        cur_x = start[0]
        cur_y = start[1]
        while cur_x > end[0] - 1 and cur_y < end[1] + 1:
            line_coordinates.append([cur_x, cur_y])
            cur_x -= 1
            cur_y += 1
    # left up (x-, y-)
    elif start[0] > end[0] and start[1] > end[1]:
        cur_x = start[0]
        cur_y = start[1]
        while cur_x > end[0] - 1 and cur_y > end[1] - 1:
            line_coordinates.append([cur_x, cur_y])
            cur_x -= 1
            cur_y -= 1
    return line_coordinates

# solution part 2:
map = initialize_map(determine_dimensions(data))
enter_instructions_with_diagonals(map, data)
print_map(map)
print(determine_overlaps(map))
