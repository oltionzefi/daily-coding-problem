import array
# if N = 2, 2 => [0, 1, 2] or [0, 2]
# if N = 1, 1 => [0, 1]
# if N = 3, 3 => [0, 1, 2, 3], [0, 1, 3], [0, 2, 3]
# if N = 4, 5 => [0, 1, 2, 3, 4], [0, 1, 2, 4], [0, 1, 3, 4], [0, 2, 3, 4], [0, 2, 4]
# if N = 3, we can jump one step and then we have the solution, and instead we use top stair as first step
# so if N = 1, 1 => [1, 0]
# so if N = 2, 2 => [2, 1, 0], [2, 0]
# so if N = 3. [3, 2, 1, 0], [3, 2, 0], [3, 1, 0] or we have N = 2 which we can use and N = 1
# unique_ways(3) = unique_ways(2) + unique_ways(1)
# if N = 0, we can consider as one way [0]


# not so efficient because we repeat calculation over and over
#              u_ways(5)
#            /           \
#     u_ways(4)           u_ways(3)
#      /      \          /         \
#  u_ways(3) u_ways(3) u_ways(2) u_ways(1)
#   /    \    /    \
# so we repeat calculations over and over
def unique_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return unique_ways(n-1) + unique_ways(n-2)


# bottom-up approach
def unique_ways_bu(n):
    if n == 0 or n == 1:
        return 1
    nums = array.array('i', [0 for i in range(0, n+1)])
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]


# if N and X = {1, 3, 5}
def unique_ways_with_conditions(n, x):
    if n == 0:
        return 1
    total = 0
    for i in x:
        if n - i >= 0:
            total += unique_ways_with_conditions(n-i, x)
    return total


# using bottom-up approach
def unique_ways_with_conditions_bu(n, x):
    if n == 0:
        return 1
    nums = array.array('i', [0 for i in range(0, n+1)])
    nums[0] = 1
    for i in range(1, n+1):
        total = 0
        for j in x:
            if i - j >= 0:
                total += nums[i-j]
        nums[i] = total
    return nums[n]
