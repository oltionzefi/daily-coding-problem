def stable_marriage(guy_preferences, gal_preferences):
    if not guy_preferences:
        return []

    matches = list()
    taken_guys, taken_gals = set(), set()

    for guy in guy_preferences:
        gal = guy_preferences[guy][0]
        preference_guy = gal_preferences[gal][0]

        if preference_guy == guy:
            matches.append((guy, gal))
            taken_guys.add(guy)
            taken_gals.add(gal)

    if not matches:
        for guy in guy_preferences:
            gal = guy_preferences[guy][0]
            matches.append((guy, gal))
        return matches

    for (guy, gal) in matches:
        del guy_preferences[guy]
        del gal_preferences[gal]

        for a_guy in guy_preferences:
            guy_preferences[a_guy] = [x for x in guy_preferences[a_guy] if x not in taken_guys]

        for a_gal in gal_preferences:
            gal_preferences[a_gal] = [x for x in gal_preferences[a_gal] if x not in taken_gals]

    return matches + stable_marriage(guy_preferences, gal_preferences)
