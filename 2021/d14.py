from collections import Counter


def spawn(code, secs):
    news = []
    for i in range(len(code) - 1):
        s = code[i:i+2]
        if s in secs:
            news.append((i+1, secs[s]))

    newcode = code[:]
    for _i, (i, n) in enumerate(news):
        newcode = newcode[:i+_i] + n + newcode[i + _i:]

    return newcode


def part1(lines):
    code = lines[0]
    secs = {}
    for line in lines[2:]:
        k, v = line.split(' -> ')
        secs[k] = v

    for x in range(10):
        code = spawn(code, secs)

    c = Counter(code)
    most = c.most_common(1)[0][1]
    less = c.most_common()[-1][1]
    print(most, '-', less, '=', most - less)


def part2(lines):
    code = lines[0]
    secs = {}
    for line in lines[2:]:
        k, v = line.split(' -> ')
        secs[k] = [k[0]+v, v+k[1]]

    d = {}
    for i in range(len(code) - 1):
        s = code[i:i+2]
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1

    for x in range(40):
        newd = {}
        for dk, dv in d.items():
            for nc in secs[dk]:
                if nc not in newd:
                    newd[nc] = dv
                else:
                    newd[nc] += dv
        d = newd

    charcnts = {}
    for dk, dv in d.items():
        for c in dk:
            if c not in charcnts:
                charcnts[c] = dv
            else:
                charcnts[c] += dv

    newcounts = {}
    for k, v in charcnts.items():
        newcounts[k] = v // 2 + (v % 2)

    maxc = max(newcounts.items(), key=lambda x: x[1])[1]
    minc = min(newcounts.items(), key=lambda x: x[1])[1]
    print(maxc, '-', minc, '=', maxc - minc)


with open('./d14.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    part1(lines)
    part2(lines)
