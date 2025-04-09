# Graph Pathfinding with Dijkstra and A* Algorithms

This project demonstrates the implementation of a custom `Graph` class in Python and the application of **Dijkstra's algorithm** and **A\* (A-Star) search** to find the shortest path between two nodes in a large, weighted, and directed graph.

## Features

- Customizable `Graph` class with:
  - Support for directed and undirected graphs
  - Support for weighted and unweighted edges
  - BFS and DFS iterators
  - Vertex position handling (for A\* heuristic)
- File reading support for graph structures and vertex positions
- Implementation of:
  - Dijkstra's algorithm
  - A\* search algorithm (with Euclidean distance as the heuristic)
- Performance statistics (execution time, priority queue operations)

## File Structure

- `main.py`: Entry point for user interaction and comparison of Dijkstra and A\*.
- `graph.py`: Contains the `Graph` class and its methods for manipulating graphs.
- `a3.py`: Implements `dijkstra` and `a_star` search algorithms.
- `a3_examples/`: Directory containing graph and position input files.

## How to Run

1. Make sure your graph and position files are in the correct format. Examples are provided in `a3_examples/Positive only dataset/`.
2. Run the program:

```bash
python main.py
```

3. Enter the start and end vertex names when prompted.

Example:

```
Enter start vertex: 1
Enter end vertex: 1000
```

## Example Output

```
Minimum cost walk 1 to 1000:
    Dijkstra: time: 126.54 ms, cost: 453, path: 1, 5, 9, ..., 1000
    A*: time: 102.31 ms, cost: 453, path: 1, 5, 9, ..., 1000
Comparison: 
        g.cost  pq.push pq.pop
Dijkstra    1432    1001    1000
A*          1023    800     799
```

## Requirements

- Python 3.7+
- No external libraries required

## Notes

- A\* assumes Euclidean distances between nodes based on provided coordinates.
- The graph file must specify whether it's directed/undirected and weighted/unweighted in the first line.

## Author

Project developed for Assignment 3 of a course on Algorithms and Data Structures.