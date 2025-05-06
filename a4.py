from graph import Graph
from collections import deque

def topological_sort(graph : Graph):
    in_degree = {v: 0 for v in graph.get_vertices()}

    for u in graph.get_vertices():
        for v in graph.neighbours(u):
            v = v[0] if graph.weighted else v
            in_degree[v] += 1

    queue = deque([v for v in graph.get_vertices() if in_degree[v] == 0])
    top_order = []
    
    while queue:
        u = queue.popleft()
        top_order.append(u)

        for v in graph.neighbours(u):
            v = v[0] if graph.weighted else v
            in_degree[v] -= 1

            if in_degree[v] == 0:
                queue.append(v)


    if len(top_order) != graph.get_v():
        return None # Cycle detected

    return top_order


def longest_path_dag(graph : Graph, start_vertex, end_vertex):
    if not graph.directed or not graph.weighted:
        raise ValueError("Graph must be directed and weighted for the longest path in DAG")

    top_order = topological_sort(graph)
    if top_order is None:
        print("The graph is not a DAG")
        return None

    print("Topological order: ", top_order)

    dist = {v:float('-inf') for v in graph.get_vertices()}
    prev = {v:None for v in graph.get_vertices()}
    dist[start_vertex] = 0

    for u in top_order:
        if dist[u] != float('-inf'):
            for v, w in graph.neighbours(u):
                if dist[u] + w > dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u

    # Reconstruct path
    path = []
    current = end_vertex

    while current is not None:
        path.append(current)
        current = prev[current]
    
    path.reverse()

    if dist[end_vertex] == float('-inf'):
        print("No path from", start_vertex, "to", end_vertex)
        return None

    print("Longest path cost:", dist[end_vertex])
    print("Longest path:", " -> ".join(path))
    return path, dist[end_vertex]



# bonus

def build_tree(inorder, preorder):
    index_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = [0] # list so we can modify it in the nested function

    def helper(l, r):
        if l > r:
            return None

        root = preorder[pre_idx[0]]
        index = index_map[root]
        pre_idx[0]+=1

        left = helper(l, index - 1)
        right = helper(index + 1, r)

        return (root, left, right)

    return helper(0, len(inorder) - 1)


def tree_to_graph(tree):
    g = Graph(directed = True, weighted = False)

    def dfs(node):
        if not node:
            return

        root, l, r = node
        if root not in g.get_vertices():
            g.add_vertex(root)

        if l:
            child = l[0] if isinstance(l, tuple) else l

            if child not in g.get_vertices():
                g.add_vertex(child)
            g.add_edge(root, child)

        if r:
            child = r[0] if isinstance(r, tuple) else r

            if child not in g.get_vertices():
                g.add_vertex(child)

            g.add_edge(root, child)

        if isinstance(l, tuple):
            dfs(l)

        if isinstance(r, tuple):
            dfs(r)

    dfs(tree)
    return g

def bonus_problem(preorder, inorder, postorder):
    return tree_to_graph(build_tree(inorder, preorder))
