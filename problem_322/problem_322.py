import sys
# At any step i, we can move forward i, then backward i + 1.
# Since distance of + 5 and – 5 from 0 is same, hence we find answer for absolute value of destination.
# If at any point if current value is bigger or same as destination destination; return number of steps.
# From any vertex we can go to :
# positive -> current value + last step +1
# negative -> current value – last step -1


def path_steps(start, step, destination):
    # best case 1
    if abs(start) > destination:
        return sys.maxsize
    # best case 2
    if start == destination:
        return step

    positive_jump = path_steps(start + step + 1, step + 1, destination)
    negative_jump = path_steps(start - step - 1, step + 1, destination)

    # print(negative_jump)
    return min(positive_jump, negative_jump)
