def minWithIndex(arr):
    """Return the minimum value and its index in the array."""
    minVal = arr[0]
    minIdx = 0
    for i in range(1, len(arr)):
        if arr[i] < minVal:
            minVal = arr[i]
            minIdx = i
    return [minIdx, minVal]