class GraphSearch:

  def __init__(self, graph, source_vertex):
    self.graph = graph
    self.source = source_vertex
    self.count = graph.v()
    self.visited = [False for v in range(graph.v())]
    self.parent = [None for v in range(graph.v())]
    self.cycle = []
    self._dfs(source_vertex)

  def is_acyclic(self):
    return bool(self.cycle)

  def source_has_path_to(self, v):
    return self.visited[v]

  def source_path_to(self, v):
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
    queue = [self.source]
    while queue:
      v = queue.pop(0)
      self.visited[v] = True
      for w in self.graph.adj(v):
        if self.visited[w] == True and not w == self.parent[v]:
          self.cycle = self.source_path_to(w) + list(reversed(self.source_path_to(v)))
        if self.visited[w] == False:
          self.parent[w] = v
          queue.append(w)

  def _dfs(self, v):
    self.visited[v] = True
    for w in self.graph.adj(v):
      if self.visited[w] == True and not w == self.parent[v]:
        self.cycle = self.source_path_to(w) + list(reversed(self.source_path_to(v)))
      if self.visited[w] == False:
        self.parent[w] = v
        self._dfs(w)

  def _dfs_iterative(self):
    stack = [(self.source, None)]
    while stack:
      (v, parent) = stack.pop()
      if self.visited[v] == True and not v == self.parent[parent]:
        self.cycle = self.source_path_to(v) + list(reversed(self.source_path_to(parent)))
      if self.visited[v] == False:
        self.visited[v] = True
        self.parent[v] = parent
        stack.extend([(adj, v) for adj in self.graph.adj(v)])

  def _has_self_loop(self):
    for v in range(self.count):
      for w in self.graph.adj(v):
        if w == v:
          self.cycle.extend([v, v])
          return True

  def _has_parallel_edge(self):
    for v in range(self.count):
      visited = [False for v in range(self.count)]
      for w in self.graph.adj(v):
        if visited[w]:
          self.cycle.extend([v, w, v])
          return True
        visited[w] = True