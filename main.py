from graph import read_from_file
from a6 import *

g = read_from_file("A5_eulerian.txt")
try:
    cost, path = bellman_ford(g, "A", "D")
    print(f"Minimum cost from A to D is {cost}")
    print(f"Path: {' -> '.join(path)}")
except ValueError as ve:
    print(ve)
