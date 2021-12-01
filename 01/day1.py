from util.fileReader import readNumbers

formatted_input = readNumbers(open("input"))
sample = readNumbers(open("sample"))


# part 1
def count_increases(data):
    increases = 0
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            increases += 1
    return increases


# solution part 1:
print(count_increases(formatted_input))


# part 2
def generate_windows(data):
    increase_windows = []
    for i in range(len(data) - 2):
        increase_windows.append(data[i] + data[i + 1] + data[i + 2])
    return increase_windows


# solution part 2:
print(count_increases(generate_windows(formatted_input)))
