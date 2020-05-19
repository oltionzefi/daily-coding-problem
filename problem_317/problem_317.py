# 1.
# Find position of Most Significant Bit (MSB) in both numbers.
# If positions of MSB are different, then result is 0.
# If positions are same. Let positions be msb_position.
# ……a) We add 2msb_position to result.
# ……b) We subtract 2msb_position from lower limit and upper limit,
# ……c) Repeat steps 1, 2 and 3 for new values of lower limit and upper limit.
# 2.
# Flip the LSB of upper limit.
# And check if the new number is in range(lower limit < number < upper limit) or not
# if the number greater than 'lower limit' again flip lsb
# if it is not then that's the answer


def msb_position(number):
    msb_pos = -1
    while number > 0:
        number = number >> 1
        msb_pos += 1
    return msb_pos


def bitwise_and(lower_limit, upper_limit):
    result = 0

    while lower_limit > 0 and upper_limit > 0:
        msb_pos1 = msb_position(lower_limit)
        msb_pos2 = msb_position(upper_limit)
        if msb_pos1 != msb_pos2:
            break

        msb_val = (1 << msb_pos1)
        result = result + msb_val

        lower_limit = lower_limit - msb_val
        upper_limit = upper_limit - msb_val

    return result


def bitwise_and_with_lsb(lower_limit, upper_limit):
    while lower_limit < upper_limit:
        upper_limit -= (upper_limit & -upper_limit)

    return upper_limit
