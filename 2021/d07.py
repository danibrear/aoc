from datetime import datetime


def part1(lines):
    ps = list(map(int, lines[0].split(',')))
    ps = sorted(ps)

    m = len(ps)//2
    medians = ps[m-10:m+10]

    sm = float('inf')
    for me in medians:
        fuel = 0
        for x in ps:
            fuel += abs(x - me)
        if fuel < sm:
            sm = fuel
    print(sm)


def calc(n):
    return (n * (n+1))//2


def part2(lines):
    smallest = float('inf')

    ps = list(map(int, lines[0].split(',')))
    ps = sorted(ps)
    m = len(ps)//2
    medians = ps[m-200:m+200]

    for me in medians:
        fuel = 0
        for x in ps:
            fuel += calc(abs(x - me))
        if fuel < smallest:
            smallest = fuel

    print(smallest)


with open('./d07.txt', 'r') as f:

    from datetime import datetime

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    start = datetime.now()
    print('Part 1: 335271:')
    part1(lines)
    print('Part 2: 95851339:')
    part2(lines)
    print('Time: {} seconds'.format((datetime.now() - start).total_seconds()))
