visited = []
visitedInv = []
adj = []
adjInv = []
stack = []
score = []


def dfs_1(u):
    if visited[u]:
        return

    visited[u] = 1

    for i in range(len(adj[u])):
        dfs_1(adj[u][i])

    stack.append(u)


def dfs_2(u, counter):
    if visitedInv[u]:
        return

    visitedInv[u] = 1

    for i in range(len(adjInv[u])):
        dfs_2(adjInv[u][i])

    score[u] = counter


def add_edges(a, b):
    adj[a].append(b)


def add_edges_inverse(a, b):
    adjInv[b].append(a)


def is2_cnf_satisfiable(n, m, a, b):
    counter = 1
    for i in range(m):
        if a[i] > 0 and b[i] > 0:
            add_edges(a[i] + n, b[i])
            add_edges_inverse(a[i] + n, b[i])
            add_edges(b[i] + n, a[i])
            add_edges_inverse(b[i] + n, a[i])
        elif a[i] < 0 and b[i] < 0:
            add_edges(a[i] + n, n-b[i])
            add_edges_inverse(a[i] + n, n-b[i])
            add_edges(-b[i], a[i])
            add_edges_inverse(-b[i], a[i])
        elif a[i] < 0 and b[i] > 0:
            add_edges(-a[i], b[i])
            add_edges_inverse(-a[i], b[i])
            add_edges(b[i]+n, n-a[i])
            add_edges_inverse(b[i] + n, n-a[i])
        else:
            add_edges(-a[i], n-b[i])
            add_edges_inverse(-a[i], n-b[i])
            add_edges(-b[i], n-a[i])
            add_edges_inverse(-b[i], n-a[i])

    for i in range(n*2):
        if not visited[i]:
            dfs_1(i)

    while len(stack) > 0:
        n = stack.pop()

        if not visited[n]:
            dfs_2(n, counter)
            counter += 1

    for i in range(n):
        if score[i] == score[i+n]:
            print("unsatisfiable")
            return

    print("satisfiable")
    return 
