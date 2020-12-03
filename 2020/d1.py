def part1(values):
    for val in values:
        if (2020 - val) in values:
            print(2020 - val, val)
            print((2020 - val) * val)


def part2(values):

    for i in range(len(values) - 2):
        for j in range(i, len(values) - 1):
            for k in range(j, len(values)):

                if values[i] + values[j] + values[k] == 2020:
                    print(values[i], values[j], values[k])
                    print(values[i] * values[j] * values[k])
                    return


with open('./d1-1.txt', 'r') as f:

    lines = f.readlines()
    lines = map(lambda x: x.split('\n')[0], lines)
    values = map(lambda x: int(x), lines)
    values = sorted(values)

    part1(values)
    part2(values)
