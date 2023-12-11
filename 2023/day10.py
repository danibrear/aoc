from utils import aslist, splitlines, ingroups, getday, getpath

VALID_PIPES = {
    "|": {"up": ["F", "|", "7"], "down": ["L", "|", "J"], "left": [], "right": []},
    "-": {"up": [], "down": [], "left": ["F", "-", "L"], "right": ["J", "-", "7"]},
    "F": {"up": [], "down": ["|", "L", "J"], "left": [], "right": ["-", "J", "7"]},
    "L": {"up": ["F", "|", "7"], "down": [], "left": [], "right": ["7", "-", "J"]},
    "J": {"up": ["F", "|", "7"], "down": [], "left": ["F", "-", "L"], "right": []},
    "7": {"up": [], "down": ["L", "|", "J"], "left": ["F", "-", "L"], "right": []},
}


def isS(val):
    return val == "S"


def isValid(lines, row, col):
    val = lines[row][col]
    if val not in VALID_PIPES:
        return False
    validpipes = VALID_PIPES[val]

    connections = 0
    if row > 0:
        if lines[row - 1][col] in validpipes["up"] or isS(lines[row - 1][col]):
            connections += 1
    if row < len(lines) - 1:
        if lines[row + 1][col] in validpipes["down"] or isS(lines[row + 1][col]):
            connections += 1
    if col > 0:
        if lines[row][col - 1] in validpipes["left"] or isS(lines[row][col - 1]):
            connections += 1
    if col < len(lines[row]) - 1:
        if lines[row][col + 1] in validpipes["right"] or isS(lines[row][col + 1]):
            connections += 1
    return connections == 2


def step(lines, row, col, dir):
    if lines[row][col] == "S":
        if dir == "up":
            if lines[row - 1][col] == "F":
                return [row - 1, col, "up"]
            elif lines[row - 1][col] == "|":
                return [row - 1, col, "up"]
            elif lines[row - 1][col] == "7":
                return [row - 1, col, "up"]
        elif dir == "down":
            if lines[row + 1][col] == "L":
                return [row + 1, col, "down"]
            elif lines[row + 1][col] == "|":
                return [row + 1, col, "down"]
            elif lines[row + 1][col] == "J":
                return [row + 1, col, "down"]
        elif dir == "left":
            if lines[row][col - 1] == "F":
                return [row, col - 1, "left"]
            elif lines[row][col - 1] == "-":
                return [row, col - 1, "left"]
            elif lines[row][col - 1] == "L":
                return [row, col - 1, "left"]
        elif dir == "right":
            if lines[row][col + 1] == "7":
                return [row, col + 1, "right"]
            elif lines[row][col + 1] == "-":
                return [row, col + 1, "right"]
            elif lines[row][col + 1] == "J":
                return [row, col + 1, "right"]
    elif lines[row][col] == "-":
        if dir == "left":
            return [row, col - 1, dir]
        elif dir == "right":
            return [row, col + 1, dir]
    elif lines[row][col] == "|":
        if dir == "up":
            return [row - 1, col, dir]
        elif dir == "down":
            return [row + 1, col, dir]
    elif lines[row][col] == "F":
        if dir == "up":
            return [row, col + 1, "right"]
        elif dir == "left":
            return [row + 1, col, "down"]
    elif lines[row][col] == "L":
        if dir == "down":
            return [row, col + 1, "right"]
        elif dir == "left":
            return [row - 1, col, "up"]
    elif lines[row][col] == "J":
        if dir == "down":
            return [row, col - 1, "left"]
        elif dir == "right":
            return [row - 1, col, "up"]
    elif lines[row][col] == "7":
        if dir == "up":
            return [row, col - 1, "left"]
        elif dir == "right":
            return [row + 1, col, "down"]
    return None


def areEqual(a, b):
    if a is None or b is None:
        return False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                return False
    return True


def part1(lines):
    cleanedRows = []
    rows = []
    for line in lines:
        rows.append(list(line))
    lines = rows
    sRow = None
    sCol = None
    lastCleaned = rows

    cleaned = True
    steps = 0

    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == "S":
                sRow = row
                sCol = col
                break
        if sRow is not None:
            break
    while not cleaned:
        steps += 1
        print("step", steps)
        cleanedRows = []
        for row, line in enumerate(lastCleaned):
            cleanedRow = []
            for col, val in enumerate(line):
                if val not in VALID_PIPES and not isS(val):
                    cleanedRow.append(".")
                    continue
                if val == "S":
                    cleanedRow.append("S")
                    sRow = row
                    sCol = col
                elif isValid(lastCleaned, row, col):
                    cleanedRow.append(val)
                else:
                    cleanedRow.append(".")
            cleanedRows.append(cleanedRow)
        if not areEqual(cleanedRows, lastCleaned):
            lastCleaned = cleanedRows
            cleaned = False
        else:
            cleaned = True
            break

    s1At = [sRow, sCol]
    s2At = [sRow, sCol]

    cleanedRows = rows

    connectionsToS = []
    if sRow > 0:
        up = lines[sRow - 1][sCol]
        if up in VALID_PIPES and VALID_PIPES[up]["down"] != []:
            connectionsToS.append(step(cleanedRows, sRow, sCol, "up"))
    if sRow < len(lines) - 1:
        down = lines[sRow + 1][sCol]
        if down in VALID_PIPES and VALID_PIPES[down]["up"] != []:
            connectionsToS.append(step(cleanedRows, sRow, sCol, "down"))
    if sCol > 0:
        left = lines[sRow][sCol - 1]
        if left in VALID_PIPES and VALID_PIPES[left]["right"] != []:
            connectionsToS.append(step(cleanedRows, sRow, sCol, "left"))
    if sCol < len(lines[sRow]) - 1:
        right = lines[sRow][sCol + 1]
        if right in VALID_PIPES and VALID_PIPES[right]["left"] != []:
            connectionsToS.append(step(cleanedRows, sRow, sCol, "right"))

    s1At = connectionsToS[0]
    s2At = connectionsToS[1]

    steps = 0
    while True:
        if s1At[0] == s2At[0] and s1At[1] == s2At[1]:
            steps += 1
            break
        print(
            "before",
            s1At,
            cleanedRows[s1At[0]][s1At[1]],
            s2At,
            cleanedRows[s2At[0]][s2At[1]],
        )
        s1At = step(cleanedRows, s1At[0], s1At[1], s1At[2])
        s2At = step(cleanedRows, s2At[0], s2At[1], s2At[2])
        if s1At is None or s2At is None:
            print("failed with ", s1At, "s2", s2At)
            return
        # print(
        #     "after",
        #     s1At,
        #     cleanedRows[s1At[0]][s1At[1]],
        #     s2At,
        #     cleanedRows[s2At[0]][s2At[1]],
        # )

        steps += 1

    print(steps)


def part2(lines):
    cleanedRows = []
    rows = []
    for line in lines:
        rows.append(list(line))
    lines = rows
    sRow = None
    sCol = None
    lastCleaned = rows

    cleaned = True
    steps = 0

    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == "S":
                sRow = row
                sCol = col
                break
        if sRow is not None:
            break
    while not cleaned:
        steps += 1
        print("step", steps)
        cleanedRows = []
        for row, line in enumerate(lastCleaned):
            cleanedRow = []
            for col, val in enumerate(line):
                if val not in VALID_PIPES and not isS(val):
                    cleanedRow.append(".")
                    continue
                if val == "S":
                    cleanedRow.append("S")
                    sRow = row
                    sCol = col
                elif isValid(lastCleaned, row, col):
                    cleanedRow.append(val)
                else:
                    cleanedRow.append(".")
            cleanedRows.append(cleanedRow)
        if not areEqual(cleanedRows, lastCleaned):
            lastCleaned = cleanedRows
            cleaned = False
        else:
            cleaned = True
            break

    s1At = [sRow, sCol]
    s2At = [sRow, sCol]

    cleanedRows = rows

    connectionsToS = []
    if sRow > 0:
        up = lines[sRow - 1][sCol]
        if up in VALID_PIPES and VALID_PIPES[up]["down"] != []:
            connectionsToS.append(step(cleanedRows, sRow, sCol, "up"))
    if sRow < len(lines) - 1:
        down = lines[sRow + 1][sCol]
        if down in VALID_PIPES and VALID_PIPES[down]["up"] != []:
            connectionsToS.append(step(cleanedRows, sRow, sCol, "down"))
    if sCol > 0:
        left = lines[sRow][sCol - 1]
        if left in VALID_PIPES and VALID_PIPES[left]["right"] != []:
            connectionsToS.append(step(cleanedRows, sRow, sCol, "left"))
    if sCol < len(lines[sRow]) - 1:
        right = lines[sRow][sCol + 1]
        if right in VALID_PIPES and VALID_PIPES[right]["left"] != []:
            connectionsToS.append(step(cleanedRows, sRow, sCol, "right"))

    s1At = connectionsToS[0]
    s2At = connectionsToS[1]

    steps = 0

    pointsOnLoop = set()
    pointsOnLoop.add((s1At[0], s1At[1]))
    pointsOnLoop.add((s2At[0], s2At[1]))
    pointsOnLoop.add((sRow, sCol))
    while True:
        if s1At[0] == s2At[0] and s1At[1] == s2At[1]:
            steps += 1
            break
        s1At = step(cleanedRows, s1At[0], s1At[1], s1At[2])
        s2At = step(cleanedRows, s2At[0], s2At[1], s2At[2])
        if s1At is None or s2At is None:
            print("failed with ", s1At, "s2", s2At)
            return

        pointsOnLoop.add((s1At[0], s1At[1]))
        pointsOnLoop.add((s2At[0], s2At[1]))

        steps += 1

    cleanedRows = []
    for row, line in enumerate(lines):
        cleanedRow = []
        for col, val in enumerate(line):
            if (row, col) not in pointsOnLoop:
                cleanedRow.append(".")
                continue
            cleanedRow.append(val)
        cleanedRows.append(cleanedRow)

    outputMat = []
    for line in cleanedRows:
        outmatrow = []
        on = False
        at = None
        for val in line:
            if val in VALID_PIPES or isS(val):
                if val == "|":
                    on = not on

                if val in ["F", "L"]:
                    at = val

                if val == "7":
                    if at == "L":
                        on = not on
                        at = None

                if val == "J":
                    if at == "F":
                        on = not on
                        at = None

                outmatrow.append(val)
            if val == ".":
                if on:
                    outmatrow.append("I")
                else:
                    outmatrow.append("O")

        outputMat.append(outmatrow)
    for row, line in enumerate(outputMat):
        for col, val in enumerate(line):
            if row > 0:
                if outputMat[row - 1][col] == "O" and val == "I":
                    outputMat[row][col] = "O"
            if row < len(outputMat) - 1:
                if outputMat[row + 1][col] == "O" and val == "I":
                    outputMat[row][col] = "O"
            if col > 0:
                if outputMat[row][col - 1] == "O" and val == "I":
                    outputMat[row][col] = "O"
            if col < len(outputMat[row]) - 1:
                if outputMat[row][col + 1] == "O" and val == "I":
                    outputMat[row][col] = "O"

    included = 0
    for line in outputMat:
        for val in line:
            if val == "I":
                included += 1

    print(included)


path = getpath(__file__)
with open("{}/day10.txt".format(path), "r") as f:
    lines = f.readlines()

    lines = aslist(lines)

    part1(lines)  # 7145
    part2(lines)  # 445
