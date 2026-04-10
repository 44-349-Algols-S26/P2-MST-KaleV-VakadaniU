import heapq

def prim(graph):
    visited = set()
    min_heap = [(0, 0)]
    total_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_weight += weight

        for neighbor, w in graph.adj[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor))

    return total_weight