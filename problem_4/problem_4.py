# Sorting array from lowest to highest will allow
# us to do a simple check
# 1 - If length of array will be 0, we will return 1
# 2 - Since also for other negative value the next missing positive is 1 will initialize next_missing to 1
# 3 - If in the loop we found something equal or lower we increase the value by 1
# For testing purposes we implemented insertion sort


def sorted_f(arr):
    # Uses Timsort algorithm O(n), worst O(n log(n))
    return sorted(arr)


def insertion_f(arr):
    return insertion_sort(arr)


def lowest_value(arr, case=1):
    options = {
        1: sorted_f,
        2: insertion_sort,
    }
    options[case](arr)

    next_missing = 1
    if len(arr) == 0:
        return next_missing
    # O(n) complexity
    for value in arr:
        if 0 < value <= next_missing:
            next_missing = value + 1

    return next_missing


# let create and use insertion sort which has O(n) best and O(n^2) worst
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = cursor

    return arr
