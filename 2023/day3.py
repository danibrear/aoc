from utils import aslist, splitlines, ingroups, getday, getpath

def isNumber(char):
    return char.isdigit()

def part1(lines):
    parts = []
    for row, line in enumerate(lines):
        isPart = False
        part = None
        for col, char in enumerate(line):
            if char == '.':
                if isPart:
                    parts.append(part)
                    isPart = False
                part = None

            if isNumber(char):
                if part is None:
                    part = [char]
                else:
                    part.append(char)
                if not isPart:
                    if col > 0 and not isNumber(line[col - 1]) and line[col - 1] != '.':
                        isPart = True
                    if col < len(line) - 1 and not isNumber(line[col + 1]) and line[col + 1] != '.':
                        isPart = True
                    if row > 0 and not isNumber(lines[row - 1][col]) and lines[row - 1][col] != '.':
                        isPart = True
                    if row < len(lines) - 1 and not isNumber(lines[row + 1][col]) and lines[row + 1][col] != '.':
                        isPart = True
                    if col > 0 and row > 0 and not isNumber(lines[row - 1][col - 1]) and lines[row - 1][col - 1] != '.':
                        isPart = True
                    if col > 0 and row < len(lines) - 1 and not isNumber(lines[row + 1][col - 1]) and lines[row + 1][col - 1] != '.':
                        isPart = True
                    if col < len(line) - 1 and row > 0 and not isNumber(lines[row - 1][col + 1]) and lines[row - 1][col + 1] != '.':
                        isPart = True
                    if col < len(line) - 1 and row < len(lines) - 1 and not isNumber(lines[row + 1][col + 1]) and lines[row + 1][col + 1] != '.':
                        isPart = True
            else:
                if isPart:
                    parts.append(part)
                    isPart = False
                part = None
        if isPart:
            parts.append(part)
    total = 0

    for part in parts:
        n = ''.join(part)
        total += int(n)
    print(total)


def part2(lines):
    gears = []
    for row, line in enumerate(lines):
        for col, l in enumerate(line):
            adjParts = 0
            hasUp = False
            hasDown = False
            if l == '*':
                if col > 0 and isNumber(line[col - 1]):
                    adjParts += 1
                if col < len(line) - 1 and isNumber(line[col + 1]):
                    adjParts += 1
                if row > 0 and isNumber(lines[row - 1][col]) and lines[row - 1][col] != '.':
                    adjParts += 1
                    hasUp = True
                if row < len(lines) - 1 and isNumber(lines[row + 1][col]) and lines[row + 1][col] != '.':
                    adjParts += 1
                    hasDown = True
                if col > 0 and row > 0 and isNumber(lines[row - 1][col - 1]) and not hasUp:
                    adjParts += 1
                if col > 0 and row < len(lines) - 1 and isNumber(lines[row + 1][col - 1]) and not hasDown:
                    adjParts += 1
                if col < len(line) - 1 and row > 0 and isNumber(lines[row - 1][col + 1]) and not hasUp:
                    adjParts += 1
                if col < len(line) - 1 and row < len(lines) - 1 and isNumber(lines[row + 1][col + 1]) and not hasDown:
                    adjParts += 1
                if adjParts == 2:
                    gears.append([row, col])

    touchingGears = {}
    for row, line in enumerate(lines):
        part = None
        isTouchingGear = None
        for col, char in enumerate(line):
            if char == '.':
                if isTouchingGear is not None:
                    if isTouchingGear not in touchingGears:
                        touchingGears[isTouchingGear] = []
                    touchingGears[isTouchingGear].append(part)
                    isTouchingGear = None
                part = None

            if isNumber(char):
                if part is None:
                    part = [char]
                else:
                    part.append(char)
                if not isTouchingGear:
                    if col > 0 and [row, col - 1] in gears:
                        isTouchingGear = (row, col - 1)
                    if col < len(line) - 1 and [row, col + 1] in gears:
                        isTouchingGear = (row, col + 1)
                    if row > 0 and [row - 1, col] in gears:
                        isTouchingGear = (row - 1, col)
                    if row < len(lines) - 1 and [row + 1, col] in gears:
                        isTouchingGear = (row + 1, col)
                    if col > 0 and row > 0 and [row - 1, col - 1] in gears:
                        isTouchingGear = (row - 1, col - 1)
                    if col > 0 and row < len(lines) - 1 and [row + 1, col - 1] in gears:
                        isTouchingGear = (row + 1, col - 1)
                    if col < len(line) - 1 and row > 0 and [row - 1, col + 1] in gears:
                        isTouchingGear = (row - 1, col + 1)
                    if col < len(line) - 1 and row < len(lines) - 1 and [row + 1, col + 1] in gears:
                        isTouchingGear = (row + 1, col + 1)
            else:
                if isTouchingGear is not None:
                    if isTouchingGear not in touchingGears:
                        touchingGears[isTouchingGear] = []
                    touchingGears[isTouchingGear].append(part)
                    isTouchingGear = None
                part = None
        if isTouchingGear is not None:
            if isTouchingGear not in touchingGears:
                touchingGears[isTouchingGear] = []
            touchingGears[isTouchingGear].append(part)
            isTouchingGear = None
        part = None
    total = 0
    gears = None
    for gears in touchingGears.values():
        gearTotal = 1
        for gear in gears:
            gearTotal *= int(''.join(gear))
        total += gearTotal
    print(total)


path = getpath(__file__)
with open('{}/day3.txt'.format(path), 'r') as f:

    lines = f.readlines()

    lines = aslist(lines)

    part1(lines) # 525119
    part2(lines) # 76504829