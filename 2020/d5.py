import math


def get_row(directions):
    high = 127.
    low = 0
    mid = low + int(math.ceil((high - low) / 2))
    for c in directions:
        if c == 'F':
            high = mid
        elif c == 'B':
            low = mid
        mid = low + int(math.ceil((high - low) / 2))

    return mid


def get_col(directions):
    high = 7.
    low = 0
    mid = low + int(math.ceil((high - low) / 2))
    for c in directions:
        if c == 'L':
            high = mid
        elif c == 'R':
            low = mid
        mid = low + int(math.ceil((high - low) / 2))

    return mid


def get_seat(line):
    first = line[:7]
    last = line[7:]
    row = get_row(first)
    col = get_col(last)

    seat = row * 8 + col

    return seat


def part1(lines):
    highest = 0
    for line in lines:
        seat = get_seat(line)

        if seat > highest:
            highest = seat

    print(highest)


def part2(lines):
    min_seat = float('inf')
    max_seat = 0
    seats = {}
    for line in lines:
        seat = get_seat(line)

        if seat > max_seat:
            max_seat = seat
        if seat < min_seat:
            min_seat = seat

        seats[seat] = 1

    for x in range(min_seat, max_seat):
        if x-1 in seats and x+1 in seats and x not in seats:
            print(x)

    # print(highest)


with open('./d5.txt', 'r') as f:

    lines = f.readlines()

    lines = map(lambda x: x.replace('\n', ''), lines)
    lines = list(lines)

    part1(lines)
    part2(lines)
