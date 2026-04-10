from test_graphs import create_test_graph
from prim import prim
from kruskal import kruskal
from generator import generate_sparse_graph, generate_dense_graph

# ---------- PART 1: Test Graph ----------
g, expected = create_test_graph()

p = prim(g)
k = kruskal(g)

print("Test Case 1")
print("Prim:", p)
print("Kruskal:", k)
print("Expected:", expected)

if p == expected and k == expected:
    print("Tests Passed\n")
else:
    print("Tests Failed\n")

# ---------- PART 2: Sparse Graph ----------
g_sparse = generate_sparse_graph(10)

p_sparse = prim(g_sparse)
k_sparse = kruskal(g_sparse)

print("Sparse Graph")
print("Prim:", p_sparse)
print("Kruskal:", k_sparse)

# ---------- PART 3: Dense Graph ----------
g_dense = generate_dense_graph(10)

p_dense = prim(g_dense)
k_dense = kruskal(g_dense)

print("\nDense Graph")
print("Prim:", p_dense)
print("Kruskal:", k_dense)