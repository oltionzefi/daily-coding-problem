# Get count of the nodes in the first list, let count be l1.
# Get count of the nodes in the second list, let count be l2.
# Get the difference of counts d = abs(l1 – l2)
# Now traverse the bigger list from the first node till
# d nodes so that from here onwards both the lists have equal no of nodes.
# Then we can traverse both the lists in parallel till we come across a common node.


def intersection_node(list1, list2):
    l1 = len(list1)
    l2 = len(list2)

    diff = abs(l1 - l2)

    if l1 > l2:
        p = list1[diff:]
        q = list2[:]
    elif l2 > l1:
        p = list1[:]
        q = list2[diff:]
    else:
        p = list1[:]
        q = list2[:]

    for i in range(min(l1, l2)):
        if q[i] == p[i]:
            return q[i]
