
def part1(lines):
    points = []
    maxX = 0
    maxY = 0
    for line in lines:
        sects = line.split(' -> ')

        [x1, y1] = list(map(int, sects[0].split(',')))
        [x2, y2] = list(map(int, sects[1].split(',')))

        maxX = max(maxX, x1, x2)
        maxY = max(maxY, y1, y2)

        points.append([x1, y1, x2, y2])

    grid = [[0 for _ in range(maxX+1)] for _ in range(maxY+1)]

    for point in points:
        [x1, y1, x2, y2] = point

        if x1 == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            for y in range(start, end+1):
                grid[y][x1] += 1
        elif y1 == y2:
            start = min(x1, x2)
            end = max(x1, x2)
            for x in range(start, end+1):
                grid[y1][x] += 1

    count = 0
    for row in grid:
        for val in row:
            if val > 1:
                count += 1
    print(count)

    return count


def part2(lines):
    points = []
    maxX = 0
    maxY = 0
    for line in lines:
        sects = line.split(' -> ')

        [x1, y1] = list(map(int, sects[0].split(',')))
        [x2, y2] = list(map(int, sects[1].split(',')))

        maxX = max(maxX, x1, x2)
        maxY = max(maxY, y1, y2)

        points.append([x1, y1, x2, y2])

    grid = [[0 for _ in range(maxX+1)] for _ in range(maxY+1)]

    for point in points:
        [x1, y1, x2, y2] = point

        if x1 == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            for y in range(start, end+1):
                grid[y][x1] += 1
        elif y1 == y2:
            start = min(x1, x2)
            end = max(x1, x2)
            for x in range(start, end+1):
                grid[y1][x] += 1
        else:
            xdir = 1 if x2 > x1 else -1
            ydir = 1 if y2 > y1 else -1
            while x1 != x2 and y1 != y2:
                grid[y1][x1] += 1
                x1 += xdir
                y1 += ydir
            grid[y1][x1] += 1

    count = 0
    for row in grid:
        for val in row:
            if val > 1:
                count += 1

    # for row in grid:
    #     print(' '.join([str(x) if x > 0 else '.' for x in row]))

    print(count)
    return count


with open('./d05.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    print('Part 1 should be 6005:')
    part1(lines)
    print('Part 2 should be 23864:')
    part2(lines)
