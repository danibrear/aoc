def part1(line):
    floor = 0
    for c in line:
        if c == '(':
            floor += 1
        if c == ')':
            floor -= 1
    print(floor)


def part2(line):
    floor = 0
    for i, c in enumerate(line):
        if c == '(':
            floor += 1
        if c == ')':
            floor -= 1
        if floor < 0:
            print(i + 1)
            break


with open('./d1.txt', 'r') as file:

    line = file.readline()

    part1(line)
    part2(line)
