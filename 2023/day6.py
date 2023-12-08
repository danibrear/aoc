from utils import aslist, splitlines, ingroups, getday, getpath
import re
import math


def part1(lines):
    times = map(
        lambda x: int(x), re.sub(r"\s+", " ", lines[0].split(":")[1].strip()).split(" ")
    )
    distances = map(
        lambda x: int(x), re.sub(r"\s+", " ", lines[1].split(":")[1].strip()).split(" ")
    )

    total = 1

    for [time, distance] in zip(times, distances):
        half = math.floor(time / 2)
        diff = half * (time - half) - distance
        dist = math.floor(math.sqrt(diff))
        if (half - dist) * (time - (half - dist)) > distance:
            dist += 1
        cnt = 2 * dist

        if time % 2 == 0:
            if (time / 2) ** 2 > distance:
                cnt -= 1
        total *= cnt

    print(total)

    return total


def part2(lines):
    time = re.sub(r"\s+", "", lines[0].split(":")[1].strip())
    distance = re.sub(r"\s+", "", lines[1].split(":")[1].strip())

    time = int(time)
    distance = int(distance)
    half = math.floor(time / 2)

    diff = half * (time - half) - distance

    dist = math.floor(math.sqrt(diff))
    if (half - dist) * (time - (half - dist)) > distance:
        dist += 1
    cnt = 2 * dist

    if time % 2 == 0:
        if (time / 2) ** 2 > distance:
            cnt -= 1

    print(cnt)
    return cnt


path = getpath(__file__)
with open("{}/day6.txt".format(path), "r") as f:
    lines = f.readlines()

    lines = aslist(lines)

    p1Val = part1(lines)  # 160816
    p2Val = part2(lines)  # 46561107

    assert p1Val == 160816
    assert p2Val == 46561107
