def flip_count(string, first_char, second_char):
    length = len(string)

    # we suppose that the first character is same as length, and
    # second character position is in the end
    last_first_char_position, first_second_char_position = length, -1

    # we will find first second_char position
    for i in range(length):
        if string[i] == second_char:
            first_second_char_position = i
            break

    # we will find the last first_char position
    for i in range(length):
        index = length - i - 1
        if string[index] == first_char:
            last_first_char_position = index
            break

    first_char_count, second_char_count = 0, 0

    # lets count how many time second_char is repeated till the last position of first_char
    for i in range(last_first_char_position):
        if string[i] == second_char:
            second_char_count += 1

    # lets count how many time the first_char is repeated after first position of second_char
    for i in range(first_second_char_position + 1, length):
        if string[i] == first_char:
            first_char_count += 1

    return min(first_char_count, second_char_count)
