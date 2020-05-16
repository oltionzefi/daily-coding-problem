# 1. to better jump from the the number if we would have the list of
# divisor for the number will make checking much more easy
# 2. then will create a function which will calculate the lowest divisor which
# we can jump to it
# 3. as last part will go through the process of jumping
import math


def divisor_generator(number):
    large_divisors = []
    for i in range(1, int(math.sqrt(number) + 1)):
        if number % i == 0:
            yield i
            if i * i != number:
                large_divisors.append(number / i)
    for divisor in reversed(large_divisors):
        yield divisor


def lowest_divisor(number):
    divisors = list(divisor_generator(number))
    lowest_usable_values = []
    for divisor in divisors:
        value = number / divisor
        lowest_usable_values.append(max(value, divisor))

    return int(min(lowest_usable_values))


def smaller_number_steps(number):
    path = [number]
    while number > 1:
        lowest = lowest_divisor(number)
        if lowest and lowest not in path:
            number = lowest
        else:
            number -= 1
        path.append(number)

    return ' -> '.join([str(value) for value in path])
