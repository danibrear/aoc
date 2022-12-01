import re
from itertools import permutations


def generate_points(b1, b2):
    points = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            b_1 = [x * b for b in b1]
            b_2 = [y * b for b in b2]
            c = [list(zip(each_permutation, b_2))
                 for each_permutation in permutations(b_1, len(b_2))]

            c = [(sum(_c_) for _c_ in _c) for _c in c]
            points.extend(c)
    return points


def part1(lines):
    scanners = {}
    currsh = ''
    for line in lines:
        scannerhead = re.match(r'--- scanner (\d+) ---', line)
        if scannerhead:
            currsh = scannerhead.group(1)
            scanners[currsh] = []
        elif len(line) > 0:
            scanners[currsh].append(tuple(map(int, line.split(','))))

    scanner0 = scanners['0']

    beacons = {}
    for i in scanner0:
        beacons[i] = 1

    # print(beacons)
    # print('--' * 20)

    scanner1 = scanners['1']
    for i in scanner1:
        for j in scanner0:
            points = generate_points(i, j)
            for point in points:
                point = tuple(point)
                if point in beacons:
                    beacons[point] += 1
                else:
                    beacons[point] = 1

    # print(beacons)
    for k, v in beacons.items():
        if v > 1:
            print(k)


def part2(lines):
    for line in lines:
        pass


with open('./d19-test-2.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    part1(lines)
    part2(lines)
