# 1. we need a function to count the distinct characters of string
# and return them
# 2. lets go through the entire characters and string and build substrings
# which contains all the values
# 3. find the smallest string and its length
# ...
# first solution it is not so efficient and there a technique called sliding window
# Algorithm :
#
# 1. Maintain an array (visited) of maximum possible characters (256 characters)
# and as soon as we find any in the string, mark that index in the array
# (this is to count all distinct characters in the string).
# 2. Take two pointers start and end which will mark the start and end of window.
# 3. Take a counter=0 which will be used to count distinct characters in the window.
# 4. Now start reading the characters of the given string and if we come across a
# character which has not been visited yet increment the counter by 1.
# 5. If the counter is equal to total number of distinct characters, Try to shrink the window.
# 6.For shrinking the window -:
# - If the frequency of character at start pointer is greater than 1 increment the pointer as it is redundant.
# - Now compare the length of present window with the minimum window length.
from collections import defaultdict

MAX_CHARS = 256


def distinct_characters(string):
    return set([x for x in string])


def substring_with_distinct_characters(string, length):
    substrings = []
    distinct_char = distinct_characters(string)
    for value in range(length):
        substr = []
        for v in range(length):
            if string[v] not in substr:
                substr.append(string[v])
        if len(substr) == len(distinct_char):
            substrings.append(substr)

    return substrings


def smallest_window(string):
    return len(min(substring_with_distinct_characters(string, len(string)), key=len))


def smallest_window_sw(string):
    n = len(string)

    distinct_char = len(distinct_characters(string))
    current_count = defaultdict(lambda: 0)
    # set start to 0
    start = 0
    start_index = -1
    count = 0
    min_length = MAX_CHARS
    for value in range(n):
        current_count[string[value]] += 1

        if current_count[string[value]] == 1:
            count += 1

        if count == distinct_char:
            while current_count[string[start]] > 1:
                if current_count[string[start]] > 1:
                    current_count[string[start]] -= 1
                start += 1

            len_window = value - start + 1
            if min_length > len_window:
                min_length = len_window
                start_index = start

    return len(string[start_index: start_index + min_length])
