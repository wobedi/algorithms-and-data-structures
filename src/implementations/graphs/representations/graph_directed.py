from functools import reduce


class Digraph:
    def __init__(self, vertex_count: int):
        """Implements a digraph, represented
        as an adjacency list and vertices as intergers.
        that supports self loops but not parallel edges
        """
        self.vertex_count = vertex_count
        self.adj_list = [set() for v in range(vertex_count)]
        self.adj_list_reversed = [set() for v in range(vertex_count)]

    def __str__(self):
        return (f'Adj List: {[list(v) for v in self.adj_list]}\n'
                f'Reversed: {[list(v) for v in self.adj_list_reversed]}\n'
                f'**********************************************')

    def add_edge(self, v: int, w: int):
        """Adds a directional edge from v to w"""
        self.adj_list[v].add(w)
        self.adj_list_reversed[w].add(v)

    def adj(self, v: int) -> list:
        """Returns a list of vertices adjacent to v"""
        return list(self.adj_list[v])

    def adj_reversed(self, v: int) -> list:
        """Returns a list of vertices adjacent to v in reversed digraph"""
        return list(self.adj_list_reversed[v])

    def e(self) -> int:
        """Returns number of edges"""
        return reduce(lambda a, b: a + len(b), self.adj_list, 0)

    def edge_between(self, v: int, w: int) -> bool:
        """Returns True if there is an edge from v to w, else False"""
        return w in self.adj_list[v]

    def edge_between_reversed(self, v: int, w: int) -> bool:
        """Returns True if there is an edge from v to w in reversed digraph,
        else False
        """
        return w in self.adj_list_reversed[v]

    def v(self) -> int:
        """Returns number of vertices"""
        return self.vertex_count


if __name__ == '__main__':
    DG = Digraph(10)
    print(DG)
    DG.add_edge(0, 9)
    DG.add_edge(0, 9)
    print(DG)

    assert DG.edge_between(0, 9) is True
    assert DG.edge_between(0, 8) is False

    edges = [
        (0, 8),
        (0, 7),
        (1, 2),
        (1, 1),
        (2, 6),
        (2, 9),
        (9, 2),
        (3, 5),
        (6, 9),
        (7, 8),
        (8, 0),
        (0, 8)
    ]
    for (v, w) in edges:
        DG.add_edge(v, w)

    print(f'Vertex count: {DG.v()}')
    print(f'Edge count: {DG.e()}')
    print(DG)
    print('Edges for vertex 0:')
    print(DG.adj(0))
    print('Edges for vertex 9:')
    print(DG.adj(9))
    print('Edges for vertex 5:')
    print(DG.adj(5))

    assert DG.v() == 10
    assert DG.e() == 12
    assert DG.adj(0) == [8, 9, 7]
    assert DG.adj(9) == [2]
    assert DG.adj(5) == []
