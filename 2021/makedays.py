template = f'''
def part1(lines):
    for line in lines:
        pass


def part2(lines):
    for line in lines:
        pass


with open('./d__DAY__.txt', 'r') as f:

    lines = f.readlines()

    part1(lines)
    part2(lines)

'''

for x in range(3, 26):

    with open(f"d{x}.py", "w") as f:
        f.write(template.replace('__DAY__', str(x)))
    with open(f"d{x}.txt", "w") as f:
        f.write("")
    with open(f"d{x}-test.txt", "w") as f:
        f.write("")
