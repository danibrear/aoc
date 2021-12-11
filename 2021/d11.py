import copy


def flash(octi, i, j, flashed):
    i_s = [i + x for x in range(-1, 2)]
    j_s = [j + x for x in range(-1, 2)]
    pos = [(_i, _j) for _i in i_s for _j in j_s]
    pos = list(filter(lambda p: p[0] >= 0 and p[1] >= 0 and p[0] < len(
        octi) and p[1] < len(octi[0]), pos))
    pos = list(filter(lambda p: p != (i, j), pos))
    for (ni, nj) in pos:
        if (ni, nj) not in flashed:
            octi[ni][nj] += 1
            if octi[ni][nj] > 9:
                flashed.add((ni, nj))
                octi[ni][nj] = 0
                flash(octi, ni, nj, flashed)


def step(octi):
    flashed = set()
    for i in range(len(octi)):
        for j in range(len(octi[i])):
            octi[i][j] += 1
            if octi[i][j] > 9:
                flashed.add((i, j))
                octi[i][j] = 0
                flash(octi, i, j, flashed)
    for (i, j) in flashed:
        octi[i][j] = 0
    return len(flashed)


def part1(octi1):
    total = 0
    for _ in range(100):
        total += step(octi1)
    return total


def part2(octi2):
    stepno = 0
    while True:
        stepno += 1
        if step(octi2) == 100:
            break

    return stepno


def main():
    with open("d11.txt", "r") as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.replace('\n', ''), lines))
        lines = list(map(lambda x: list(map(int, x)), lines))

        l1 = copy.deepcopy(lines)
        l2 = copy.deepcopy(lines)

        print(f"Part 1 [1785]: {part1(l1)}")
        print(f"Part 2 [354]: {part2(l2)}")


main()
