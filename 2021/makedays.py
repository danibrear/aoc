template = '''
import re
from collections import *

def part1(lines):
    for line in lines:
        pass


def part2(lines):
    for line in lines:
        pass


with open('./d__DAY__.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.strip()), lines))

    part1(lines)
    part2(lines)

'''

for x in range(1, 26):

    dayStr = str(x).zfill(2)
    with open(f"d{dayStr}.py", "w") as f:
        f.write(template.replace('__DAY__', dayStr))
    with open(f"d{dayStr}.txt", "w") as f:
        f.write("")
    with open(f"d{dayStr}-test.txt", "w") as f:
        f.write("")
