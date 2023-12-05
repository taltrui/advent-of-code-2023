import re

file_path = "./input.txt"

gamesList = []


def part_1(games):
    sum = 0
    for game in games:
        redOverLimit = any(x > 12 for x in game["reds"])
        blueOverLimit = any(x > 14 for x in game["blues"])
        greenOverLimit = any(x > 13 for x in game["greens"])

        possible = not redOverLimit and not blueOverLimit and not greenOverLimit
        if possible:
            sum += game["id"]

    print(f"Part 1 answer: {sum}")


def part_2(games):
    sum = 0
    for game in games:
        maxRed = max(game["reds"])
        maxBlue = max(game["blues"])
        maxGreen = max(game["greens"])

        sum += maxRed * maxBlue * maxGreen

    print(f"Part 2 answer: {sum}")


try:
    file = open(file_path, "r")
    lines = file.readlines()

    for line in lines:
        cubes = re.findall(
            r"(\d+(?= red))|(\d+(?= blue))|(\d+(?= green))",
            line,
        )

        id = re.search("\d+(?=:)", line).group()

        greens = []
        blues = []
        reds = []
        for colors in cubes:
            [red, blue, green] = colors
            greens.append(int(green)) if green != "" else None
            reds.append(int(red)) if red != "" else None
            blues.append(int(blue)) if blue != "" else None

        gamesList.append(
            {"id": int(id), "reds": reds, "greens": greens, "blues": blues}
        )

    part_1(gamesList)
    part_2(gamesList)

    file.close()
except FileNotFoundError:
    print("File not found.")
