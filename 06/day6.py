from util.fileReader import read_strings

data = read_strings(open("input"))
sample = read_strings(open("sample"))


def read_population(num_list):
    num_list = num_list[0].split(",")
    nums_by_occurrence = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in num_list:
        nums_by_occurrence[int(num)] += 1
    return nums_by_occurrence


def evolution_step(population):
    new_population = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(population)):
        new_population[(i - 1) % 9] += population[i]
        if i == 0 and population[0] > 0:
            new_population[6] += population[i]
    return new_population


def simulate_evolution_for_days(population_string, days):
    population = read_population(population_string)
    for day in range(days):
        population = evolution_step(population)
    return sum(population)


# solution part 1:
print(simulate_evolution_for_days(data, 80))
# solution part 2:
print(simulate_evolution_for_days(data, 256))
