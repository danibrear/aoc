import copy


def part1(lines):
    paths = {}
    for line in lines:
        [src, dest] = line.split('-')
        if src not in paths:
            paths[src] = []
        paths[src].append(dest)
        if dest not in paths:
            paths[dest] = []
        paths[dest].append(src)

    p2end = []

    def find(paths, src, end, curr):
        if src == end:
            p2end.append(curr)
            return
        for p in paths[src]:
            if p not in curr or p.isupper():
                find(paths, p, end, curr + [p])

    find(paths, 'start', 'end', ['start'])

    return len(p2end)


def part2(lines):
    paths = {}
    for line in lines:
        [src, dest] = line.split('-')
        if src not in paths:
            paths[src] = []
        paths[src].append(dest)
        if dest not in paths:
            paths[dest] = []
        paths[dest].append(src)

    p2end = []

    def find(paths, src, end, curr, cansmall):
        if src == end:
            p2end.append(curr)
            return
        for p in paths[src]:
            if p == 'start':
                continue
            if p in curr and p.islower() and curr.count(p) == 1 and cansmall:
                find(paths, p, end, curr + [p], False)
            elif p not in curr or p.isupper():
                find(paths, p, end, curr + [p], cansmall)

    find(paths, 'start', 'end', ['start'], True)

    return len(p2end)


with open('./d12.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))
    # lines = list(map(lambda x: list(map(int, x)), lines))

    print('Part 1: [4792] {}'.format(part1(copy.deepcopy(lines))))
    print('Part 2: [133360] {}'.format(part2(copy.deepcopy(lines))))
