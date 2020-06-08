from src.implementations.graphs.representations.graph_undirected import Graph
from src.implementations.graphs.representations.graph_directed import Digraph


class GraphSearch:
    """Preprocesses a graph to store shortest paths from a given source vertex
    to all other vertices that are connected to this source vertex.
    This allows the lookup of paths in O(L) where L is the length of the path.
    """
    def __init__(self, graph, source_vertex: int, method='bfs'):
        self.graph = graph
        self.source = source_vertex
        self.count = graph.v()
        self.visited = [False for v in range(graph.v())]
        self.parent = [None for v in range(graph.v())]
        self.cycle = []

        if method == 'bfs':
            self._bfs()
        elif method == 'dfs_recursive':
            self._dfs(source_vertex)
        else:
            self._dfs_iterative()

    def is_cyclic(self) -> bool:
        """Returns True if graph is cyclic, else False"""
        return bool(self.cycle)

    def source_has_path_to(self, v: int) -> bool:
        """Returns True if there is a path from source to v, else False"""
        return self.visited[v]

    def source_path_to(self, v: int) -> list:
        """Returns the path from source to v if there is one, else []"""
        if not self.source_has_path_to(v):
            return []
        path = [v]
        parent = self.parent[v]
        while parent is not self.source:
            path.append(parent)
            parent = self.parent[parent]
        path.append(self.source)
        path.reverse()
        return path

    def _bfs(self):
        # Breadth-first search, iteratively, starting at the source
        queue = [self.source]
        while queue:
            v = queue.pop()
            self.visited[v] = True
            for w in self.graph.adj(v):
                # if self.visited[w] is True and not w == self.parent[v]:
                #     self.cycle = (self.source_path_to(w)
                #                   + list(reversed(self.source_path_to(v))))
                if self.visited[w] is False:
                    self.parent[w] = v
                    queue.append(w)

    def _dfs(self, v: int):
        # Depth-first search, recursively
        self.visited[v] = True
        for w in self.graph.adj(v):
            # if self.visited[w] is True and not w == self.parent[v]:
            #     self.cycle = (self.source_path_to(w)
            #                   + list(reversed(self.source_path_to(v))))
            if self.visited[w] is False:
                self.parent[w] = v
                self._dfs(w)

    def _dfs_iterative(self):
        # Depth-first search, iteratively
        stack = [(self.source, None)]
        while stack:
            (v, parent) = stack.pop()
            # if self.visited[v] is True and not v == self.parent[parent]:
            #     self.cycle = (self.source_path_to(v) +
            #                   list(reversed(self.source_path_to(parent))))
            if self.visited[v] is False:
                self.visited[v] = True
                self.parent[v] = parent
                stack.extend([(adj, v) for adj in self.graph.adj(v)])

    def _has_self_loop(self):
        # Returns True if any vertex v in self.graph self-loops, else false
        for v in range(self.count):
            for w in self.graph.adj(v):
                if w == v:
                    self.cycle.extend([v, v])
                    return True
        return False

    def _has_parallel_edge(self):
        # Returns True if any vertex v has parallel edges, else false
        for v in range(self.count):
            visited = [False for v in range(self.count)]
            for w in self.graph.adj(v):
                if visited[w]:
                    self.cycle.extend([v, w, v])
                    return True
                visited[w] = True
        return False


if __name__ == '__main__':
    """Undirected graph search"""
    G = Graph(10)
    edges = [
        (0, 9),
        (0, 8),
        (0, 7),
        (1, 2),
        (1, 1),
        (2, 6),
        (9, 2),
        (3, 5),
        (6, 9),
    ]
    for (v, w) in edges:
        G.add_edge(v, w)

    GS = GraphSearch(G, 0)

    assert GS.source_has_path_to(6) is True
    assert GS.source_path_to(6) == [0, 9, 2, 6]
    assert GS.source_has_path_to(3) is False
    assert GS.source_path_to(3) == []
    assert GS.is_cyclic() is True
    assert GS.cycle != []
    print('Arbitrary cycle (undirected):', GS.cycle)

    """Directed graph search"""
    DG = Digraph(10)
    edges = [
        (0, 9),
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

    GSD = GraphSearch(DG, 0)

    assert GSD.source_has_path_to(2) is True
    assert GSD.source_path_to(2) == [0, 9, 2]
    assert GSD.source_has_path_to(3) is False
    assert GSD.source_path_to(3) == []
    assert GSD.is_cyclic() is True
    assert GSD.cycle != []
    print('Arbitrary cycle (undirected):', GSD.cycle)
