from math import prod

htob = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def btod(binary):

    binary = int(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def vort(line):
    return btod(line[:3])


def headers(bl):
    at = 0
    ver = vort(bl)
    at += 3
    typeid = vort(bl[at:])
    at += 3
    lentype = int(bl[at])
    at += 1
    return (ver, typeid, lentype)


def lit(bl):
    (v, t, l) = headers(bl)
    nosp = 0
    at = 6
    bits = []
    while bl[at] != '0' and at < len(bl):
        bits.append(bl[at+1:at+5])
        at += 5
    if bl[at] == '0':
        bits.append(bl[at+1:at+5])
        at += 5

    return (btod(''.join(bits)), at)


versions = []


def op1(bl):
    (v, t, l) = headers(bl)
    versions.append(v)
    if t == 4:
        (v, a) = lit(bl)
        return (v, a)
    else:
        nosp = 0
        at = 7
        start0 = 0
        values = []
        if l == 1:
            nosp = btod(bl[at:at+11])
            at += 11
            for _ in range(nosp):
                (v, a) = op1(bl[at:])
                values.append(v)
                at += a
        elif l == 0:
            nosp = btod(bl[at:at+15])
            at += 15
            subpacket = bl[at:at+nosp]
            while start0 < len(subpacket):
                (v, a) = op1(subpacket[start0:])
                values.append(v)
                start0 += a
        return (values, at + start0)


def part1(lines):
    line = lines[0]
    bl = []
    for l in line:
        bl.append(htob[l])
    bl = "".join(bl)
    op1(bl)

    print(sum(versions))


def op2(bl):
    (v, t, l) = headers(bl)
    if t == 4:
        (v, a) = lit(bl)
        return (v, a)
    else:
        nosp = 0
        at = 7
        start0 = 0
        values = []
        if l == 1:
            nosp = btod(bl[at:at+11])
            at += 11
            for _ in range(nosp):
                (v, a) = op2(bl[at:])
                values.append(v)
                at += a
        elif l == 0:
            nosp = btod(bl[at:at+15])
            at += 15
            subpacket = bl[at:at+nosp]
            while start0 < len(subpacket):
                (v, a) = op2(subpacket[start0:])
                values.append(v)
                start0 += a

        if t == 0:
            return (sum(values), at + start0)
        elif t == 1:
            return (prod(values), at + start0)
        elif t == 2:
            return (min(values), at + start0)
        elif t == 3:
            return (max(values), at + start0)
        elif t == 5:
            return (1 if values[0] > values[1] else 0, at + start0)
        elif t == 6:
            return (1 if values[0] < values[1] else 0, at + start0)
        elif t == 7:
            return (1 if values[0] == values[1] else 0, at + start0)
        return (values, at + start0)


def part2(lines):
    line = lines[0]
    bl = []
    for l in line:
        bl.append(htob[l])
    bl = "".join(bl)
    (v, _) = op2(bl)

    print(v)


with open('./d16.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    print('Part 1: [879]')
    part1(lines)
    print('Part 2: [539051801941]')
    part2(lines)
