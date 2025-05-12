import unittest
from graph import Graph
from a4 import topological_sort, longest_path_dag, bonus_problem

class TestGraphAlgorithms(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(directed=True, weighted=True)
        edges = [
            ('A', 'B', 3),
            ('A', 'C', 6),
            ('B', 'C', 4),
            ('B', 'D', 4),
            ('C', 'D', 8),
            ('D', 'E', 2),
            ('E', 'F', 6)
        ]

        vertices = set()
        for u, v, _ in edges:
            vertices.add(u)
            vertices.add(v)

        for vertex in vertices:
            self.graph.add_vertex(vertex)

        for u, v, w in edges:
            self.graph.add_edge(u, v, w)
    

    def test_topological_sort(self):
        topo_order = topological_sort(self.graph)
        self.assertIsNotNone(topo_order)
        # Ensure no cycles (length check)
        self.assertEqual(len(topo_order), self.graph.get_v())
        # Check basic topological property: for each edge u -> v, u comes before v
        position = {v: i for i, v in enumerate(topo_order)}
        for u in self.graph.get_vertices():
            for v, _ in self.graph.neighbours(u):
                self.assertLess(position[u], position[v])

    def test_longest_path_dag(self):
        graph = Graph(directed=True, weighted=True)

        for v in ['A', 'B', 'C', 'D', 'E', 'F']:
            graph.add_vertex(v)

        graph.add_edge('A', 'B', 5)
        graph.add_edge('B', 'C', 7)
        graph.add_edge('B', 'D', 8)
        graph.add_edge('C', 'D', 2)
        graph.add_edge('D', 'E', 6)
        graph.add_edge('E', 'F', 4)

        path, cost = longest_path_dag(graph, 'A', 'F')

        expected_cost = 24  # 5 + 7 + 2 + 6 + 4 = 24

        self.assertEqual(cost, expected_cost)

        # Now verify the path itself:
        self.assertEqual(path[0], 'A')
        self.assertEqual(path[-1], 'F')
    
        # Check that each consecutive (u,v) is an edge in the graph
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            neighbors = [neighbor for neighbor, _ in graph.neighbours(u)]
            self.assertIn(v, neighbors)
 
    def test_bonus_problem(self):
        preorder = ['A', 'B', 'D', 'E', 'C', 'F']
        inorder = ['D', 'B', 'E', 'A', 'C', 'F']
        postorder = ['D', 'E', 'B', 'F', 'C', 'A']  # not used 

        graph_from_tree = bonus_problem(preorder, inorder, postorder)
        print(graph_from_tree)
        # Expected structure:
        #         A
        #        / \
        #      B     C
        #     / \     \
        #    D   E     F

        # Check edges
        expected_edges = [
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'D'),
            ('B', 'E'),
            ('C', 'F')
        ]
        for u, v in expected_edges:
            self.assertIn(v, graph_from_tree.neighbours(u))

if __name__ == "__main__":
    unittest.main()

