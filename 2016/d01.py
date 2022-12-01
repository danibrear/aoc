
def part1(lines):
    dirs = lines[0].split(', ')

    x = y = 0
    facing = 'n'
    visits = {}
    for dir in dirs:
        if dir[0] == 'R':
            facing = {
                'n': 'e',
                'e': 's',
                's': 'w',
                'w': 'n'
            }[facing]
        else:
            facing = {
                'n': 'w',
                'w': 's',
                's': 'e',
                'e': 'n'
            }[facing]

        if facing == 'n':
            y += int(dir[1:])
        elif facing == 's':
            y -= int(dir[1:])
        elif facing == 'e':
            x += int(dir[1:])
        elif facing == 'w':
            x -= int(dir[1:])
    print('Part 1: {}'.format(abs(x) + abs(y)))


def part2(lines):
    dirs = lines[0].split(', ')

    x = y = 0
    facing = 'n'
    visits = {}
    for dir in dirs:
        if dir[0] == 'R':
            facing = {
                'n': 'e',
                'e': 's',
                's': 'w',
                'w': 'n'
            }[facing]
        else:
            facing = {
                'n': 'w',
                'w': 's',
                's': 'e',
                'e': 'n'
            }[facing]

        ny = 0
        nx = 0
        dx = 1
        dy = 1
        if facing == 'n':
            ny = int(dir[1:])
        elif facing == 's':
            ny = -int(dir[1:])
            dy = -1
        elif facing == 'e':
            nx = int(dir[1:])
        elif facing == 'w':
            nx = -int(dir[1:])
            dx = -1
        for i in range(x, x + nx, dx):
            if (i, y) not in visits:
                visits[(i, y)] = 1
            else:
                print('Part 2: {}'.format(abs(i) + abs(y)))
                return
        for j in range(y, y + ny, dy):
            if (x, j) not in visits:
                visits[(x, j)] = 1
            else:
                print('Part 2: {}'.format(abs(x) + abs(j)))
                return
        x += nx
        y += ny
    print(x, y)


with open('./d01.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    part1(lines)
    part2(lines)
