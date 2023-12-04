from utils import aslist, splitlines, ingroups, getday, getpath
import re
import math


def part1(lines):
    total = 0
    for line in lines:
        line = re.sub(r"\s+", " ", line)
        parts = line.split(" | ")
        winningNums = parts[0].split(": ")[1].split(" ")
        myNums = parts[1].split(" ")

        myNums = [int(num) for num in myNums]
        winningNums = [int(num) for num in winningNums]

        correct = 0
        for num in myNums:
            if num in winningNums:
                correct += 1
        total += math.floor(2 ** (correct - 1))
    print(total)

    return total


def part2(lines):
    total = 0
    multiples = {}
    for row, line in enumerate(lines):
        if row not in multiples:
            multiples[row] = 1
        line = re.sub(r"\s+", " ", line)
        parts = line.split(" | ")
        winningNums = parts[0].split(": ")[1].split(" ")
        myNums = parts[1].split(" ")

        myNums = [int(num) for num in myNums]
        winningNums = [int(num) for num in winningNums]

        correct = 0
        for num in myNums:
            if num in winningNums:
                correct += 1

        multiplier = 1
        if row in multiples:
            multiplier = multiples[row]

        for x in range(1, correct + 1):
            if row + x not in multiples:
                multiples[row + x] = 1
            multiples[row + x] += multiplier

    total = 0
    for v in multiples.values():
        total += v
    print(total)
    return total


path = getpath(__file__)
with open("{}/day4.txt".format(path), "r") as f:
    lines = f.readlines()

    lines = aslist(lines)

    part1(lines)  # 21959
    part2(lines)  # 5132675
