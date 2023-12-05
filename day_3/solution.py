file_path = "./input.txt"


adjacentpos = [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1]]


def isCharValid(matrix, charI, vectorI):
    currPos = [vectorI, charI]
    valid = False
    for pos in adjacentpos:
        try:
            char = matrix[currPos[0] + pos[0]][currPos[1] + pos[1]]
            if not char.isalnum() and char != ".":
                valid = True
        except:
            None

    return valid


def getFullRatioNumber(matrix, pos):
    initialNumber = matrix[pos[0]][pos[1]]
    rightDigit = None
    currentPos = pos[1]
    leftDigit = None
    while rightDigit != -1:
        if currentPos + 1 > len(matrix[pos[0]]) - 1:
            currentPos = pos[1]
            rightDigit = -1
            break

        char = matrix[pos[0]][currentPos + 1]
        if char.isdigit():
            initialNumber = f"{initialNumber}{char}"
            currentPos = currentPos + 1
        else:
            currentPos = pos[1]
            rightDigit = -1

    while leftDigit != -1:
        if currentPos - 1 < 0:
            leftDigit = -1
            break
        char = matrix[pos[0]][currentPos - 1]
        if char.isdigit():
            initialNumber = f"{char}{initialNumber}"
            currentPos = currentPos - 1
        else:
            currentPos = pos[1]
            leftDigit = -1

    return int(initialNumber)


def getGearRatios(matrix, i, j):
    firstRatioInitialPos = None
    secondRatioInitialPos = None
    for pos in adjacentpos:
        char = matrix[i + pos[0]][j + pos[1]]
        if char.isdigit():
            if firstRatioInitialPos == None:
                firstRatioInitialPos = [i + pos[0], j + pos[1]]
                continue

            if firstRatioInitialPos[0] == i + pos[0]:
                if (
                    firstRatioInitialPos[1] + 1 == j + pos[1]
                    or firstRatioInitialPos[1] - 1 == j + pos[1]
                ):
                    continue

            if secondRatioInitialPos == None:
                secondRatioInitialPos = [i + pos[0], j + pos[1]]
                continue

    firstRatio = (
        getFullRatioNumber(matrix, firstRatioInitialPos)
        if firstRatioInitialPos != None
        else 0
    )
    secondRatio = (
        getFullRatioNumber(matrix, secondRatioInitialPos)
        if secondRatioInitialPos != None
        else 0
    )

    print(firstRatio, secondRatio)

    return firstRatio * secondRatio


def part_1(matrix):
    sum = 0
    currentNum = None
    currentNumValid = False

    for i, vector in enumerate(matrix):
        for j, char in enumerate(vector):
            if char.isdigit():
                currentNum = char if currentNum is None else f"{currentNum}{char}"
                currentNumValid = (
                    isCharValid(matrix, j, i) if currentNumValid is False else True
                )

            if not char.isdigit():
                if currentNumValid:
                    sum += int(currentNum)

                currentNumValid = False
                currentNum = None

    print(sum)


def part_2(matrix):
    sum = 0
    numofgears = 0
    numofratio = 0
    for i, vector in enumerate(matrix):
        for j, char in enumerate(vector):
            if char == "*":
                numofgears += 1

                ratio = getGearRatios(matrix, i, j)

                if ratio > 0:
                    numofratio += 1

                sum += ratio

    print(sum)
    print(numofratio)
    print(numofgears)


schemeMatrix = []
try:
    file = open(file_path, "r")
    lines = file.readlines()

    for line in lines:
        schemeMatrix.append(list(filter(lambda x: x != "\n", [*line])))

    part_1(schemeMatrix)
    part_2(schemeMatrix)

    file.close()
except FileNotFoundError:
    print("File not found.")
