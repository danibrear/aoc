def part1(outer):
    used = []
    nextlist = set(outer['shiny gold'])
    count = 0
    while len(nextlist) > 0:
        nextup = nextlist.pop()

        if nextup in used:
            continue
        used.append(nextup)
        count += 1
        if nextup in outer:
            for bag in outer[nextup]:
                nextlist.add(bag)

    print(count)


def part2(bags):

    def get_inner_bags(bag):
        if bag not in bags or len(bags[bag]) == 0:
            return 0

        inner_total = 0
        for (num, color) in bags[bag]:
            inner_total += num + (num * get_inner_bags(color))
        return inner_total

    print(get_inner_bags('shiny gold'))


with open('./d7.txt', 'r') as f:

    lines = f.readlines()

    lines = map(lambda x: x.replace('\n', ''), lines)
    lines = list(lines)

    bags = {}
    outer = {}
    for line in lines:
        color, rest = line.split(' bags contain ')

        rest = rest.replace('.', '')
        rest = rest.replace('bags', '')
        rest = rest.replace('bag', '')
        inner = []
        for bag in rest.split(', '):
            if 'no other' in bag:
                break
            else:
                num = int(bag.split(' ')[0])
                bagcolor = ' '.join(bag.split(' ')[1:]).strip()
                inner.append((num, bagcolor))
                if bagcolor in outer:
                    outer[bagcolor].append(color)
                else:
                    outer[bagcolor] = [color]
        bags[color] = inner

    part1(outer)
    part2(bags)
