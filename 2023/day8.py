from utils import aslist, splitlines, ingroups, getday, getpath

def part1(lines):
    for line in lines:
        pass

def part2(lines):
    for line in lines:
        pass


day = getday(__file__)
path = getpath(__file__)
with open('{}/{}.txt'.format(path, day), 'r') as f:

    lines = f.readlines()

    lines = aslist(lines)

    part1(lines)
    part2(lines)