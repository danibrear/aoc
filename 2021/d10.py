from collections import deque


def part1(lines):
    score = 0
    stack = deque()
    for line in lines:
        for c in line:
            if c in ['{', '<', '(', '[']:
                stack.append(c)
            elif c == ')':
                if stack.pop() != '(':
                    score += 3
                    break
            elif c == ']':
                if stack.pop() != '[':
                    score += 57
                    break
            elif c == '}':
                if stack.pop() != '{':
                    score += 1197
                    break
            elif c == '>':
                if stack.pop() != '<':
                    score += 25137
                    break
    print(score)


def part2(lines):
    stack = deque()
    incompletes = []
    for line in lines:
        failed = False
        for c in line:
            if c in ['{', '<', '(', '[']:
                stack.append(c)
            elif c == ')':
                if stack.pop() != '(':
                    failed = True
                    break
            elif c == ']':
                if stack.pop() != '[':
                    failed = True
                    break
            elif c == '}':
                if stack.pop() != '{':
                    failed = True
                    break
            elif c == '>':
                if stack.pop() != '<':
                    failed = True
                    break
        if not failed:
            incompletes.append(line)

    stack = deque()
    scores = []
    for line in incompletes:
        for c in line:
            if c == '{' or c == '<' or c == '(' or c == '[':
                stack.append(c)
            elif c == ')':
                stack.pop()
            elif c == ']':
                stack.pop()
            elif c == '}':
                stack.pop()
            elif c == '>':
                stack.pop()

        leftover = []
        while len(stack) > 0:
            d = stack.pop()
            leftover.append(d)
        score = 0
        for c in leftover:
            score *= 5
            if c == '(':
                score += 1
            elif c == '[':
                score += 2
            elif c == '{':
                score += 3
            elif c == '<':
                score += 4
        scores.append(score)

    scores = sorted(scores)

    print(scores[len(scores) // 2])


with open('./d10.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    part1(lines)
    part2(lines)
