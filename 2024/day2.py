from utils import aslist, splitlines, ingroups, getday, getpath

def issafe(nums):
    inc = nums[0] < nums[1]
    safe = True
    for i in range(0, len(nums)-1):
        if nums[i] == nums[i+1]:
            return [False, i]
        if inc and nums[i] > nums[i+1]:
            return [False, i]
        if not inc and nums[i] < nums[i+1]:
            return [False, i]
        if inc and nums[i+1] > nums[i]+3:
            return [False, i]
        if not inc and nums[i]-3 > nums[i+1]:
            return [False, i]
    return [True, -1]

def part1(lines):
    safelines = 0
    for line in lines:
        nums = list(map(lambda x: int(x), line.split(' ')))
        [safe, _] = issafe(nums)
        if safe:
            safelines += 1
    print(safelines)

def part2(lines):
    safelines = 0
    for line in lines:
        nums = list(map(lambda x: int(x), line.split(' ')))
        [safe, idx] = issafe(nums)

        if not safe:
            n2 = nums.copy()
            n2.pop(idx)
            safe = issafe(n2)[0]
        if not safe:
            n2 = nums.copy()
            n2.pop(idx+1)
            safe = issafe(n2)[0]
        if not safe:
            n2 = nums.copy()
            n2.pop(idx-1)
            safe = issafe(n2)[0]
        if safe:
            safelines += 1
    print(safelines)


path = getpath(__file__)
with open('{}/day2.txt'.format(path), 'r') as f:

    lines = f.readlines()

    lines = aslist(lines)

    part1(lines)
    part2(lines)