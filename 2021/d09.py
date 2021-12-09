
def part1(lines):
    mat = []
    for line in lines:
        mat.append([int(x) for x in line])
    mins = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == 0:
                if j == 0:
                    if mat[i][j] < mat[i][j+1] and mat[i][j] < mat[i+1][j]:
                        mins.append(mat[i][j])
                elif j == len(mat[i])-1:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i+1][j]:
                        mins.append(mat[i][j])
                else:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i+1][j] and mat[i][j] < mat[i][j+1]:
                        mins.append(mat[i][j])
            elif i == len(mat)-1:
                if j == 0:
                    if mat[i][j] < mat[i][j+1] and mat[i][j] < mat[i-1][j]:
                        mins.append(mat[i][j])
                elif j == len(mat[i])-1:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i-1][j]:
                        mins.append(mat[i][j])
                else:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i][j+1]:
                        mins.append(mat[i][j])
            else:
                if j == 0:
                    if mat[i][j] < mat[i][j+1] and mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i+1][j]:
                        mins.append(mat[i][j])
                elif j == len(mat[i])-1:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i+1][j]:
                        mins.append(mat[i][j])
                else:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i][j+1] and mat[i][j] < mat[i+1][j] and mat[i][j] < mat[i-1][j]:
                        mins.append(mat[i][j])

    return sum([m + 1 for m in mins])


def part2(lines):
    mat = []
    for line in lines:
        mat.append([int(x) for x in line])
    mins = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == 0:
                if j == 0:
                    if mat[i][j] < mat[i][j+1] and mat[i][j] < mat[i+1][j]:
                        mins.append((i, j))
                elif j == len(mat[i])-1:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i+1][j]:
                        mins.append((i, j))
                else:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i+1][j] and mat[i][j] < mat[i][j+1]:
                        mins.append((i, j))
            elif i == len(mat)-1:
                if j == 0:
                    if mat[i][j] < mat[i][j+1] and mat[i][j] < mat[i-1][j]:
                        mins.append((i, j))
                elif j == len(mat[i])-1:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i-1][j]:
                        mins.append((i, j))
                else:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i][j+1]:
                        mins.append((i, j))
            else:
                if j == 0:
                    if mat[i][j] < mat[i][j+1] and mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i+1][j]:
                        mins.append((i, j))
                elif j == len(mat[i])-1:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i+1][j]:
                        mins.append((i, j))
                else:
                    if mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i][j+1] and mat[i][j] < mat[i+1][j] and mat[i][j] < mat[i-1][j]:
                        mins.append((i, j))

    seen = set()
    basins = {}
    for m in mins:
        (i, j) = m
        tosee = []
        if i > 0:
            tosee.append((i-1, j))
        if i < len(mat)-1:
            tosee.append((i+1, j))
        if j > 0:
            tosee.append((i, j-1))
        if j < len(mat[i])-1:
            tosee.append((i, j+1))
        seen.add(m)
        basins[m] = 1
        while len(tosee) > 0:
            (i, j) = tosee.pop()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if (i, j) in tosee or mat[i][j] == 9:
                continue
            if i > 0 and (i-1, j) not in seen and (i-1, j) not in tosee:
                tosee.append((i-1, j))
            if i < len(mat)-1 and (i+1, j) not in seen and (i+1, j) not in tosee:
                tosee.append((i+1, j))
            if j > 0 and (i, j-1) not in seen and (i, j-1) not in tosee:
                tosee.append((i, j-1))
            if j < len(mat[i])-1 and (i, j+1) not in seen and (i, j+1) not in tosee:
                tosee.append((i, j+1))
            basins[m] += 1

    x = 1
    vals = list(basins.values())
    vals = sorted(vals)
    for b in vals[-3:]:
        x *= b
    return x


with open('./d09.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    print('Part 1 correct: [566] {}'.format(part1(lines)))
    print('Part 2 correct: [891684] {}'.format(part2(lines)))
