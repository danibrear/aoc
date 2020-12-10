def part1(lines):

    total = 0
    for line in lines:
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        needed = (2*l*w) + (2*w*h) + (2*h*l)

        if max([l, w, h]) == h:
            needed += (l * w)
        elif max([l, w, h]) == w:
            needed += (l * h)
        elif max([l, w, h]) == l:
            needed += (w * h)

        total += needed
    print(total)


def part2(lines):
    pass


with open('./d2.txt', 'r') as file:

    lines = file.readlines()

    lines = map(lambda x: x.replace('\n', ''), lines)

    part1(lines)
    part2(lines)
