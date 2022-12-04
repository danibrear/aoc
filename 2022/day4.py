
from utils import aslist


def part1(lines):
    count = 0
    for line in lines:
        e1, e2 = line.split(',')
        e1start, e1end = e1.split('-')
        e2start, e2end = e2.split('-')

        if int(e1start) <= int(e2start) and int(e1end) >= int(e2end):
            count += 1
        elif int(e2start) <= int(e1start) and int(e2end) >= int(e1end):
            count += 1
    print(count)


def part2(lines):
    count = 0
    for line in lines:
        e1, e2 = line.split(',')
        e1start, e1end = e1.split('-')
        e2start, e2end = e2.split('-')

        if int(e1start) <= int(e2start) <= int(e1end):
            count += 1
        elif int(e2start) <= int(e1start) <= int(e2end):
            count += 1
    print(count)


with open('day4.txt', 'r') as f:

    lines = f.readlines()
    lines = aslist(lines)

    part1(lines)  # 605
    part2(lines)  # 914
