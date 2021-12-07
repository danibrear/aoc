def part1(lines):
    incs = 0
    last = float('inf')
    for line in lines:
        this = int(line)
        if this > last:
            incs += 1
        last = this
    print(incs)

    # print(sum([x < y for x, y in zip(lines[:-1], lines[1:])]))


def part2(lines):
    start = 0
    last = float('inf')
    incs = 0
    while start < len(lines):
        total = sum(map(int, lines[start:start+3]))
        if (total > last):
            incs += 1
        start += 1
        last = total

    print(incs)


with open('./d1.txt', 'r') as f:

    lines = f.readlines()

    part1(lines)
    part2(lines)
