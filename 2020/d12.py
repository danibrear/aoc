def l_turn(way_at):
    [up, left] = way_at
    return [left, -up]


def r_turn(way_at):
    [up, left] = way_at
    return [-left, up]


def part1(rows):
    north = 0
    east = 0
    facing = [0, 1]

    for row in rows:
        action = row[0]
        value = int(row[1:])

        if action == 'R':
            turns = value / 90
            for _ in range(turns):
                facing = r_turn(facing)
        elif action == 'L':
            turns = value / 90
            for _ in range(turns):
                facing = l_turn(facing)
        elif action == 'F':
            [up, left] = facing
            north += (up * value)
            east += (left * value)

        elif action == 'N':
            north += value
        elif action == 'S':
            north -= value
        elif action == 'E':
            east += value
        elif action == 'W':
            east -= value
        else:
            print('dunno', action)

    print(abs(north) + abs(east))


def part2(rows):
    north = 0
    east = 0
    way_at = [1, 10]

    for row in rows:
        action = row[0]
        value = int(row[1:])

        if action == 'R':
            turns = value / 90
            for _ in range(turns):
                way_at = r_turn(way_at)
        elif action == 'L':
            turns = value / 90
            for _ in range(turns):
                way_at = l_turn(way_at)
        elif action == 'F':
            [up, left] = way_at
            north += (up * value)
            east += (left * value)
        elif action == 'N':
            [up, left] = way_at
            way_at = [up + value, left]
        elif action == 'S':
            [up, left] = way_at
            way_at = [up - value, left]
        elif action == 'E':
            [up, left] = way_at
            way_at = [up, left + value]
        elif action == 'W':
            [up, left] = way_at
            way_at = [up, left - value]
        else:
            print('dunno', action)

    print(abs(north) + abs(east))


with open('./d12.txt', 'r') as f:

    rows = f.readlines()

    rows = list(rows)
    rows = map(lambda x: x.replace('\n', ''), rows)

    part1(rows)
    part2(rows)
