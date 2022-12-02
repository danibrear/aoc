

def part1(lines):
    score = 0
    for line in lines:
        win = False
        draw = False
        lose = False
        [them, me] = line.replace('\n', '').split(' ')
        if me == 'X':
            score += 1
        elif me == 'Y':
            score += 2
        elif me == 'Z':
            score += 3
        if them == 'A':
            if me == 'X':
                draw = True
            elif me == 'Y':
                win = True
            elif me == 'Z':
                lose = True
        elif them == 'B':
            if me == 'X':
                lose = True
            elif me == 'Y':
                draw = True
            elif me == 'Z':
                win = True
        elif them == 'C':
            if me == 'X':
                win = True
            elif me == 'Y':
                lose = True
            elif me == 'Z':
                draw = True
        if win:
            score += 6
        elif draw:
            score += 3
        elif lose:
            score += 0

    print(score)

def part2(lines):
    score = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    for line in lines:
        [them, me] = line.replace('\n', '').split(' ')
        if me == 'X':
            score += 0
        elif me == 'Y':
            score += 3
        elif me == 'Z':
            score += 6
        if them == 'A':
            if me == 'X':
                score += SCISSORS
            elif me == 'Y':
                score += ROCK
            elif me == 'Z':
                score += PAPER
        elif them == 'B':
            if me == 'X':
                score += ROCK
            elif me == 'Y':
                score += PAPER
            elif me == 'Z':
                score += SCISSORS
        elif them == 'C':
            if me == 'X':
                score += PAPER
            elif me == 'Y':
                score += SCISSORS
            elif me == 'Z':
                score += ROCK

    print(score)

with open('./day2.txt', 'r') as f:

    lines = f.readlines()

    part1(lines)
    part2(lines)
