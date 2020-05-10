import sys
# give this example
# 1 | 2 | 3
# 4 | 8 | 2
# 1 | 5 | 3
# the minimum cost to go to path (2, 2) is
# 1 (x) | 2 (x) | 3
# 4 | 8 | 2 (x)
# 1 | 5 | 3 (x)
# to reach (m, n) must be through one of 3 cells (m-1, n-1) or (m-1, n) or (m, n-1)
# plus cost(m, n)

R = 3
C = 3


# using Minimum Cost Path
def min_cost(cost, m, n):
    if n < 0 or m < 0:
        return sys.maxsize
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        return cost[m][n] + min(min_cost(cost, m-1, n-1), min_cost(cost, m-1, n), min_cost(cost, m, n-1))


# but this solution repeat computational of recursive functions
#                                                min_cost(cost, 2, 2)
#                              /                             |                    \ ...
#                    min_cost(cost, 1, 1)               min_cost(cost, 1, 2) ...
#                    /              \                        /  ...
#             min_cost(cost, 0, 0) min_cost(0,1) ...   min_cost(cost, 0, 1) ...
# so we try with bottom up approach
def min_cost_bu(cost, m, n):
    total_cost = [[0 for i in range(C)] for i in range(R)]

    total_cost[0][0] = cost[0][0]

    # first column of total_cost
    for i in range(1, m+1):
        total_cost[i][0] = total_cost[i-1][0] + cost[i][0]

    # first row of total_cost
    for j in range(1, n+1):
        total_cost[0][j] = total_cost[0][j-1] + cost[0][j]

    # rest of cost
    for i in range(1, m+1):
        for j in range(1, n+1):
            total_cost[i][j] = min(total_cost[i-1][j-1], total_cost[i-1][j], total_cost[i][j-1]) + cost[i][j]

    return total_cost[m][n]
