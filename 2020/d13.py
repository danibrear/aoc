from itertools import count
from operator import mul


def get_buses(inp):
    buses = []
    for x in inp.split(','):
        if x == 'x':
            continue
        buses.append(int(x))

    return buses


def part1(id, buses):

    print(id, buses)
    buses = get_buses(buses)

    start = id
    done = False
    while not done:
        for bus in buses:
            if start % bus == 0:
                print((start - id) * bus)
                done = True
                break
        start += 1
    pass


def part2(inp):
    buses = sorted([(int(bus), idx) for idx, bus in enumerate(
        inp.split(',')) if bus != 'x'], reverse=True)
    t, step = 0, 1
    for bus, offs in buses:
        for c in count(t, step):
            if (c + offs) % bus == 0:
                t, step = c, step * bus
                break

    print(t)


with open('./d13.txt', 'r') as f:

    rows = f.readlines()

    id = int(rows[0].replace('\n', ''))
    buses = rows[1].replace('\n', '')

    part1(id, buses)
    part2(buses)
