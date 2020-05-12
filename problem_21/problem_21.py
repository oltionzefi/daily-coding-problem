# Checking for each interval the next intervals if has start
# lower then actual end


def rooms(intervals):
    min_rooms = 0
    for key, value in enumerate(intervals):
        lesson = intervals[key]
        required = 1
        for vm in intervals:
            if vm[0] > lesson[1]:
                required += 1
        if required > min_rooms:
            min_rooms = required

    return min_rooms


def rooms_sorted(intervals):
    dict_intervals = {}
    # O(n)
    for v in intervals:
        dict_intervals[v[0]] = dict_intervals[v[0]] + 1 if v[0] in dict_intervals else 1
        dict_intervals[v[1]] = dict_intervals[v[1]] - 1 if v[1] in dict_intervals else -1
    # Timsort algorithm O(n.log(n))

    sorted_events = sorted(dict_intervals.items())
    min_rooms = 0

    rooms_available = 0
    # O(n)
    for k, v in sorted_events:
        rooms_available += v
        if rooms_available > min_rooms:
            min_rooms = rooms_available
    return min_rooms
