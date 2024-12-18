from utils import aslist, splitlines, ingroups, getday, getpath
import re

from tools import minWithIndex

print(minWithIndex([100, 50, 25, 70, 300]))

arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
arr2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def part1(lines):
    total = 0
    for line in lines:
        first = 0
        second = 0
        numbers = []
        for i in range(len(line)):
            for num in arr:
                if line[i:].startswith(num):
                    numbers.append(num)
                    break
        first = numbers[0]
        second = numbers[-1]

        total += int(first) * 10 + int(second)
    print(total)
    pass


def part2(lines):
    total = 0
    totalArr = arr + arr2
    for line in lines:
        first = 0
        second = 0
        numbers = []
        for i in range(len(line)):
            for num in totalArr:
                if line[i:].startswith(num):
                    if (num in arr2):
                        numbers.append(arr2.index(num) + 1)
                    else:
                        numbers.append(num)

        first = numbers[0]
        second = numbers[-1]

        total += int(first) * 10 + int(second)
    print(total)

day = getday(__file__)
path = getpath(__file__)
with open('{}/day1.txt'.format(path), 'r') as f:

    lines = f.readlines()

    lines = aslist(lines)

    part1(lines) # 54601
    part2(lines) # 54078