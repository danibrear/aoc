def part1(rows):
    pass


def part2(rows):
    pass


with open('./d11.txt', 'r') as f:

    rows = f.readlines()

    rows = list(rows)
    rows = map(lambda x: x.replace('\n', ''), rows)

    part1(rows)
    part2(rows)
