from graph import Graph

def is_eulerian(graph: Graph) -> bool:
    if graph.directed:
        in_degrees = {v: 0 for v in graph.list_of_neighbours}
        out_degrees = {v: len(graph.list_of_neighbours[v]) for v in graph.list_of_neighbours}

        for u in graph.list_of_neighbours:
            for neighbor in graph.list_of_neighbours[u]:
                v = neighbor[0] if graph.weighted else neighbor
                in_degrees[v] += 1

        return all(in_degrees[v] == out_degrees[v] for v in graph.list_of_neighbours)
    else:
        for v in graph.list_of_neighbours:
            if len(graph.list_of_neighbours[v]) % 2 != 0:
                return False
        return True


def find_eulerian_circuit(graph: Graph) -> list:
    if not is_eulerian(graph):
        raise ValueError("Graph is not Eulerian")

    graph_copy = {u: list(graph.list_of_neighbours[u])[:] for u in graph.list_of_neighbours}
    stack = []
    circuit = []

    current = next((v for v in graph_copy if graph_copy[v]), None)
    if current is None:
        return []

    stack.append(current)

    while stack:
        if graph_copy[current]:
            stack.append(current)
            if graph.weighted:
                next_vertex = graph_copy[current].pop()[0]
            else:
                next_vertex = graph_copy[current].pop()
            if not graph.directed:
                if graph.weighted:
                    reverse_edge = (current, graph.get_weight(next_vertex, current))
                    graph_copy[next_vertex].remove(reverse_edge)
                else:
                    graph_copy[next_vertex].remove(current)
            current = next_vertex
        else:
            circuit.append(current)
            current = stack.pop()

    return circuit[::-1]
