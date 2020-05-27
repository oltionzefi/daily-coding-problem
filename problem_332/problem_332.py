def positive_integer_pairs(m, n):
    results = list()

    for a in range(m // 2 + 1 ):
        b = m - a
        if a ^ b == n:
            results.append((a, b))

    return results
