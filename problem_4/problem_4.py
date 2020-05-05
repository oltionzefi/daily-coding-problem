
def lowest_value(arr):
    if len(arr) == 0:
        return 1
    for value in arr:
        if value < 0:
            continue
        arr[value-1] = value

    for value in arr:
        if arr[value] != value + 1:
            return value + 1

    return len(arr) + 1
