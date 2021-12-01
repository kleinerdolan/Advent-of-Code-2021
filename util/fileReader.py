def readNumbers(inputFile):
    numbers = []
    for line in inputFile:
        numbers.append(int((line.strip())))
    return numbers