import array
# if 2 -> "b" ways = 1
# "" -> "" ways = 1
# "12345" -> "a" + ways("2345") or "l" + ways("345")
# "27345" -> "b" + ways("7345")
# "011" -> no 0 ways = 0


def way_of_decoding(data):
    return ways_rec(data, len(data))


# No efficient since repeats calculation O(2^n)
def ways_rec(data, k):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == "0":
        return 0

    result = ways_rec(data, k-1)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += ways_rec(data, k-2)
    return result


# O(n)
def ways_mem(data, k, mem):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == "0":
        return 0
    if mem[k] is not "null":
        return mem[k]

    result = ways_mem(data, k - 1, mem)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += ways_mem(data, k - 2, mem)

    mem[k] = result
    return result


def ways_of_decoding_mem(data):
    mem = ["null"] * (len(data) + 1)
    return ways_mem(data, len(data), mem)
