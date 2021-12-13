import re


def fold(dir, loc, points):
    newpoints = set()

    for (x, y) in points:
        if dir == 'x':
            if x > loc:
                newpoints.add(((2 * loc) - x, y))
            else:
                newpoints.add((x, y))
        elif dir == 'y':
            if y > loc:
                newpoints.add((x, (2 * loc) - y))
            else:
                newpoints.add((x, y))
    return newpoints


def part1(lines):
    points = []
    folds = []
    maxX = 0
    maxY = 0
    for line in lines:
        if len(line) > 0:
            x, y = line.split(',')
            maxX = max(maxX, int(x))
            maxY = max(maxY, int(y))
            points.append((int(x), int(y)))
        else:
            break

    for line in lines:
        if len(line) > 0 and line[0] == 'f':
            l = line.split('fold along ')[1]
            dir, loc = l.split('=')
            folds.append((dir, int(loc)))

    print(len(fold(folds[0][0], folds[0][1], points)))


def part2(lines):
    points = []
    folds = []
    maxX = 0
    maxY = 0
    for line in lines:
        if len(line) > 0:
            x, y = line.split(',')
            maxX = max(maxX, int(x))
            maxY = max(maxY, int(y))
            points.append((int(x), int(y)))
        else:
            break

    for line in lines:
        if len(line) > 0 and line[0] == 'f':
            l = line.split('fold along ')[1]
            dir, loc = l.split('=')
            folds.append((dir, int(loc)))

    for f in folds:
        points = fold(f[0], f[1], points)

    cols = max(points, key=lambda x: x[0])[0]
    rows = max(points, key=lambda x: x[1])[1]

    grid = [[' ' for _ in range(cols + 1)] for _ in range(rows + 1)]
    for (x, y) in points:
        grid[y][x] = '#'

    for row in grid:
        print(''.join(row))


with open('./d13.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    print('Part 1: [602]')
    part1(lines)
    print('Part 2: [CAFJHZCK]')
    part2(lines)
