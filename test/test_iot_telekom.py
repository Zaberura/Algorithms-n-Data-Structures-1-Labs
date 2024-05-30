from src.iot_telekom import Graph
import unittest


class TestGraph(unittest.TestCase):
    def test_add_well(self):
        graph = Graph()
        graph.add_well(1, 2, 200)
        self.assertEqual(graph.graph, {1: {2: 200}, 2: {1: 200}})

    def test_find_min_path(self):
        graph = Graph()
        graph.add_well(1, 2, 200)
        graph.add_well(2, 3, 300)
        graph.add_well(1, 3, 400)
        mst = graph.find_min_path()
        self.assertEqual(mst, [(1, 2, 200), (2, 3, 300)])

    def test_find_min_path_empty_graph(self):
        graph = Graph()
        mst = graph.find_min_path()
        self.assertEqual(mst, [])

    def test_find_min_path_single_well(self):
        graph = Graph()
        graph.add_well(1, 1, 0)
        mst = graph.find_min_path()
        self.assertEqual(mst, [])

    def test_find_min_path_duplicate_edges(self):
        graph = Graph()
        graph.add_well(1, 2, 300)
        graph.add_well(1, 2, 200)
        graph.add_well(2, 3, 400)
        mst = graph.find_min_path()
        self.assertEqual(mst, [(1, 2, 200), (2, 3, 400)])


if __name__ == '__main__':
    unittest.main()
