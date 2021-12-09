import copy

from util.fileReader import read_strings, read_matrix, print_2d_list

sample_string = read_strings(open("sample"))
data_string = read_strings(open("input"))


def convert_to_int(string_list_of_lists):
    int_list = []
    for y in range(len(string_list_of_lists)):
        int_row = []
        for x in range(len(string_list_of_lists[0])):
            int_row.append(int(string_list_of_lists[y][x]))
        int_list.append(int_row)
    return int_list


sample = convert_to_int(read_matrix(sample_string))
data = convert_to_int(read_matrix(data_string))


def is_lowpoint(x, y, map):
    cur_point = map[y][x]
    # check top
    if y > 0:
        if map[y-1][x] <= cur_point:
            return False
    # check right
    if x < len(map[0]) - 1:
        if map[y][x+1] <= cur_point:
            return False
    # check bottom
    if y < len(map) - 1:
        if map[y+1][x] <= cur_point:
            return False
    # check left
    if x > 0:
        if map[y][x-1] <= cur_point:
            return False
    return True


def find_lows(map):
    lows = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if is_lowpoint(x, y, map):
                lows.append(int(map[y][x]))
                map[y][x] = 0
    return lows


def calculate_risk(lows):
    return sum(lows) + len(lows)


# solution part 1:
# print(calculate_risk(find_lows(data)))


# part 2:
def mark_basin(orig_map, x, y):
    cur_map = copy.copy(orig_map)
    marked_fields = 0
    # print("checking [" + str(x) + "][" + str(y) + "]")
    # check top
    for y_dif in range(1, y + 1):
        # print("top [" + str(x) + "][" + str(y - y_dif) + "]")
        if 0 < cur_map[y - y_dif][x] < 9:
            cur_map[y - y_dif][x] = 0
            marked_fields += 1
            # print("recursion top")
            marked_fields += mark_basin(cur_map, x, y - y_dif)
        else:
            break
    # check left
    for x_dif in range(1, x + 1):
        # print("left [" + str(x - x_dif) + "][" + str(y) + "]")
        if 0 < cur_map[y][x - x_dif] < 9:
            cur_map[y][x - x_dif] = 0
            marked_fields += 1
            # print("recursion left")
            marked_fields += mark_basin(cur_map, x - x_dif, y)
        else:
            break
    # check bottom
    for y_dif in range(1, len(cur_map) - y):
        # print("bottom [" + str(x) + "][" + str(y + y_dif) + "]")
        if 0 < cur_map[y + y_dif][x] < 9:
            cur_map[y + y_dif][x] = 0
            marked_fields += 1
            # print("recursion bottom")
            marked_fields += mark_basin(cur_map, x, y + y_dif)
        else:
            break
    # check right
    for x_dif in range(1, len(cur_map[0]) - x):
        # print("right [" + str(x + x_dif) + "][" + str(y) + "]")
        if 0 < cur_map[y][x + x_dif] < 9:
            cur_map[y][x + x_dif] = 0
            marked_fields += 1
            # print("recursion right")
            marked_fields += mark_basin(cur_map, x + x_dif, y)
        else:
            break
    return marked_fields


def find_basins(map):
    basins = []
    find_lows(map)
    basin_map = copy.deepcopy(map)
    # mark all fields next to 0s, except they are 9
    for y in range(len(basin_map)):
        for x in range(len(basin_map[0])):
            if basin_map[y][x] == 0:
                marked = mark_basin(copy.deepcopy(basin_map), x, y)
                marked += 1 # because we marked the lowpoint earlier
                basins.append(marked)
    return basins


def calculate_result(basins):
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


# solution part 2:
print(calculate_result(find_basins(data)))
