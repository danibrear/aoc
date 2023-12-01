from utils import aslist, splitlines, ingroups, getday, getpath
import re

def part1(lines):
    total = 0
    for line in lines:
        nums = re.findall(r'[0-9]{1}', line)
        total += int(nums[0]+nums[-1])

    print(total)
    pass


def part2(lines):
    total = 0
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in lines:
        firstText = min([100] + [line.find(num) for num in nums if line.find(num) != -1])
        firstDig = min([100] + [line.find(str(i)) for i in range(1, 10) if line.find(str(i)) != -1])

        if (firstText < firstDig):
            dig = [line[firstText:firstText+len(num)] == num for num in nums].index(True) + 1
            firstDig = dig
        else:
            dig = int(line[firstDig])
            firstDig = dig

        secondText = max([0] + [line.rfind(num) for num in nums if line.rfind(num) != -1])
        secondDig = max([0] + [line.rfind(str(i)) for i in range(1, 10) if line.rfind(str(i)) != -1])
        if (secondText > secondDig):
            dig = [line[secondText:secondText+len(num)] == num for num in nums].index(True) + 1
            secondDig = dig
        else:
            dig = int(line[secondDig])
            secondDig = dig
        total += firstDig * 10 + secondDig

    print(total)

day = getday(__file__)
path = getpath(__file__)
print('path', path)
with open('./{}/{}.txt'.format(path, day), 'r') as f:

    lines = f.readlines()

    lines = aslist(lines)

    part1(lines)
    part2(lines)