#  for assignment 3

from graph import Graph
import heapq

def dijkstra(g : Graph, start_vertex, goal_vertex): # complexity : O((V+E)logE)
    if start_vertex not in g.list_of_neighbours:
        raise ValueError("Start vertex not in graph")
    
    stats = {"cost_calls": 0, "pq_pushes": 0, "pq_pops": 0}
    
    distances = {v : float('inf') for v in g.list_of_neighbours}
    distances[start_vertex] = 0
    
    priority_queue = [(0, start_vertex)] # (distance, vertex)
    
    came_from = {}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        stats["pq_pops"] += 1
        
        if current_distance > distances[current_vertex]:
            continue
        
        if current_vertex == goal_vertex:
            path = []
            while current_vertex in came_from:
                path.append(current_vertex)
                current_vertex = came_from[current_vertex]
            path.append(start_vertex)
            return path[::-1], distances[goal_vertex], stats
        
        for neighbour in g.list_of_neighbours[current_vertex]:
            nb, weight = (neighbour[0], neighbour[1]) if g.weighted else (neighbour, 1)
            stats["cost_calls"] += 1
            
            distance = current_distance + weight
            
            if distance < distances[nb]:
                came_from[nb] = current_vertex
                distances[nb] = distance
                heapq.heappush(priority_queue, (distance, nb))
                stats["pq_pushes"] += 1
    
    return None, float('inf'), stats # If goal is unreachable



def a_star(g: Graph, start_vertex, goal_vertex): # O(ElogV)
    if start_vertex not in g.list_of_neighbours or goal_vertex not in g.list_of_neighbours:
        raise ValueError("Start or goal vertex not in graph")

    stats = {"cost_calls": 0, "pq_pushes": 0, "pq_pops": 0}

    open_set = [(0, start_vertex)]
    came_from = {}

    g_score = {v: float('inf') for v in g.list_of_neighbours}
    f_score = {v: float('inf') for v in g.list_of_neighbours}

    g_score[start_vertex] = 0
    f_score[start_vertex] = g.euclidean_distance(start_vertex, goal_vertex)

    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        stats["pq_pops"] += 1

        if current == goal_vertex:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start_vertex)
            return path[::-1], g_score[goal_vertex], stats

        visited.add(current)

        for neighbor in g.list_of_neighbours[current]:
            nb, weight = (neighbor[0], neighbor[1]) if g.weighted else (neighbor, 1)
            stats["cost_calls"] += 1

            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[nb]:
                came_from[nb] = current
                g_score[nb] = tentative_g_score
                f_score[nb] = tentative_g_score + g.euclidean_distance(nb, goal_vertex)
                if nb not in visited:
                    heapq.heappush(open_set, (f_score[nb], nb))
                    stats["pq_pushes"] += 1

    return None, float('inf'), stats  # If goal is unreachable
