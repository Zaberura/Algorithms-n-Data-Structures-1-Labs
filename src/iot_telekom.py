import heapq

class Graph:
    def __init__(self):
        self.graph = {}
        self.priority_queue = []

    def add_well(self, well_one, well_two, distance):
        """
        Adds an edge between two wells with a given distance.

        Args:
            well_one (int): The first well.
            well_two (int): The second well.
            distance (float): The distance between the two wells.
        """

        if well_one not in self.graph:
            self.graph[well_one] = {}
        if well_two not in self.graph:
            self.graph[well_two] = {}
        self.graph[well_one][well_two] = distance
        self.graph[well_two][well_one] = distance

    def find_min_path(self):
        """
        Finds the minimum spanning tree of the graph using Prim's algorithm.

        Returns:
            list: A list of tuples representing the edges in the minimum spanning tree.
                  Each tuple contains the two vertices of the edge and the weight of the edge.
        """

        if not self.graph:
            return []
        parent = {}
        distance = {}
        min_path_set = set()

        start_point = next(iter(self.graph.keys()))
        distance[start_point] = 0
        parent[start_point] = None

        for well in self.graph:
            if well != start_point:
                distance[well] = float('inf')
                parent[well] = None

        heapq.heappush(self.priority_queue, (0, start_point))

        while self.priority_queue:
            current_distance, current_well = heapq.heappop(self.priority_queue)
            if current_well in min_path_set:
                continue
            min_path_set.add(current_well)
            for connected_well, edge_weight in self.graph[current_well].items():
                if connected_well not in min_path_set and edge_weight < distance[connected_well]:
                    distance[connected_well] = edge_weight
                    parent[connected_well] = current_well
                    heapq.heappush(self.priority_queue, (edge_weight, connected_well))

        mst = []
        for connected_well in parent:
            if parent[connected_well] is not None:
                mst.append((parent[connected_well], connected_well, self.graph[connected_well][parent[connected_well]]))
        return mst


def load_graph_from_csv(file_path):
    """
    Loads a graph from a CSV file where each row represents an edge between two wells.

    Args:
        file_path (str): The path to the CSV file containing the graph data.

    Returns:
        Graph: An instance of the Graph class representing the loaded graph.
    """

    graph = Graph()
    with open(file_path, 'r') as file:
        for line in file:
            u, v, w = map(int, line.strip().replace('K', '').split(','))
            graph.add_well(u, v, w)
    return graph



# # Example usage:
# file_path = '../src/communication_wells.csv'
# graph = load_graph_from_csv(file_path)
# mst = graph.find_min_path()
#
# print("Edges in the Minimum Spanning Tree:")
# for u, v, weight in mst:
#     print(f"{u} -- {v} == {weight}")
