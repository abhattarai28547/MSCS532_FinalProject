import unittest
from scaling.dataset_loader import generate_large_dataset
from data_structures.graph import Graph

class TestGraph(unittest.TestCase):
    def test_a_star(self):
        graph = Graph()
        graph.add_edge((0, 0), (1, 1), 5)
        graph.add_edge((1, 1), (2, 2), 3)
        result = graph.a_star((0, 0), (2, 2))
        self.assertEqual(result, [(0, 0), (1, 1), (2, 2)])
    
    def test_large_dataset(self):
        graph = Graph()
        large_dataset = generate_large_dataset(1000, 10)
        for u, edges in large_dataset.items():
            for v, cost in edges:
                graph.add_edge(u, v, cost)
        result = graph.a_star(0, 999)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
