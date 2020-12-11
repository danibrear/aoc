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
    total = 0
    for line in lines:
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        needed = 0

        if max([l, w, h]) == h:
            needed += (2 * l + 2 * w)
        elif max([l, w, h]) == w:
            needed += (2 * l + 2 * h)
        elif max([l, w, h]) == l:
            needed += (2*w + 2*h)

        needed += (l*w*h)

        total += needed
    print(total)


with open('./d2.txt', 'r') as file:

    lines = file.readlines()

    lines = list(map(lambda x: x.replace('\n', ''), lines))

    part1(lines)
    part2(lines)
