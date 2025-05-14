from graph import Graph, read_from_file
from a5 import *

g = read_from_file("A5_bipartite.txt")

print(g)

print(maximum_matching_bipartite(g))

