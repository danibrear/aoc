from utils import aslist, splitlines, ingroups


def part1(grid):
    visiblecoords = set()

    total = (len(grid) - 1) * 4
    # left
    for r in range(1, len(grid)-1):
        maxsofar = grid[r][0]
        for c in range(1, len(grid[r])-1):
            if grid[r][c] > maxsofar:
                visiblecoords.add((r, c))
                maxsofar = grid[r][c]
    # right
    for r in range(1, len(grid)-1):
        maxsofar = grid[r][-1]
        for c in range(len(grid[r])-1, 0, -1):
            if grid[r][c] > maxsofar:
                visiblecoords.add((r, c))
                maxsofar = grid[r][c]

    # top
    for c in range(1, len(grid[0])-1):
        maxsofar = grid[0][c]
        for r in range(1, len(grid)-1):
            if grid[r][c] > maxsofar:
                visiblecoords.add((r, c))
                maxsofar = grid[r][c]

    # bottom
    for c in range(1, len(grid[0])-1):
        maxsofar = grid[-1][c]
        for r in range(len(grid)-1, 1, -1):
            if grid[r][c] > maxsofar:
                visiblecoords.add((r, c))
                maxsofar = grid[r][c]

    # print(visiblecoords)
    print(total + len(visiblecoords))


def part2(grid):

    def calat(grid, r, c):
        show = r == 3 and c == 2
        treedirs = []
        # up
        trees = 0
        maxsofar = grid[r][c]
        _r = r - 1
        while _r >= 0 and grid[_r][c] <= maxsofar:
            if grid[_r][c] < maxsofar:
                trees += 1
            else:
                trees += 1
                break
            _r -= 1
        treedirs.append(trees)
        # down
        maxsofar = grid[r][c]
        trees = 0
        _r = r + 1
        while _r < len(grid):
            if grid[_r][c] < maxsofar:
                trees += 1
            else:
                trees += 1
                break
            _r += 1
        treedirs.append(trees)
        # left
        maxsofar = grid[r][c]
        trees = 0
        _c = c - 1

        while _c >= 0:
            if grid[r][_c] < maxsofar:
                trees += 1
            else:
                trees += 1
                break
            _c -= 1
        treedirs.append(trees)
        # right
        maxsofar = grid[r][c]
        trees = 0
        _c = c + 1
        while _c < len(grid[r]):
            if grid[r][_c] < maxsofar:
                trees += 1
            else:
                trees += 1
                break
            _c += 1

        treedirs.append(trees)

        v = 1
        for t in treedirs:
            v *= t
        return v

    maxtrees = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            ts = calat(grid, r, c)
            if ts > maxtrees:
                maxtrees = ts
    print(maxtrees)


with open('day8.txt', 'r') as f:

    lines = f.readlines()

    lines = aslist(lines)

    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        grid.append(row)

    part1(grid)  # 1820
    part2(grid)  # 385112
