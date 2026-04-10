import random
from graph import Graph

def generate_dense_graph(n):
    g = Graph(n)

    for i in range(n):
        for j in range(i + 1, n):
            weight = random.randint(1, 100)
            g.add_edge(i, j, weight)

    return g
def generate_sparse_graph(n, k=3):
    g = Graph(n)

    # ensure connectivity first (chain)
    for i in range(n - 1):
        weight = random.randint(1, 100)
        g.add_edge(i, i + 1, weight)

    # add extra random edges
    for i in range(n):
        for _ in range(k):
            j = random.randint(0, n - 1)
            if i != j:
                weight = random.randint(1, 100)
                g.add_edge(i, j, weight)

    return g