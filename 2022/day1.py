def part1(lines):
    maxsofar = 0
    total = 0
    for line in lines:
        if line == '\n':
            maxsofar = max(maxsofar, total)
            total = 0
        else:
            total += int(line)
    maxsofar = max(maxsofar, total)
    print(maxsofar)
    return maxsofar


def part2(lines):
    total = 0
    maxes = []
    for line in lines:
        if line == '\n':
            maxes.append(total)
            total = 0
        else:
            total += int(line)

    maxes.append(total)
    maxes = sorted(maxes, reverse=True)
    maxes = maxes[0:3]
    print(sum(maxes))
    return maxsofar


with open('./day1.txt', 'r') as f:

    lines = f.readlines()

    part1(lines)
    part2(lines)
