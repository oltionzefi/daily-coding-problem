# Use of loop


def production(array, actual_key):
    prod = 1
    for key, value in enumerate(array):
        if key == actual_key:
            prod *= 1
        else:
            prod *= value

    return prod


def prod_element(array):
    prod_array = []
    for key, _ in enumerate(array):
        prod_array.insert(key, production(array, key))

    return prod_array


def production_rec(array, result, actual_key):
    if not array:
        return result
    else:
        return production_rec(array, result * array.pop(), actual_key)


def prod_element_rec(array):
    prod_array = []
    for key, _ in enumerate(array):
        array_to_calculate = list(array)
        del array_to_calculate[key]
        prod_array.insert(key, production_rec(array_to_calculate, 1, key))

    return prod_array


def production_rec_mem(array, result, actual_key, mem):
    key = ':'.join([str(value) for value in array])
    if key in mem:
        return mem[key]
    if not array:
        to_return = result
    else:
        to_return = production_rec(array, result * array.pop(), actual_key)

    mem[key] = to_return
    return to_return


def prod_element_rec_mem(array):
    mem = {}
    prod_array = []
    for key, _ in enumerate(array):
        array_to_calculate = list(array)
        del array_to_calculate[key]
        prod_array.insert(key, production_rec_mem(array_to_calculate, 1, key, mem))

    return prod_array
