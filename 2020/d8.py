import copy


def part1(lines):
    current_index = 0
    accumulator = 0

    seen_indexes = set()

    while current_index not in seen_indexes and current_index < len(lines):
        seen_indexes.add(current_index)

        op, val = lines[current_index].split(' ')
        if op == 'acc':
            accumulator += int(val)
            current_index += 1
        elif op == 'jmp':
            current_index += int(val)
        elif op == 'nop':
            current_index += 1

    print(accumulator)


def run_acc(lines):
    current_index = 0
    accumulator = 0

    seen_indexes = set()
    while current_index not in seen_indexes and current_index < len(lines):
        seen_indexes.add(current_index)

        op, val = lines[current_index].split(' ')
        if op == 'acc':
            accumulator += int(val)
            current_index += 1
        elif op == 'jmp':
            current_index += int(val)
        elif op == 'nop':
            current_index += 1

    if (current_index in seen_indexes):
        return -1

    return accumulator


def part2(lines):

    last_idx = len(lines) - 1

    found_value = 0

    while last_idx > 0:
        new_lines = copy.deepcopy(lines)
        val = -1
        if lines[last_idx].startswith('jmp'):
            new_lines[last_idx] = 'nop -1'
            val = run_acc(new_lines)
        elif lines[last_idx].startswith('nop'):
            _, value = lines[last_idx].split(' ')
            new_lines[last_idx] = 'nop '+value
            val = run_acc(new_lines)

        if val > 0:
            found_value = val
            break
        last_idx -= 1

    print(found_value)


with open('./d8.txt', 'r') as f:

    lines = f.readlines()

    lines = map(lambda x: x.replace('\n', ''), lines)
    lines = list(lines)

    part1(lines)
    part2(lines)
