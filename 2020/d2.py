def part1(lines):
    right = 0

    for line in lines:
        [start, end] = line.split(':')
        [count, letter] = start.split(' ')

        [low, high] = count.split('-')
        low = int(low)
        high = int(high)

        end = end[1:].replace('\n', '')

        charcount = 0
        for c in end:
            print(c)
            if c == letter:
                charcount += 1

        if (charcount <= high and charcount >= low):
            right += 1

    print(right)


def part2(lines):
    right = 0

    for line in lines:
        [start, end] = line.split(':')
        [count, letter] = start.split(' ')

        [low, high] = count.split('-')
        low = int(low)
        high = int(high)

        end = end[1:].replace('\n', '')
        if (end[low - 1] == letter and end[high - 1] != letter) or \
                (end[low - 1] != letter and end[high - 1] == letter):
            right += 1

    print(right)


with open('./d2.txt', 'r') as f:

    lines = f.readlines()

    part1(lines)
    part2(lines)
