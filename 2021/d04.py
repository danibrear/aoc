def check_board(board):

    for row in board:
        if sum(row) == 5:
            return True

    col = 0
    while col < 5:
        total = 0
        for row in board:
            if row[col] == 1:
                total += 1
        if total == 5:
            return True
        col += 1

    return False


def calc_board(board, marked_board):
    total = 0
    for y, line in enumerate(marked_board):
        for x, n in enumerate(line):
            if n == 0:
                total += board[y][x]
    return total


def part1(lines):
    numbers = lines[0].replace('\n', '').split(',')

    boards = []

    board = []

    marked_boards = []
    marked_board = []
    for line in lines[2:]:
        line = line.replace('\n', '')
        line = line.replace(r'  ', ' ')
        if len(line) > 0 and line[0] == ' ':
            line = line[1:]
        if len(line) == 0:
            boards.append(board)
            board = []
            marked_boards.append(marked_board)
            marked_board = []
        else:
            l = line.split(' ')
            l = [int(x) for x in l]
            board.append(l)
            marked_board.append([0] * len(l))
    boards.append(board)
    marked_boards.append(marked_board)

    for number in numbers:
        number = int(number)
        for bi, board in enumerate(boards):
            for y, line in enumerate(board):
                for x, n in enumerate(line):
                    if n == number:
                        marked_boards[bi][y][x] = 1

                        winner = check_board(marked_boards[bi])

                        if winner:
                            num = calc_board(boards[bi], marked_boards[bi])
                            print(num * number)
                            return


def part2(lines):
    numbers = lines[0].replace('\n', '').split(',')

    boards = []

    board = []

    marked_boards = []
    marked_board = []
    for line in lines[2:]:
        line = line.replace('\n', '')
        line = line.replace(r'  ', ' ')
        if len(line) > 0 and line[0] == ' ':
            line = line[1:]
        if len(line) == 0:
            boards.append(board)
            board = []
            marked_boards.append(marked_board)
            marked_board = []
        else:
            l = line.split(' ')
            l = [int(x) for x in l]
            board.append(l)
            marked_board.append([0] * len(l))
    boards.append(board)
    marked_boards.append(marked_board)

    won_idx = []

    for number in numbers:
        number = int(number)
        for bi, board in enumerate(boards):
            for y, line in enumerate(board):
                for x, n in enumerate(line):
                    if n == number:
                        marked_boards[bi][y][x] = 1

                        winner = check_board(marked_boards[bi])

                        if winner and bi not in won_idx:
                            if len(won_idx) < len(boards) - 1:
                                won_idx.append(bi)
                            else:
                                num = calc_board(boards[bi], marked_boards[bi])
                                print(num * number)
                                return


with open('./d04.txt', 'r') as f:

    lines = f.readlines()

    part1(lines)
    part2(lines)
