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
