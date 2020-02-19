class GraphSearch:
    """Preprocesses a graph to store shortest paths from a given source vertex
    to all other vertices that are connected to this source vertex.
    This allows the lookup of paths in O(L) where L is the length of the path.
    """
    def __init__(self, graph, source_vertex: int):
        self.graph = graph
        self.source = source_vertex
        self.count = graph.v()
        self.visited = [False for v in range(graph.v())]
        self.parent = [None for v in range(graph.v())]
        self.cycle = []
        self._dfs(source_vertex)  # Could be replaced with bfs or iterative dfs

    def is_acyclic(self) -> bool:
        """Returns True if graph is acyclic, else False"""
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
            v = queue.pop(0)
            self.visited[v] = True
            for w in self.graph.adj(v):
                if self.visited[w] is True and not w == self.parent[v]:
                    self.cycle = (self.source_path_to(w)
                                  + list(reversed(self.source_path_to(v))))
                if self.visited[w] is False:
                    self.parent[w] = v
                    queue.append(w)

    def _dfs(self, v: int):
        # Depth-first search, recursively
        self.visited[v] = True
        for w in self.graph.adj(v):
            if self.visited[w] is True and not w == self.parent[v]:
                self.cycle = (self.source_path_to(w)
                              + list(reversed(self.source_path_to(v))))
            if self.visited[w] is False:
                self.parent[w] = v
                self._dfs(w)

    def _dfs_iterative(self):
        # Depth-first search, iteratively
        stack = [(self.source, None)]
        while stack:
            (v, parent) = stack.pop()
            if self.visited[v] is True and not v == self.parent[parent]:
                self.cycle = (self.source_path_to(v) +
                              list(reversed(self.source_path_to(parent))))
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
