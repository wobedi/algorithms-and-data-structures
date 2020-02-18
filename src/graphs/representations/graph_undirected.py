from functools import reduce

from pandas import DataFrame

from src.graphs.operations.graph_connectivity import GraphConnectivity
from src.graphs.operations.graph_search import GraphSearch


class Graph:
    def __init__(self, vertex_count):
        """Implements three graph representation variants for illustration
        purposes: list of edges, adjaceny matrix, adjacency list.
        Supports self loops but not parallel edges.
        """
        self.vertex_count = vertex_count
        self.edge_list = []
        self.adj_matrix = ([
            [0 for v in range(vertex_count)] for w in range(vertex_count)
        ])
        self.adj_list = [set() for v in range(vertex_count)]

    def __str__(self):
        return (f'Edge List: {self.edge_list}\n'
                f'Adj Matrix: \n{DataFrame(self.adj_matrix)}\n'
                f'Adj List: {[v for v in self.adj_list]}\n'
                f'**********************************************')

    def add_edge(self, v, w):
        """Adds edge between v and w"""
        # add edge to edge list
        (self.edge_list.append((v, w))
            if not (v, w) in self.edge_list
            and not (w, v) in self.edge_list
            else None)

        # add edge to adj matrix
        self.adj_matrix[v][w] = self.adj_matrix[w][v] = 1

        # add edge to adj list
        if not self.edge_between(v, w):
            self.adj_list[v].add(w)
            self.adj_list[w].add(v)

    def adj(self, v):
        """Returns an iterable of vertices adjacent to v (from adj list)"""
        return self._adj_from_adj_list(v)

    def e(self):
        """Returns number of edges"""
        return self._e_from_adj_list()

    def edge_between(self, v, w):
        """Returns True if there is an edge between v and w, else False"""
        # using only adjacency list here to not overcomplicate this code
        return w in self.adj_list[v]

    def v(self):
        """Returns number of vertices"""
        return self.vertex_count

    def _adj_from_edge_list(self, v):
        """Returns an iterable of vertices adjacent to v from edge list"""
        return [edge[0] if edge[1] == v else edge[1]
                for edge in self.edge_list
                if edge[0] == v or edge[1] == v]

    def _adj_from_adj_matrix(self, v):
        """Returns iterable of vertices adjacent to v from adj matrix"""
        return [index for (index, value) in enumerate(self.adj_matrix[v])
                if value == 1]

    def _adj_from_adj_list(self, v):
        """Returns iterable of vertices adjacent to v from adj list"""
        return self.adj_list[v]

    def _e_from_edge_list(self):
        """Returns number of edges from edge list"""
        return len(self.edge_list)

    def _e_from_adj_matrix(self):
        """Returns number of edges from adj matrix"""
        # divide by 2 because each edge is represented twice: [v][w] and [w][v]
        return reduce(lambda a, b: a + b.count(1), self.adj_matrix, 0) // 2

    def _e_from_adj_list(self):
        """Returns number of edges from adj list"""
        # divide by 2 because each edge is represented twice: [v][w] and [w][v]
        return sum([len(vertex_set) for vertex_set in self.adj_list]) // 2


if __name__ == "__main__":
    G = Graph(10)
    print(G)
    G.add_edge(0, 9)
    G.add_edge(0, 9)
    print(G)
    G.add_edge(0, 8)
    G.add_edge(0, 7)
    G.add_edge(1, 2)
    G.add_edge(1, 1)
    G.add_edge(2, 6)
    G.add_edge(2, 9)
    G.add_edge(9, 2)
    G.add_edge(3, 5)
    G.add_edge(6, 9)
    print(f'Vertex count: {G.v()}')
    print(f'Edge count: {G._e_from_edge_list()} / {G._e_from_adj_matrix()}'
          f'/ {G._e_from_adj_list()}')
    print(G)
    print('Edges for vertex 0:')
    print(G._adj_from_edge_list(0))
    print(G._adj_from_adj_matrix(0))
    print(G._adj_from_adj_list(0))
    print('Edges for vertex 9:')
    print(G._adj_from_edge_list(9))
    print(G._adj_from_adj_matrix(9))
    print(G._adj_from_adj_list(9))
    print('Edges for vertex 5:')
    print(G._adj_from_edge_list(5))
    print(G._adj_from_adj_matrix(5))
    print(G._adj_from_adj_list(5))
    GS = GraphSearch(G, 0)
    print(GS.source_has_path_to(6))
    print('Path from source to 6:', GS.source_path_to(6))
    print(GS.source_has_path_to(3))
    print('Path from source to 3:', GS.source_path_to(3))
    print('Arbitrary cycle (if any):', GS.cycle)
    CC = GraphConnectivity(G)
    print(CC)
    assert CC.connected(0, 1) is True
    assert CC.connected(0, 3) is False
    assert CC.connected(3, 4) is False
    assert CC.id(0) == 1
    assert CC.id(1) == 1
    assert CC.id(4) == 3
    assert CC.count() == 3

# Edge List: []
# Adj Matrix:
#        0    1    2    3    4    5    6    7    8    9
# 0    0    0    0    0    0    0    0    0    0    0
# 1    0    0    0    0    0    0    0    0    0    0
# 2    0    0    0    0    0    0    0    0    0    0
# 3    0    0    0    0    0    0    0    0    0    0
# 4    0    0    0    0    0    0    0    0    0    0
# 5    0    0    0    0    0    0    0    0    0    0
# 6    0    0    0    0    0    0    0    0    0    0
# 7    0    0    0    0    0    0    0    0    0    0
# 8    0    0    0    0    0    0    0    0    0    0
# 9    0    0    0    0    0    0    0    0    0    0
# Adj List: [set(), set(), set(), set(), set(), set(), set(),set(),set(),set()]
# **********************************************
# Edge List: [(0, 9)]
# Adj Matrix:
#        0    1    2    3    4    5    6    7    8    9
# 0    0    0    0    0    0    0    0    0    0    1
# 1    0    0    0    0    0    0    0    0    0    0
# 2    0    0    0    0    0    0    0    0    0    0
# 3    0    0    0    0    0    0    0    0    0    0
# 4    0    0    0    0    0    0    0    0    0    0
# 5    0    0    0    0    0    0    0    0    0    0
# 6    0    0    0    0    0    0    0    0    0    0
# 7    0    0    0    0    0    0    0    0    0    0
# 8    0    0    0    0    0    0    0    0    0    0
# 9    1    0    0    0    0    0    0    0    0    0
# Adj List: [{9}, set(), set(), set(), set(), set(), set(), set(), set(), {0}]
# **********************************************
# Vertex count: 10
# Edge count: 8 / 8 / 8
# Edge List: [(0, 9), (0, 8), (0, 7), (1, 2), (2, 6), (2, 9), (3, 5), (6, 9)]
# Adj Matrix:
#        0    1    2    3    4    5    6    7    8    9
# 0    0    0    0    0    0    0    0    1    1    1
# 1    0    0    1    0    0    0    0    0    0    0
# 2    0    1    0    0    0    0    1    0    0    1
# 3    0    0    0    0    0    1    0    0    0    0
# 4    0    0    0    0    0    0    0    0    0    0
# 5    0    0    0    1    0    0    0    0    0    0
# 6    0    0    1    0    0    0    0    0    0    1
# 7    1    0    0    0    0    0    0    0    0    0
# 8    1    0    0    0    0    0    0    0    0    0
# 9    1    0    1    0    0    0    1    0    0    0
# Adj List: [{8, 9, 7}, {2}, {1, 6, 9}, {5},set(),{3},{9, 2},{0},{0},{0, 2, 6}]
# **********************************************
# Edges for vertex 0:
# [9, 8, 7]
# [7, 8, 9]
# {8, 9, 7}
# Edges for vertex 9:
# [0, 2, 6]
# [0, 2, 6]
# {0, 2, 6}
# Edges for vertex 5:
# [3]
# [3]
# {3}
# True
# Path from source to 6: [0, 9, 2, 6]
# False
# Path from source to 3: []
# Arbitrary cycle (if any): [0, 9, 6, 2, 9, 0]
# <__main__.GraphConnectivity object at 0x7f87af109110>
