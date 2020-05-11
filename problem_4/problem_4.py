# Sorting array from lowest to highest will allow
# us to do a simple check
# 1 - If length of array will be 0, we will return 1
# 2 - Since also for other negative value the next missing positive is 1 will initialize next_missing to 1
# 3 - If in the loop we found something equal or lower we increase the value by 1


def lowest_value(arr):
    sorted(arr)
    next_missing = 1
    if len(arr) == 0:
        return next_missing
    for value in arr:
        if 0 < value <= next_missing:
            next_missing = value + 1

    return next_missing
