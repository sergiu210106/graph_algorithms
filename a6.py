from graph import Graph

# problem 9 - assignment 6

# Given a weighted undirected graph with negative cycles, find the minimum cost path
# between 2 given vertices.


def bellman_ford(graph: Graph, start_vertex: str, end_vertex: str):
    if not graph.weighted:
        raise ValueError("Graph must be weighted")

    distance = {v: float('inf') for v in graph.get_vertices()}
    distance[start_vertex] = 0

    predecessor = {v: None for v in graph.get_vertices()}

    V = graph.get_v()

    for _ in range(V - 1):
        for u in graph.get_vertices():
            for edge in graph.neighbours(u):
                v, w = edge  # because graph is weighted
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

    # Check for negative-weight cycles
    for u in graph.get_vertices():
        for edge in graph.neighbours(u):
            v, w = edge
            if distance[u] + w < distance[v]:
                # Negative cycle detected
                raise ValueError("Negative cycle detected; shortest path is undefined")

    # Reconstruct the path
    path = []
    current = end_vertex
    while current is not None:
        path.append(current)
        current = predecessor[current]

    path.reverse()

    return distance[end_vertex], path
