from utils import aslist, splitlines, ingroups, getday, getpath
import math


def part1(lines):
    instructions = lines[0]

    maps = {}
    at = "AAA"
    for line in lines[2:]:
        parts = line.split(" = ")

        p1 = parts[1].replace("(", "")
        p1 = p1.replace(")", "")
        dirs = p1.split(", ")
        maps[parts[0]] = dirs

    inst = 0
    step = 0
    while at != "ZZZ":
        d = instructions[inst]
        if d == "L":
            at = maps[at][0]
        elif d == "R":
            at = maps[at][1]
        inst += 1
        inst %= len(instructions)
        step += 1

    return step


def part2(lines):
    instructions = lines[0]
    maps = {}
    for line in lines[2:]:
        parts = line.split(" = ")
        dirs = parts[1].replace("(", "").replace(")", "").split(", ")
        maps[parts[0]] = dirs

    ats = []
    for k in maps.keys():
        if k.endswith("A"):
            ats.append(k)

    atsWithZ = {}
    for a in ats:
        atsWithZ[a] = set()
    for a in ats:
        inst = 0
        seen = set()
        find = a

        step = 0

        while "{}-{}".format(find, inst) not in seen:
            seen.add("{}-{}".format(find, inst))
            if find.endswith("Z"):
                atsWithZ[a].add(step)
            if instructions[inst] == "L":
                find = maps[find][0]
            else:
                find = maps[find][1]

            inst += 1
            inst %= len(instructions)
            step += 1

    values = [v.pop() for v in atsWithZ.values()]

    return math.lcm(*values)


path = getpath(__file__)
with open("{}/day8.txt".format(path), "r") as f:
    lines = f.readlines()

    lines = aslist(lines)

    p1 = part1(lines)  # 13301
    p2 = part2(lines)

    print(p1)
    print(p2)

    assert p1 == 13301
    assert p2 == 7309459565207
