from collections import deque
from graph import Graph
def maximum_matching_bipartite(graph: Graph):
    if graph.directed:
        raise ValueError("Graph must be undirected")

    # Step 1: Partition the graph using BFS (coloring)
    color = {}
    U, V = set(), set()

    for vertex in graph.get_vertices():
        if vertex not in color:
            queue = deque([vertex])
            color[vertex] = 0
            U.add(vertex)
            while queue:
                u = queue.popleft()
                for v in graph.neighbours(u):
                    if v not in color:
                        color[v] = 1 - color[u]
                        if color[v] == 0:
                            U.add(v)
                        else:
                            V.add(v)
                        queue.append(v)
                    elif color[v] == color[u]:
                        raise ValueError("Graph is not bipartite")

    pair_U = {u: None for u in U}
    pair_V = {v: None for v in V}
    dist = {}

    def bfs():
        queue = deque()
        for u in U:
            if pair_U[u] is None:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[None] = float('inf')

        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for v in graph.neighbours(u):
                    if pair_V[v] is None:
                        if dist[None] == float('inf'):
                            dist[None] = dist[u] + 1
                    elif dist[pair_V[v]] == float('inf'):
                        dist[pair_V[v]] = dist[u] + 1
                        queue.append(pair_V[v])
        return dist[None] != float('inf')

    def dfs(u):
        if u is not None:
            for v in graph.neighbours(u):
                if pair_V[v] is None or (dist[pair_V[v]] == dist[u] + 1 and dfs(pair_V[v])):
                    pair_U[u] = v
                    pair_V[v] = u
                    return True
            dist[u] = float('inf')
            return False
        return True

    matching = 0
    while bfs():
        for u in U:
            if pair_U[u] is None:
                if dfs(u):
                    matching += 1

    matched_pairs = [(u, pair_U[u]) for u in U if pair_U[u] is not None]
    return matched_pairs
