from functools import reduce

from pandas import DataFrame


class Graph:
    """Implement three graph representation variants for illustration.
    (List of edges, adjacency matrix, adjacency list)
    All representations represent vertices as integers.
    Supports self loops but not parallel edges.
    """

    def __init__(self, vertex_count: int):
        """Initialize list of edges, adjacency matrix and adjacency list."""
        self.vertex_count = vertex_count
        self.edge_list = []
        self.adj_matrix = ([
            [0 for v in range(vertex_count)] for w in range(vertex_count)
        ])
        self.adj_list = [set() for v in range(vertex_count)]

    def __str__(self):
        """Return graph in all representations."""
        return (f'Edge List: {self.edge_list}\n'
                f'Adj Matrix: \n{DataFrame(self.adj_matrix)}\n'
                f'Adj List: {[v for v in self.adj_list]}\n'
                f'**********************************************')

    def add_edge(self, v: int, w: int):
        """Add edge between v and w."""
        # Adds edge to edge list
        (self.edge_list.append((v, w))
            if not (v, w) in self.edge_list
            and not (w, v) in self.edge_list
            else None)

        # Adds edge to adj matrix
        self.adj_matrix[v][w] = self.adj_matrix[w][v] = 1

        # Adds edge to adj list
        if not self.edge_between(v, w):
            self.adj_list[v].add(w)
            self.adj_list[w].add(v)

    def adj(self, v: int) -> list:
        """Return an iterable of vertices adjacent to v (from adj list)."""
        return self._adj_from_adj_list(v)

    def e(self) -> int:
        """Return number of edges."""
        return self._e_from_adj_list()

    def edge_between(self, v: int, w: int) -> bool:
        """Return True if there is an edge between v and w, else False."""
        # Using only adjacency list here to not overcomplicate this code
        return w in self.adj_list[v]

    def v(self) -> int:
        """Return number of vertices."""
        return self.vertex_count

    def _adj_from_edge_list(self, v: int) -> list:
        """Return an iterable of vertices adjacent to v from edge list."""
        return [edge[0] if edge[1] == v else edge[1]
                for edge in self.edge_list
                if edge[0] == v or edge[1] == v]

    def _adj_from_adj_matrix(self, v: int) -> list:
        """Return iterable of vertices adjacent to v from adj matrix."""
        return [index for (index, value) in enumerate(self.adj_matrix[v])
                if value == 1]

    def _adj_from_adj_list(self, v: int) -> list:
        """Return iterable of vertices adjacent to v from adj list."""
        return self.adj_list[v]

    def _e_from_edge_list(self) -> int:
        """Return number of edges from edge list."""
        return len(self.edge_list)

    def _e_from_adj_matrix(self) -> int:
        """Return number of edges from adj matrix."""
        deduplicated_adj_matrix = [
            row[row_index:] for row_index, row in enumerate(self.adj_matrix)
        ]  # using a 'diagonally-split' half of the adj matrix to deduplicate
        return reduce(lambda a, b: a + b.count(1), deduplicated_adj_matrix, 0)

    def _e_from_adj_list(self) -> int:
        """Return number of edges from adj list."""
        number_of_self_loops = 0
        for vertex, edges in enumerate(self.adj_list):
            if vertex in edges:
                number_of_self_loops += 1
        number_of_non_self_loop_edges = sum([
            len(vertex_set) for vertex_set in self.adj_list
        ]) // 2

        return number_of_self_loops + number_of_non_self_loop_edges


if __name__ == '__main__':
    G = Graph(10)
    print(G)
    G.add_edge(0, 9)
    G.add_edge(0, 9)
    print(G)

    assert G.edge_between(0, 9) is True
    assert G.edge_between(0, 8) is False

    edges = [
        (0, 8),
        (0, 7),
        (1, 2),
        (1, 1),
        (2, 6),
        (2, 9),  # duplicate
        (9, 2),  # duplicate
        (3, 5),
        (6, 9),
    ]
    for (v, w) in edges:
        G.add_edge(v, w)

    print(f'Vertex count: {G.v()}')
    print(f'Edge count: {G._e_from_edge_list()} / {G._e_from_adj_matrix()} '
          f'/ {G._e_from_adj_list()}')
    print(G)
    print(f'Edges for vertex 0: {G._adj_from_edge_list(0)} / '
          f'{G._adj_from_adj_matrix(0)} / {G._adj_from_adj_list(0)}')
    print(f'Edges for vertex 9: {G._adj_from_edge_list(9)} / '
          f'{G._adj_from_adj_matrix(9)} / {G._adj_from_adj_list(9)}')
    print(f'Edges for vertex 5: {G._adj_from_edge_list(5)} / '
          f'{G._adj_from_adj_matrix(5)} / {G._adj_from_adj_list(5)}')

    assert G.v() == 10

    assert G._e_from_edge_list() == 9
    assert G._e_from_adj_matrix() == 9
    assert G._e_from_adj_list() == 9

    assert G._adj_from_edge_list(0) == [9, 8, 7]
    assert G._adj_from_adj_matrix(0) == [7, 8, 9]
    assert G._adj_from_adj_list(0) == {7, 8, 9}
    assert G._adj_from_edge_list(9) == [0, 2, 6]
    assert G._adj_from_adj_matrix(9) == [0, 2, 6]
    assert G._adj_from_adj_list(9) == {0, 2, 6}
    assert G._adj_from_edge_list(5) == [3]
    assert G._adj_from_adj_matrix(5) == [3]
    assert G._adj_from_adj_list(5) == {3}
