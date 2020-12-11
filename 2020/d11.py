from copy import deepcopy


def part1(rows):

    def check_around(row, col, layout):
        occupied = 0
        max_col = len(layout[0]) - 1
        max_row = len(layout) - 1
        if (row > 0):
            if (col > 0 and layout[row-1][col-1] == '#'):
                occupied += 1
            if (layout[row-1][col] == '#'):
                occupied += 1
            if (col < max_col and layout[row-1][col+1] == '#'):
                occupied += 1
        if (col > 0 and layout[row][col-1] == '#'):
            occupied += 1
        if (col < max_col and layout[row][col+1] == '#'):
            occupied += 1
        if (row < max_row):
            if (col > 0 and layout[row+1][col-1] == '#'):
                occupied += 1
            if (layout[row+1][col] == '#'):
                occupied += 1
            if (col < max_col and layout[row+1][col+1] == '#'):
                occupied += 1

        return occupied

    def count_occupied(layout):
        occupied = 0
        for row in layout:
            for col in row:
                if col == '#':
                    occupied += 1
        return occupied

    curr_layout = deepcopy(rows)

    occupied_count = count_occupied(curr_layout)
    new_occupied_count = -1
    counter = 0
    while new_occupied_count != occupied_count:
        occupied_count = new_occupied_count
        next_layout = []
        for y, row in enumerate(curr_layout):
            next_row = []
            for x, col in enumerate(row):

                if col == '.':
                    next_row.append('.')
                    continue
                occupied_seats = check_around(y, x, curr_layout)
                if col == 'L':
                    if occupied_seats == 0:
                        next_row.append('#')
                    else:
                        next_row.append('L')
                    continue
                if col == '#':
                    if occupied_seats >= 4:
                        next_row.append('L')
                    else:
                        next_row.append('#')
                    continue
            next_layout.append(next_row)

        # if (counter == 1):
        #     print(curr_layout[0][3], next_layout[0]
        #           [3], check_around(0, 3, curr_layout))
        #     for row in next_layout:
        #         print(row)
        #     print('\n\n')
        new_occupied_count = count_occupied(next_layout)

        curr_layout = next_layout
        counter += 1

    print(occupied_count)


def part2(rows):

    def check_line(row_diff, col_diff, row, col, layout):
        curr_row = row
        curr_col = col
        curr_row += row_diff
        curr_col += col_diff
        while (curr_row >= 0 and curr_row < len(layout) and curr_col >= 0 and curr_col < len(layout[0])):
            if layout[curr_row][curr_col] == '#':
                return 1
            if layout[curr_row][curr_col] == 'L':
                return 0
            curr_row += row_diff
            curr_col += col_diff

        return 0

    def check_around(row, col, layout):
        occupied = 0
        occupied += check_line(-1, -1, row, col, layout)
        occupied += check_line(-1, 0, row, col, layout)
        occupied += check_line(-1, 1, row, col, layout)
        occupied += check_line(0, -1, row, col, layout)
        occupied += check_line(0, 1, row, col, layout)
        occupied += check_line(1, -1, row, col, layout)
        occupied += check_line(1, 0, row, col, layout)
        occupied += check_line(1, 1, row, col, layout)
        return occupied

    def count_occupied(layout):
        occupied = 0
        for row in layout:
            for col in row:
                if col == '#':
                    occupied += 1
        return occupied

    curr_layout = deepcopy(rows)

    occupied_count = count_occupied(curr_layout)
    new_occupied_count = -1
    counter = 0
    runs = 0
    while counter < 5:
        occupied_count = new_occupied_count
        next_layout = []
        for y, row in enumerate(curr_layout):
            next_row = []
            for x, col in enumerate(row):

                if col == '.':
                    next_row.append('.')
                    continue
                occupied_seats = check_around(y, x, curr_layout)
                if col == 'L':
                    if occupied_seats == 0:
                        next_row.append('#')
                    else:
                        next_row.append('L')
                    continue
                if col == '#':
                    if occupied_seats >= 5:
                        next_row.append('L')
                    else:
                        next_row.append('#')
                    continue
            next_layout.append(next_row)

        # if (runs <= 1):
        #     print(curr_layout[0][2], check_around(0, 2, curr_layout))
        #     for row in next_layout:
        #         print(''.join(row))
        #     print('\n\n')
        # if runs > 1:
        #     return
        new_occupied_count = count_occupied(next_layout)

        if new_occupied_count == occupied_count:
            counter += 1
        else:
            counter = 0

        curr_layout = next_layout

        runs += 1

    print(occupied_count)


with open('./d11.txt', 'r') as f:

    rows = f.readlines()

    rows = list(rows)
    rows = map(lambda x: x.replace('\n', ''), rows)

    part1(rows)
    part2(rows)
