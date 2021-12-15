import re
from collections import *

from datetime import datetime

INCLUDE_H = False


def h(_h, _i, _j):
    if _i < len(_h) and _j < len(_h[_i]):
        return _h[_i][_j]
    return 0


def findmoves(i, j, m, sth, _h=[]):
    i_s = [i + x for x in range(-1, 2)]
    j_s = [j + x for x in range(-1, 2)]
    pos = [(_i, _j) for _i in i_s for _j in j_s]
    pos = list(filter(lambda p: p[0] >= 0 and p[1] >= 0 and p[0] < len(
        m) and p[1] < len(m[0]), pos))
    pos = list(filter(lambda p: p != (i, j), pos))
    pos = list(filter(lambda p: p[0] == i or p[1] == j, pos))
    poss = [(p, m[p[0]][p[1]] + sth + h(_h, i, j), (i, j)) for p in pos]
    poss = sorted(poss, key=lambda x: x[1])
    return poss


def sortmoves(nm, em):
    ms = sorted(nm + em, key=lambda x: x[1])
    return ms


def findp(ma, i, j, _h=[]):
    seen = set()
    seen.add((i, j))
    path = {}
    scores = findmoves(i, j, ma, 0, _h)
    scoreToHere = {(i, j): 0}
    while True:
        if (i, j) == (len(ma) - 1, len(ma[0]) - 1):
            break
        n = sortmoves(scores, findmoves(i, j, ma, scoreToHere[(i, j)], _h))
        n = list(filter(lambda x: x[0] not in seen, n))
        scores = n
        nm = n[0]

        seen.add(nm[0])
        scoreToHere[nm[0]] = scoreToHere[nm[2]] + ma[nm[0][0]][nm[0][1]]
        path[nm[0]] = nm[2]

        i, j = nm[0]

    sp = [(i, j)]
    while True:
        if (i, j) == (0, 0):
            break
        sp.append(path[(i, j)])
        i, j = path[(i, j)]

    return sum([ma[s[0]][s[1]] for s in sp]) - ma[0][0]


def part1(lines):
    ma = [[int(l) for l in line] for line in lines]

    print(findp(ma, 0, 0))


def incmap(m):
    mult = 5
    nm = [[0 for x in range(len(m[0]) * mult)] for y in range(len(m) * mult)]
    for r in range(len(m) * mult):
        xr = r // len(m)
        for c in range(len(m[0]) * mult):
            mr = r % len(m)
            mc = c % len(m[0])
            xc = c // len(m[0])

            # print('xr = {}, xc = {}, r = {}, c = {}'.format(xr, xc, r, c))

            nm[r][c] = (m[mr][mc] + xr + xc)
            if nm[r][c] >= 10:
                nm[r][c] -= 9
    return nm


def part2(lines):
    ma = [[int(l) for l in line] for line in lines]

    nm = incmap(ma)
    h = [[x+y for x in range(len(nm[0]))] for y in range(len(nm))]

    # for n in nm:
    #     print(''.join([str(x) for x in n]))

    if INCLUDE_H:
        print(findp(nm, 0, 0, h))
    else:
        print(findp(nm, 0, 0))


with open('./d15.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))

    start = datetime.now()
    print('Part 1: [562]')
    part1(lines)
    print('Part 1 took: {}'.format(datetime.now() - start))
    p2start = datetime.now()
    if INCLUDE_H:
        print('Part 2 with H: [2874]')
    else:
        print('Part 2 with No H: [2874]')
    part2(lines)
    print('Part 2 took: {}'.format(datetime.now() - p2start))
    print('Total: [{}]'.format(datetime.now() - start))
