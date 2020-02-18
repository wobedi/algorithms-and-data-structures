class Edge:
    """Implements an undirected Edge, optionally weighted"""
    def __init__(self, v, w, weight=0):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return f'{self.v} - {self.w}: {self.weight}'

    def either(self):
        """Returns pointer to an arbitrary vertex of the edge"""
        return self.v

    def both(self):
        """Returns pointers to both vertices of the edge"""
        return self.v, self.w

    def other(self, vertex):
        """Returns the corresponding other vertex of the edge, if possible"""
        if vertex != self.v and vertex != self.w:
            print(f'Error: Edge connects {self.v} and {self.w} - not {vertex}')
            return False
        return self.v if vertex == self.w else self.w

    def compare_to(self, other: Edge):
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
    def __init__(self, v, w, weight=0):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return f'{self.v} - {self.w}: {self.weight}'

    def from_(self):
        """Returns pointer to starting vertex"""
        return self.v

    def to(self):
        """"Returns pointer to ending vertex"""
        return self.w

    def compare_to(self, other: DirectedEdge):
        """Returns -1/0/1 if this edge has less/the same/more weight
        than the other edge.
        """
        if self.weight < other.weight:
            return -1
        if self.weight > other.weight:
            return 1
        return 0
