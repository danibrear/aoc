def part1(lines):
    startH = 0
    startY = 0
    for line in lines:
        parts = line.split(' ')

        if parts[0] == 'forward':
            startH += int(parts[1])
        elif parts[0] == 'down':
            startY += int(parts[1])
        elif parts[0] == 'up':
            startY -= int(parts[1])

    print(startH * startY)


def part2(lines):
    startH = 0
    startY = 0
    aim = 0
    for line in lines:
        parts = line.split(' ')

        if parts[0] == 'forward':
            startH += int(parts[1])
            startY += int(parts[1]) * int(aim)
        elif parts[0] == 'down':
            aim += int(parts[1])
        elif parts[0] == 'up':
            aim -= int(parts[1])

    print(startH * startY)


with open('./d2.txt', 'r') as f:

    lines = f.readlines()

    part1(lines)
    part2(lines)
