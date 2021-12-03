
def part1(lines):
    pos = {}
    for x in range(len(lines[0]) - 1):
        pos[x] = [0, 0]
    for line in lines:
        line = line.replace('\n', '')
        for i, x in enumerate(line):
            if x == '0':
                pos[i][0] += 1
            else:
                pos[i][1] += 1
    gamma = ''
    ep = ''
    for x in pos:
        if pos[x][0] < pos[x][1]:
            gamma += '1'
            ep += '0'
        else:
            gamma += '0'
            ep += '1'
    g = int(gamma, base=2)
    e = int(ep, base=2)

    print(g * e)


def part2(lines):
    remaining = lines

    looking_for = 0
    while looking_for < len(lines[0]) and len(remaining) > 1:
        ones = 0
        zeros = 0
        for line in remaining:
            if line[looking_for] == '1':
                ones += 1
            else:
                zeros += 1

        select = '1' if ones >= zeros else '0'
        new_remaining = []
        for line in remaining:
            if line[looking_for] == select:
                new_remaining.append(line)
        remaining = new_remaining
        looking_for += 1

    o2 = remaining[0].replace('\n', '')

    remaining = lines

    looking_for = 0
    while looking_for < len(lines[0]) and len(remaining) > 1:
        ones = 0
        zeros = 0
        for line in remaining:
            if line[looking_for] == '1':
                ones += 1
            else:
                zeros += 1

        select = '1' if ones < zeros else '0'
        new_remaining = []
        for line in remaining:
            if line[looking_for] == select:
                new_remaining.append(line)
        remaining = new_remaining
        looking_for += 1

    co2 = remaining[0]

    print(int(o2, base=2) * int(co2, base=2))


with open('./d03.txt', 'r') as f:

    lines = f.readlines()

    part1(lines)
    part2(lines)
