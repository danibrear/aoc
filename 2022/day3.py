
from utils import aslist, grouped

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = [x.upper() for x in lower]


def part1(lines):
    at = 0
    for line in lines:
        first = line[:len(line)//2]
        second = line[len(line)//2:]
        same = set()
        for x in first:
            if x in second:
                same.add(x)
        char = list(same)[0]
        total = 0
        idx = 0
        if char in lower:
            idx = lower.index(char) + 1
        else:
            idx = upper.index(char) + 27
        total += idx

        at += total

    print(at)


def part2(lines):
    groups = grouped(lines, 3)
    total = 0
    for group in groups:
        [g1, g2, g3] = group
        same = set()
        for x in g1:
            if x in g2 and x in g3:
                same.add(x)
                break
        char = list(same)[0]

        if char in lower:
            total += lower.index(char) + 1
        else:
            total += upper.index(char) + 27

    print(total)


with open('day3.txt', 'r') as f:

    lines = f.readlines()
    lines = aslist(lines)

    part1(lines)
    part2(lines)
