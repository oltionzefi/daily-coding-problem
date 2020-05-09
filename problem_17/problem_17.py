def longest_path(source):
    items = source.split("\n")

    for path in items:
        level = 0
        while path[level] == "\t":
            level += 1

    return