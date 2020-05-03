# incl : For a given i, this variable will represent the largest sum derived by adding arr[i].
# excl : For a given i, this variable will represent the largest sum derived by not adding arr[i]
# ex: [2, 4, 6, 2, 5] return 13


def find_max_sum(array):
    incl = 0
    excl = 0

    for value in array:
        # Max excluding i
        new_excl = excl if excl > incl else incl

        # Max including i
        incl = excl + value
        excl = new_excl

    return excl if excl > incl else incl
