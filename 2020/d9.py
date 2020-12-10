def part1(nums):

    presize = 25
    preamble = nums[:presize]
    for num in nums[presize:]:
        found = None
        for x in preamble:
            if num - x in preamble and num - x != x:
                found = x
                break
        if found is None:
            print(num)
            return num
        preamble.pop(0)
        preamble.append(num)


def part2(nums, num_to_find):

    arr = []
    index = 0
    found = False
    while index < len(nums) and not found:
        i = index + 2
        while i < len(nums):
            if sum(nums[index:i]) > num_to_find:
                break
            if sum(nums[index:i]) == num_to_find:
                arr = nums[index:i]
                found = True
                break
            i += 1
        index += 1

    print(min(arr) + max(arr))


with open('./d9.txt', 'r') as f:

    nums = f.readlines()

    nums = map(lambda x: x.replace('\n', ''), nums)
    nums = list(nums)
    nums = map(lambda x: int(x), nums)

    num = part1(nums)

    part2(nums, num)
