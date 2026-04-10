class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = {i: [] for i in range(n)}
        self.edges = []

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.edges.append((u, v, w))