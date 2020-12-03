def part1(lines):
    row = 1
    col = 3
    max_col = len(lines[0])
    trees = 0
    while row < len(lines):
        print('row', row)
        if lines[row][col] == '#':
            trees += 1
        row += 1
        col += 3
        col = col % max_col
    print(trees)


def part2(lines):

    def part2_sub(lines, rowinc, colinc):
        row = rowinc
        col = colinc
        max_col = len(lines[0])
        trees = 0
        while row < len(lines):
            if lines[row][col] == '#':
                trees += 1
            row += rowinc
            col += colinc
            col = col % max_col
        return trees

    val = 1
    val *= part2_sub(lines, 1, 1)
    val *= part2_sub(lines, 1, 3)
    val *= part2_sub(lines, 1, 5)
    val *= part2_sub(lines, 1, 7)
    val *= part2_sub(lines, 2, 1)
    print(val)


with open('./d3.txt', 'r') as f:

    lines = f.readlines()

    lines = map(lambda x: x.replace('\n', ''), lines)
    lines = list(lines)

    part1(lines)
    part2(lines)
