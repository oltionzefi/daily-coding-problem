from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, f):
        self.graph[u].append((v, f))
        print(self.graph)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self):
        v = len(self.graph)
        visited = [False] * v
        for i in range(v):
            if not visited[i]:
                self.dfs_util(i, visited)

    def convert(self, u, v, value):
        return

