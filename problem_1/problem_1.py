# Recursion!!!
# 1. First we will create a simple solution with simple recursion which will see that it is not efficient
# since does calculation of the values in recursive function a lot of time, so we have repeated calculation
# which makes us worried about performance.
# 2. Second we will try to add a memo for memoization of the values, so we should not repeat calculating
# recursive values over and over, increasing the performance of the function


# First solution
def count_sets(array, total):
    return two_numbers_add_to_sum(array, total, len(array)-1)


def two_numbers_add_to_sum(array, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < array[i]:
        return two_numbers_add_to_sum(array, total, i-1)
    else:
        return two_numbers_add_to_sum(array, total - array[i], i-1) + two_numbers_add_to_sum(array, total, i-1)


# Second solution with memoization
def count_sets_mem(array, total):
    # Empty dictionary
    mem = {}
    return two_numbers_add_to_sum_mem(array, total, len(array)-1, mem)


def two_numbers_add_to_sum_mem(array, total, i, mem):
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < array[i]:
        to_return = two_numbers_add_to_sum_mem(array, total, i-1, mem)
    else:
        to_return = (two_numbers_add_to_sum_mem(array, total - array[i], i-1, mem)
                     + two_numbers_add_to_sum_mem(array, total, i-1, mem))
    mem[key] = to_return
    return to_return

