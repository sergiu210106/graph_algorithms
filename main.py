from graph import read_from_file
from a6 import find_shortest_simple_path_backtracking # Import the new function

# Test case 1: Graph with negative edges, potentially negative cycles
# (but we are looking for simple paths)
g = read_from_file("read.txt")
try:
    cost, path = find_shortest_simple_path_backtracking(g, "4", "2")
    if cost == float('inf'):
        print(f"No simple path found from 4 to 2.")
    else:
        print(f"Minimum simple path cost from 4 to 2 is {cost}")
        print(f"Simple Path: {' -> '.join(path)}")
except ValueError as ve:
    print(ve)
print("-" * 30)

# Test case 2: Graph without negative cycles (should work fine)
g2 = read_from_file("no_negative_cycle.txt")
try:
    cost, path = find_shortest_simple_path_backtracking(g2, "A", "D")
    if cost == float('inf'):
        print(f"No simple path found from A to D.")
    else:
        print(f"Minimum simple path cost from A to D is {cost}")
        print(f"Simple Path: {' -> '.join(path)}")
except ValueError as ve:
    print(ve)
print("-" * 30)
