from datetime import datetime


def part1(lines):
    c = 0
    for line in lines:
        op = line.split(' | ')[1]
        c += sum([1 for x in op.split(' ') if len(x) in [2, 3, 4, 7]])

    print(c)


def diff(li1, li2):
    return [i for i in li1 + li2 if i not in li1 or i not in li2]


def uni(li1, li2):
    return sorted(list(set(li1).union(set(li2))))


def find9(o, tc, sp):
    for s in sp:
        l = sorted([x for x in s])
        if (len(diff(o, l))) == 1 and tc in l:
            return l
    return None


def find6(e, o, sp):

    for s in sp:
        l = sorted([x for x in s])
        d = diff(l, e)
        d2 = diff(d, o)
        if len(d2) == 1:
            return l
    return None


def find0(e, mc, sp):
    for s in sp:
        l = sorted([x for x in s])
        d = diff(l, e)
        if len(d) == 1 and d[0] == mc:
            return l
    return None


def find3(o, tc, bc, sp):
    for s in sp:
        l = sorted([x for x in s])
        no = o + [tc, bc]
        if (len(diff(no, l))) == 1 and tc in l and bc in l:
            return l
    return None


def part2(lines):
    total = 0
    for line in lines:
        [s, op] = line.split(' | ')
        sp = s.split(' ')
        # print(line)
        one = sorted([i for i in [x for x in sp if len(x) == 2][0]])
        seven = sorted([i for i in [x for x in sp if len(x) == 3][0]])
        four = sorted([i for i in [x for x in sp if len(x) == 4][0]])
        eight = sorted([i for i in [x for x in sp if len(x) == 7][0]])

        topCenter = diff(one, seven)[0]
        nine = find9(uni(four, seven), topCenter, sp)
        bottomCenter = diff(uni(four, seven), nine)[0]
        bottomLeft = diff(nine, eight)[0]

        three = find3(one, topCenter, bottomCenter, sp)
        middleCenter = [i for i in three if i not in uni(
            one, [topCenter, bottomCenter])][0]
        zero = find0(eight, middleCenter, sp)
        six = find6(eight, one, sp)
        topRight = [i for i in one if i not in six][0]
        bottomRight = [i for i in one if i != topRight][0]

        two = sorted([topCenter, topRight, middleCenter,
                     bottomCenter, bottomLeft])
        topLeft = diff(eight, uni(two, one))[0]
        five = sorted([topCenter, topLeft, middleCenter,
                      bottomRight, bottomCenter])

        out = []
        for o in op.split(' '):
            o = sorted([i for i in o])
            if o == zero:
                out.append('0')
            if o == one:
                out.append('1')
            elif o == two:
                out.append('2')
            elif o == three:
                out.append('3')
            elif o == four:
                out.append('4')
            elif o == five:
                out.append('5')
            elif o == six:
                out.append('6')
            elif o == seven:
                out.append('7')
            elif o == eight:
                out.append('8')
            elif o == nine:
                out.append('9')

        total += int(''.join(out))

    print(total)


with open('./d08.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    start = datetime.now()
    part1(lines)
    part2(lines)
    print('\n\nTotal time: {}'.format(datetime.now() - start))
