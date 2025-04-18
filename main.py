from graph import Graph
from a3 import *
import time

g = Graph()


g = Graph.read_from_file("a3_examples/Positive only dataset/A3_v100000_e400000_positives_8.txt")
g.read_positions_from_file("a3_examples/Positive only dataset/A3_v100000_e400000_positives_8_vertex_positions.txt")

print(g.directed)

start_vertex = input("Enter start vertex: ")
end_vertex = input("Enter end vertex: ")

start_time = time.time()
path_d, cost_d, stats_d = dijkstra(g, start_vertex, end_vertex)
dijkstra_time = (time.time() - start_time) * 1000

start_time = time.time()
path_a, cost_a, stats_a = a_star(g, start_vertex, end_vertex)
a_star_time = (time.time() - start_time)

print(f"Minimum cost walk {start_vertex} to {end_vertex}:")
print(f"\tDijkstra: time: {dijkstra_time}, cost: {cost_d}, path: {", ".join(map(str,path_d))}")
print(f"\tA*: time: {a_star_time}, cost: {cost_a}, path: {", ".join(map(str,path_a))}")
print("Comparison: ")
print("\t\tg.cost\tpq.push\tpq.pop")
print(f"Dijkstra\t{stats_d["cost_calls"]}\t{stats_d["pq_pushes"]}\t{stats_d["pq_pops"]}")
print()
print(f"A*\t\t{stats_a["cost_calls"]}\t{stats_a["pq_pushes"]}\t{stats_a["pq_pops"]}")
