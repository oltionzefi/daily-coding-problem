def get_celebrity(known):
    celebrities = set(known.keys())

    while celebrities:
        celebrity = next(iter(celebrities))
        celebrities.remove(celebrity)

        count = len(celebrities)

        for other in celebrities:
            if not knows(known, celebrity, other):
                count -= 1

        if count == 0:
            return celebrity


def knows(known, a, b):
    return b in known[a]
