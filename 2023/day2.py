from utils import aslist, splitlines, ingroups, getday, getpath

red = 12
green = 13
blue = 14

def part1(lines):
    total = 0
    for line in lines:
        parts = line.split(': ')
        gameParts = parts[0].split(' ')
        game = int(gameParts[1])
        reveals = parts[1].split('; ')
        possible = True
        for reveal in reveals:
            counts = reveal.split(', ')
            for count in counts:
                countParts = count.split(' ')
                num = int(countParts[0])
                color = countParts[1]
                if color == 'red' and num > red:
                    possible = False
                if color == 'green' and num > green:
                    possible = False
                if color == 'blue' and num > blue:
                    possible = False
                if not possible:
                    break
            if not possible:
                break
        if possible:
            total += game
    print(total)

def part2(lines):
    total = 0
    for line in lines:
        minRed = 0
        minGreen = 0
        minBlue = 0
        parts = line.split(': ')
        gameParts = parts[0].split(' ')
        game = int(gameParts[1])
        reveals = parts[1].split('; ')
        for reveal in reveals:
            counts = reveal.split(', ')
            for count in counts:
                countParts = count.split(' ')
                num = int(countParts[0])
                color = countParts[1]
                if color == 'red' and num > minRed:
                    minRed = num
                if color == 'green' and num > minGreen:
                    minGreen = num
                if color == 'blue' and num > minBlue:
                    minBlue = num
        total += minRed * minGreen * minBlue
    print(total)


path = getpath(__file__)
with open('{}/day2.txt'.format(path), 'r') as f:

    lines = f.readlines()

    lines = aslist(lines)

    part1(lines) # 1867
    part2(lines) # 84538