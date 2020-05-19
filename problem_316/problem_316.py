def denominations(array):
    den_list = []
    for i in range(len(array)):
        # since there is no coin with value 0
        if i == 0:
            continue
        if array[i] > 0:
            if not den_list:
                den_list.append(i)
                continue
            if len(den_list) > 0:
                min_coins = get_min_coins(i, den_list)
                if min_coins != 0:
                    den_list.append(i)

    return ", ".join([str(val) for val in den_list])


def get_min_coins(amount, denoms):
    print('amount', amount)
    print('denoms', denoms)
    if amount == 0:
        return 0

    coins_used = None
    denom_to_use, index_cutoff = None, None
    for x, denom in enumerate(denoms):
        if amount >= denom:
            denom_to_use = denom
            index_cutoff = x
            break

    try:
        coins_used = amount // denom_to_use
    except TypeError:
        coins_used = None

    if coins_used is not None and amount - (denom_to_use * coins_used) in denoms:
        return coins_used + get_min_coins(amount - (denom_to_use * coins_used), denoms[index_cutoff + 1:])
    else:
        return coins_used + get_min_coins(amount - denom_to_use, denoms[index_cutoff + 1:])
