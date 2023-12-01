import re

file_path = "./input.txt"


def part_1(line):
    numbers = re.findall("\d", line)
    number = numbers[0] + numbers[-1]

    return int(number)


def part_2(line):
    return part_1(
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )


try:
    file = open(file_path, "r")
    lines = file.readlines()

    part_1_sum = 0
    part_2_sum = 0

    for line in lines:
        part_1_sum += part_1(line)
        part_2_sum += part_2(line)

    print(f"Part 1 sum is: {part_1_sum}")
    print(f"Part 2 sum is: {part_2_sum}")
    file.close()
except FileNotFoundError:
    print("File not found.")
