from graph import Graph

def find_shortest_simple_path_backtracking(graph: Graph, start_vertex: str, end_vertex: str):
    if not graph.weighted:
        raise ValueError("Graph must be weighted")

    if start_vertex not in graph.get_vertices() or end_vertex not in graph.get_vertices():
        raise ValueError("Start or end vertex not in graph")

    min_cost = float('inf')
    shortest_path = []

    def backtrack(current_vertex: str, current_path: list, current_cost: float, visited: set):
        nonlocal min_cost, shortest_path

        if current_vertex == end_vertex:
            if current_cost < min_cost:
                min_cost = current_cost
                shortest_path = list(current_path)
            return min_cost, shortest_path

        for edge in graph.neighbours(current_vertex):
            neighbor_vertex, weight = edge

            if neighbor_vertex not in visited:
                current_path.append(neighbor_vertex)
                visited.add(neighbor_vertex)

                backtrack(neighbor_vertex, current_path, current_cost + weight, visited)

                visited.remove(neighbor_vertex)
                current_path.pop()

    backtrack(start_vertex, [start_vertex], 0.0, {start_vertex})

    return min_cost, shortest_path

