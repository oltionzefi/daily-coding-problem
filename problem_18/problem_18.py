import collections
# Time Complexity: O(N * K).
# The outer loop runs n-k+1 times and the inner loop runs k times for every iteration of outer loop.
# So time complexity is O((n-k+1)*k) which can also be written as O(N * K).
# Space Complexity: O(1).
# No extra space is required.


def max_val_sub_arrays(array, n, k):
    values = []

    for i in range(n - k + 1):
        max_value = array[i]
        for j in range(1, k):
            if array[i+j] > max_value:
                max_value = array[i + j]
        values.append(max_value)
    return values


def max_sub_arrays(array, k):
    return max_val_sub_arrays(array, len(array), k)


# Time Complexity: O(n).
# It seems more than O(n) at first look. It can be observed that every element of
# array is added and removed at most once. So there are total 2n operations.
# Auxiliary Space: O(k).
# Elements stored in the dequeue take O(k) space.


def max_value_sub_arrays_deque(array, n, k):
    values = []
    queue = collections.deque()

    for i in range(k):
        while queue and array[i] >= array[queue[-1]]:
            queue.pop()
        queue.append(i)

    for i in range(k, n):
        values.append(array[queue[0]])
        while queue and queue[0] <= i-k:
            queue.popleft()
            print(queue)

        while queue and array[i] >= array[queue[-1]]:
            queue.pop()

        queue.append(i)

    values.append(array[queue[0]])
    return values


def max_sub_arrays_deque(array, k):
    return max_value_sub_arrays_deque(array, len(array), k)
