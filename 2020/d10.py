def part1(nums):
    nums = sorted(nums)
    ones = 0
    threes = 1
    curr = 0
    for num in nums:
        if num - curr == 1:
            ones += 1
        elif num - curr == 3:
            threes += 1
        curr = num

    print(ones * threes)


def part2(nums):
    nums = sorted(nums)

    ways_to = {0: 1}

    for num in nums:
        count = 0
        for x in range(1, 4):
            if (num-x) in ways_to:
                count += ways_to[num-x]

        ways_to[num] = count

    print(ways_to[nums[-1]])


with open('./d10.txt', 'r') as f:

    nums = f.readlines()

    nums = map(lambda x: x.replace('\n', ''), nums)
    nums = list(nums)
    nums = map(lambda x: int(x), nums)

    part1(nums)
    part2(nums)
