def part1(groups):

    total_questions = 0
    for group in groups:
        questions = {}
        for person in group:
            for c in person:
                questions[c] = 1

        total_questions += len(questions)

    print(total_questions)


def part2(groups):

    total_questions = 0
    for group in groups:
        questions = {}
        for person in group:
            for c in person:
                if c not in questions:
                    questions[c] = 1
                else:
                    questions[c] += 1

        for v in questions.values():
            if v == len(group):
                total_questions += 1

    print(total_questions)


with open('./d6.txt', 'r') as f:

    lines = f.readlines()

    lines = map(lambda x: x.replace('\n', ''), lines)
    lines = list(lines)

    groups = []
    group = []
    for line in lines:
        if (len(line) == 0):
            groups.append(group)
            group = []
            continue

        group.append(line)

    groups.append(group)

    part1(groups)
    part2(groups)
