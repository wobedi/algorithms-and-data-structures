class Edge:
    """Implements an undirected Edge, optionally weighted"""
    def __init__(self, v: int, w: int, weight=0):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return f'Edge between {self.v} and {self.w} with weight {self.weight}'

    def either(self) -> int:
        """Returns pointer to an arbitrary vertex of the edge"""
        return self.v

    def both(self) -> (int, int):
        """Returns pointers to both vertices of the edge"""
        return self.v, self.w

    def other(self, vertex) -> int:
        """Returns the corresponding other vertex of the edge, if possible"""
        if vertex != self.v and vertex != self.w:
            return -1
        return self.v if vertex == self.w else self.w

    def compare_to(self, other) -> int:
        """Returns -1/0/1 if this edge has less/the same/more weight
        than the other edge.
        """
        if self.weight < other.weight:
            return -1
        if self.weight > other.weight:
            return 1
        return 0


class DirectedEdge(Edge):
    """Implements a directed Edge, optionally weighted"""
    def __init__(self, v: int, w: int, weight=0):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return f'{self.v}->{self.w}: {self.weight}'

    def from_(self) -> int:
        """Returns pointer to starting vertex"""
        return self.v

    def to(self) -> int:
        """"Returns pointer to ending vertex"""
        return self.w


if __name__ == '__main__':
    """Undirected Edge"""
    E1 = Edge(0, 1, 10)
    E2 = Edge(1, 2, 20)
    print(E1)
    print(E2)

    assert E1.either() == 0 or E1.either() == 1
    assert E1.both() == (0, 1)
    assert E1.other(0) == 1 and E1.other(1) == 0
    assert E1.other(99) == -1

    assert E1.compare_to(E2) == -1
    assert E2.compare_to(E1) == 1
    assert E1.compare_to(E1) == 0

    """Directed Edge"""
    DE1 = DirectedEdge(3, 4, 10)
    DE2 = DirectedEdge(5, 6, 20)
    print(DE1)
    print(DE2)

    # Repeats same tests as with Edge to verify inherited methods work
    assert DE1.either() == 3 or DE1.either() == 4
    assert DE1.both() == (3, 4)
    assert DE1.other(3) == 4 and DE1.other(3) == 4
    assert DE1.other(99) == -1

    assert DE1.compare_to(DE2) == -1
    assert DE2.compare_to(DE1) == 1
    assert DE1.compare_to(DE1) == 0

    assert DE1.from_() == 3
    assert DE1.to() == 4
