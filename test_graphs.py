from graph import Graph

def create_test_graph():
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(1, 2, 3)
    g.add_edge(0, 2, 4)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 4, 5)
    return g, 11