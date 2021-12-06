from queue import Queue


def part1(lines):
    fishes = list(map(int, lines[0].split(',')))
    day = 0

    while day < 80:
        newfishes = []
        for i in range(len(fishes)):
            fish = fishes[i]
            if fish == 0:
                fishes[i] = 6
                newfishes.append(8)
            else:
                fishes[i] -= 1
        fishes.extend(newfishes)
        day += 1

    print(len(fishes))


def part2(lines):
    fishes = list(map(int, lines[0].split(',')))

    fishonday = {}
    for fish in fishes:
        if fish not in fishonday:
            fishonday[fish] = 1
        else:
            fishonday[fish] += 1

    for x in range(9):
        if x not in fishonday:
            fishonday[x] = 0

    day = 0

    while day < 256:

        toadd = fishonday[0]
        for x in range(1, 9):
            fishonday[x-1] = fishonday[x]
        fishonday[8] = toadd
        fishonday[6] += toadd

        day += 1
    print(sum(fishonday.values()))


with open('./d06.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    print('Part 1: 365862')
    part1(lines)
    print('Part 2: 1653250886439')
    part2(lines)
