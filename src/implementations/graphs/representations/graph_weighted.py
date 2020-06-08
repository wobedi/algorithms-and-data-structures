from functools import reduce

from src.implementations.graphs.representations.edges import DirectedEdge


class DigraphWeighted:
    """Implements a digraph with weighted edges, represented
    as an adjacency list and vertices as intergers.
    Supports parallel edges and self loops.
    """
    def __init__(self, vertex_count: int):
        self.vertex_count = vertex_count
        self.adj_list = [set() for v in range(vertex_count)]

    def __str__(self):
        edges_flat = [e for s in self.adj_list for e in s]
        formatted = [f'{e.from_()}->{e.to()}: {e.weight}' for e in edges_flat]
        return (f'Adj List: {formatted}\n'
                f'**********************************************')

    def add_edge(self, e: DirectedEdge):
        """Adds edge from v to w"""
        self.adj_list[e.from_()].add(e)

    def adj(self, v: int) -> list:
        """Returns vertices adjacent to v"""
        return set([edge for edge in self.adj_list[v]])

    def edge_between(self, v: int, w: int) -> bool:
        """Returns True if there is an edge from v to w, else False"""
        return reduce(lambda a, b: b.to() == w, self.adj_list[v], False)

    def edges(self) -> list:
        """Returns iterable of edges"""
        return [e for s in self.adj_list for e in s]

    def e(self) -> int:
        """Returns number of edges"""
        return reduce(lambda a, b: a + len(b), self.adj_list, 0)

    def v(self) -> int:
        """Returns number of vertices"""
        return len(self.adj_list)


if __name__ == '__main__':
    DGW = DigraphWeighted(10)
    print(DGW)
    DGW.add_edge(DirectedEdge(0, 9, 1))
    print(DGW)

    assert DGW.edge_between(0, 9) is True
    assert DGW.edge_between(0, 8) is False

    edges = [
        DirectedEdge(0, 8, 1),
        DirectedEdge(0, 7, 2),
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

    print(f'Vertex count: {DGW.v()}')
    print(f'Edge count: {DGW.e()}')
    print(DGW)

    assert DGW.v() == 10
    assert DGW.e() == 12
