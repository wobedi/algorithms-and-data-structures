import heapq
from math import inf

from src.implementations.graphs.representations.edges import DirectedEdge
from src.implementations.graphs.representations.graph_weighted import \
    DigraphWeighted


class GraphShortestPath:
    """Preprocesses a weighted digraph to get the shortest path
    from a source vertex to any other vertex in constant time
    """
    def __init__(self, graph, source: int):
        self.graph = graph
        self.source = source
        self.parent = [None for v in range(graph.v())]
        self.dist_to = [inf for v in range(graph.v())]
        self.dist_to[source] = 0
        self.heap = []
        self._dijkstras_shortest_path()

    def source_distance_to(self, v: int) -> int:
        """Returns the distance (total weight) from source to v"""
        return self.dist_to[v]

    def source_shortest_path_to(self, v) -> list:
        """Returns an iterable of the path from source to v"""
        path = [v]
        parent = self.parent[v]
        while parent is not None:
            path.append(parent)
            parent = self.parent[parent]
        return list(reversed(path))

    def _relax(self, e):
        """Relaxes the edge from v to w if possible"""
        v, w = e.from_(), e.to()
        # Could improve performance by skipping already-dealt-with vertices
        if self.dist_to[w] > self.dist_to[v] + e.weight:
            self.parent[w] = v
            self.dist_to[w] = self.dist_to[v] + e.weight
            # Could significantly improve performance by
            # adding decrease-key here
            heapq.heappush(self.heap, (self.dist_to[w], w))

    def _dijkstras_shortest_path(self):
        """Implements https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"""
        heapq.heappush(self.heap, (0, self.source))
        while self.heap:
            _, v = heapq.heappop(self.heap)
            for edge in self.graph.adj(v):
                self._relax(edge)


if __name__ == '__main__':
    DGW = DigraphWeighted(10)
    edges = [
        DirectedEdge(0, 9, 1),
        DirectedEdge(0, 8, 1),
        DirectedEdge(6, 7, 2),
        DirectedEdge(1, 2, 3),
        DirectedEdge(1, 1, 4),
        DirectedEdge(2, 6, 5),
        DirectedEdge(2, 9, 3),  # duplicate
        DirectedEdge(9, 2, 3),  # duplicate
        DirectedEdge(3, 5, 2),
        DirectedEdge(6, 9, 1),
        DirectedEdge(7, 8, 0),
        DirectedEdge(8, 0, 1),
    ]
    for d in edges:
        DGW.add_edge(d)
    print(DGW)

    SP = GraphShortestPath(DGW, 1)

    src_to_two_dist = SP.source_distance_to(2)
    src_to_two_path = SP.source_shortest_path_to(2)
    src_to_zero_dist = SP.source_distance_to(0)
    src_to_zero_path = SP.source_shortest_path_to(0)
    src_to_six_dist = SP.source_distance_to(6)
    src_to_six_path = SP.source_shortest_path_to(6)
    src_to_seven_dist = SP.source_distance_to(7)
    src_to_seven_path = SP.source_shortest_path_to(7)
    src_to_four_dist = SP.source_distance_to(4)
    src_to_four_path = SP.source_shortest_path_to(4)

    print(f'1 to 2: {src_to_two_dist} '
          f'via {src_to_two_path} ')
    print(f'1 to 0: {src_to_zero_dist} '
          f'via {src_to_zero_path}')
    print(f'1 to 6: {src_to_six_dist} '
          f'via {src_to_six_path}')
    print(f'1 to 7: {src_to_seven_dist} '
          f'via {src_to_seven_path}')
    print(f'1 to 4: {src_to_four_dist} '
          f'via {src_to_four_path}')

    assert src_to_two_dist == 3
    assert src_to_two_path == [1, 2]
    assert src_to_zero_dist == 11
    assert src_to_zero_path == [1, 2, 6, 7, 8, 0]
    assert src_to_six_dist == 8
    assert src_to_six_path == [1, 2, 6]
    assert src_to_seven_dist == 10
    assert src_to_seven_path == [1, 2, 6, 7]
    assert src_to_four_dist == inf
    assert src_to_four_path == [4]
