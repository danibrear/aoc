from utils import aslist, splitlines, ingroups, getday, getpath


def isReflection(row, i):
    back = i - 1
    forward = i

    if back < 0 or forward >= len(row):
        return False

    while back >= 0 and forward < len(row):
        if row[back] != row[forward]:
            return False
        back -= 1
        forward += 1

    return True


def getReflections(section):
    h_reflections = []
    v_reflections = []
    for i, row in enumerate(section):
        for j, col in enumerate(row):
            if isReflection(row, j):
                # print("row", i, row[:j], row[j:][::-1])
                h_reflections.append((i, j))
    for j in range(len(section[0])):
        col = "".join([row[j] for row in section])
        for i in range(len(col)):
            if isReflection(col, i):
                v_reflections.append((i, j))
    return h_reflections, v_reflections


def part1(lines):
    sections = []
    current_section = []
    for line in lines:
        if line == "":
            sections.append(current_section)
            current_section = []
        else:
            current_section.append(line)
    sections.append(current_section)

    total = 0

    for s, section in enumerate(sections):
        h_ref, v_ref = getReflections(section)
        h_mirror = 0
        v_mirror = 0
        for i in range(len(section[0])):
            has = True
            for j in range(len(section)):
                if (j, i) not in h_ref:
                    has = False
                    break
            if has:
                h_mirror = i
                break
        for r in range(len(section)):
            has = True
            for c in range(len(section[0])):
                if (r, c) not in v_ref:
                    has = False
                    break
            if has:
                v_mirror = r
                break

        if v_mirror == 0 and h_mirror == 0:
            print("no mirror", s)
        total += v_mirror * 100 + h_mirror
    print(total)


def part2(lines):
    sections = []
    current_section = []
    for line in lines:
        if line == "":
            sections.append(current_section)
            current_section = []
        else:
            current_section.append(line)
    sections.append(current_section)

    total = 0

    for s, section in enumerate(sections):
        smudges = []
        for i, row in enumerate(section):
            for j, col in enumerate(row):
                if col == "#":
                    smudges.append((i, j))
        found = False
        for smudge in smudges:
            (r, c) = smudge
            _section = section.copy()
            _section[r] = [y for y in _section[r]]
            _section[r][c] = "."
            _section[r] = "".join(_section[r])
            h_ref, v_ref = getReflections(_section)
            h_mirror = 0
            v_mirror = 0
            for i in range(len(_section[0])):
                has = True
                for j in range(len(_section)):
                    if (j, i) not in h_ref:
                        has = False
                        break
                if has:
                    h_mirror = i
                    break
            for r in range(len(_section)):
                has = True
                for c in range(len(_section[0])):
                    if (r, c) not in v_ref:
                        has = False
                        break
                if has:
                    v_mirror = r
                    break

            if v_mirror != 0 or h_mirror != 0:
                print("for section", s, "smudge", smudge)
                for l in _section:
                    print(l)
                total += v_mirror * 100 + h_mirror
                found = True
                break
        if not found:
            print("no mirror for", section)
    print(total)


testlines = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
testlines2 = """#..#.#........#
#..######..####
.##..#.#.##.#.#
#..##..........
######........#
#..####......##
.##.##.#...##.#
"""

path = getpath(__file__)
with open("{}/day13.txt".format(path), "r") as f:
    # lines = f.readlines()
    lines = testlines.splitlines()
    # lines = testlines2.splitlines()

    lines = aslist(lines)

    part1(lines)
    part2(lines)
