class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX
            return True
        return False


def kruskal(graph):
    uf = UnionFind(graph.n)
    edges = sorted(graph.edges, key=lambda x: x[2])
    total_weight = 0

    for u, v, w in edges:
        if uf.union(u, v):
            total_weight += w

    return total_weight