from utils import aslist, splitlines, ingroups, getday, getpath

SAVE_LINES = False


def proccessEnd(line, saveLines=False):
    nextLine = []
    curr = [int(x) for x in line.split(" ")]

    lines = []
    ends = [curr[-1]]

    cnt = 0
    while not all(x == 0 for x in curr):
        cnt += 1
        nextLine = []
        if saveLines:
            lines.append(curr)
        for i in range(len(curr) - 1):
            nextLine.append(curr[i + 1] - curr[i])

        if not all(x == 0 for x in nextLine):
            ends.append(nextLine[-1])

        elif saveLines:
            lines.append(nextLine)

        curr = nextLine

    end = 0

    for li in lines:
        print(li)

    for i in range(len(ends) - 1, -1, -1):
        val = ends[i] + end
        end = val

    return val


def processStart(line, saveLines=False):
    nextLine = []
    curr = [int(x) for x in line.split(" ")]

    lines = []
    starts = [curr[0]]

    cnt = 0
    while not all(x == 0 for x in curr):
        cnt += 1
        nextLine = []
        if saveLines:
            lines.append(curr)
        for i in range(len(curr) - 1):
            nextLine.append(curr[i + 1] - curr[i])

        if not all(x == 0 for x in nextLine):
            starts.append(nextLine[0])

        elif saveLines:
            lines.append(nextLine)

        curr = nextLine

    start = 0

    for li in lines:
        print(li)

    for i in range(len(starts) - 1, -1, -1):
        val = starts[i] - start
        start = val

    return start


def part1(lines):
    total = 0
    for line in lines:
        total += proccessEnd(line, saveLines=SAVE_LINES)

    return total


def part2(lines):
    tv = 0
    for line in lines:
        val = processStart(line, saveLines=SAVE_LINES)
        tv += val

    return tv


path = getpath(__file__)
with open("{}/day9.txt".format(path), "r") as f:
    lines = f.readlines()

    lines = aslist(lines)

    SAVE_LINES = False

    p1 = part1(lines)  # 1987402313
    p2 = part2(lines)  # 900

    print(p1)
    print(p2)

    assert p1 == 1987402313
    assert p2 == 900
