def minWithIndex(arr):
    """Return the minimum value and its index in the array."""
    minVal = arr[0]
    minIdx = 0
    for i in range(1, len(arr)):
        if arr[i] < minVal:
            minVal = arr[i]
            minIdx = i
    return [minIdx, minVal]


def maxWithIndex(arr):
    """Return the maximum value and its index in the array."""
    maxVal = arr[0]
    maxIdx = 0
    for i in range(1, len(arr)):
        if arr[i] > maxVal:
            maxVal = arr[i]
            maxIdx = i
    return [maxIdx, maxVal]


def testMatrix(matrix, row=0, col=0, test=lambda x: True, default=False):
    if row < 0 or row >= len(matrix):
        return default
    if col < 0 or col >= len(matrix[0]):
        return default

    return test(matrix[row][col])


def anyInMatrix(
    matrix,
    row=0,
    col=0,
    test=lambda x: True,
    diagonal=True,
    default=False,
    forDirection={
        "up": lambda x: True,
        "down": lambda x: True,
        "left": lambda x: True,
        "right": lambda x: True,
        "upLeft": lambda x: True,
        "upRight": lambda x: True,
        "downLeft": lambda x: True,
        "downRight": lambda x: True,
    },
):
    if testMatrix(matrix, row, col - 1, test, default) and forDirection["left"](
        matrix[row][col - 1]
    ):
        return True
    if testMatrix(matrix, row, col + 1, test, default) and forDirection["right"](
        matrix[row][col + 1]
    ):
        return True
    if testMatrix(matrix, row - 1, col, test, default) and forDirection["up"](
        matrix[row - 1][col]
    ):
        return True
    if testMatrix(matrix, row + 1, col, test, default) and forDirection["down"](
        matrix[row + 1][col]
    ):
        return True
    if (
        diagonal
        and testMatrix(matrix, row - 1, col - 1, test, default)
        and forDirection["upLeft"](matrix[row - 1][col - 1])
    ):
        return True
    if (
        diagonal
        and testMatrix(matrix, row + 1, col - 1, test, default)
        and forDirection["downLeft"](matrix[row + 1][col - 1])
    ):
        return True
    if (
        diagonal
        and testMatrix(matrix, row - 1, col + 1, test, default)
        and forDirection["upRight"](matrix[row - 1][col + 1])
    ):
        return True
    if (
        diagonal
        and testMatrix(matrix, row + 1, col + 1, test, default)
        and forDirection["downRight"](matrix[row + 1][col + 1])
    ):
        return True
    return default
