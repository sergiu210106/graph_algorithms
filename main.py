from graph import Graph
from a5 import is_eulerian, find_eulerian_circuit

g = Graph(directed=False)
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "A")

print("Is Eulerian?", is_eulerian(g))
print("Eulerian Circuit:", find_eulerian_circuit(g))
