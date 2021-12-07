import sys

from util.fileReader import read_strings


def to_ordered_list(string):
    string_list = string[0].split(",")
    nums = []
    for entry in string_list:
        nums.append(int(entry))
    nums.sort()
    return nums


data = to_ordered_list(read_strings(open("input")))
sample = to_ordered_list(read_strings(open("sample")))


def caluculate_cost_by_median(list):
    median = list[round(len(list) / 2)]
    total_cost = 0
    for entry in list:
        total_cost += abs(median - entry)
    return total_cost


# solution part 1:
print(caluculate_cost_by_median(data))

#part 2:
def calculate_average(list):
    total_sum = 0
    for entry in list:
        total_sum += entry
    return int(total_sum / len(list))


def calculate_path_cost(start, end):
    steps = 0
    cost = 0
    if start > end:
        steps = start - end
    else:
        steps = end - start
    for increasing_cost in range(1, steps + 1):
        cost += increasing_cost
    # print("cost (",start,"->",end,"(",steps,") = ", cost)
    return cost


def caluculate_cost(list):
    average = calculate_average(list)
    total_cost = sys.maxsize
    for guess in range(average - 2, average + 3):
        current_total = 0
        for entry in list:
            current_total += calculate_path_cost(entry, guess)
        if current_total < total_cost:
            total_cost = current_total
    return total_cost


# solution part 2:
print(caluculate_cost(data))
