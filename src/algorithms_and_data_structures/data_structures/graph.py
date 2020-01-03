from functools import reduce
from pandas import DataFrame

class ListItem:
  # TODO change this to bag?
  # TODO Refactor this into LinkedList & ListItem classes in sep file and import
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def all(self):
    res = []
    item = self
    while item is not None:
      res.append(item.value) if item.value is not None else None
      item = item.next
    return res

  def contains(self, value):
    item = self
    while item is not None:
      if item.value == value:
        return True
      item = item.next
    return False

  def count(self):
    count = 0
    item = self
    while item.next is not None:
      count += 1
      item = item.next
    return count

  def final(self):
    item = self
    while item.next is not None:
      item = item.next
    return item

class Digraph:
  # TODO Inheriting from Graph? Or rather: Refactor graph based on Digraph
  def __init__(self, vertex_count):
    """Implements a digraph that supports self loops but not parallel edges"""
    self.vertex_count = vertex_count
    self.adj_list = [set() for v in range(vertex_count)]

  def __str__(self):
    return (f'Adj List: {[list(v) for v in self.adj_list]}\n'
            f'**********************************************')

  def add_edge(self, v, w):
    """adds a directional edge from v to w"""
    self.adj_list[v].add(w)

  def adj(self, v):
    """returns a list of vertices adjacent to v"""
    return list(self.adj_list[v])

  def e(self):
    """returns number of edges"""
    return len([w for v in self.adj_list for w in v])

  def edge_between(self, v, w):
    """returns True if there is a directional edge from v to w, else False"""
    return w in self.adj_list[v]

  def v(self):
    """returns number of vertices"""
    return self.vertex_count

  def topological_sort(self):
    """implements https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search"""
    # TODO
    pass

class Graph:
  # TODO: Missing error handling
  def __init__(self, vertex_count):
    """implementing three graph representation variants for illustration purposes:
       list of edges, adjaceny matrix, adjacency list.
       Supports self loops but not parallel edges."""
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
    """adds edge between v and w"""
 
    # add edge to edge list
    (self.edge_list.append((v, w)) 
      if not (v, w) in self.edge_list 
      and not (w, v) in self.edge_list
      else None)

    # add edge to adj matrix
    self.adj_matrix[v][w] = self.adj_matrix[w][v] = 1
    
    # add edge to adj list
    if not w in self.adj_list[v]:
      self.adj_list[v].add(w)
      self.adj_list[w].add(v)

  def adj(self, v):
    """returns iterable of vertices adjacent to v from adj list"""
    return self._adj_from_adj_list(v)

  def e(self):
    """returns number of edges"""
    return self._e_from_adj_list()

  def edge_between(self, v, w):
    """returns True if there is and edge between v and w, else False"""
    # using only adjacency list here to not overcomplicate this code
    return w in self.adj_list[v]

  def v(self):
    """returns number of vertices"""
    return self.vertex_count

  def _adj_from_edge_list(self, v):
    """returns iterable of vertices adjacent to v from edge list"""
    return [edge[0] if edge[1] == v else edge[1]
            for edge in self.edge_list
            if edge[0] == v or edge[1] == v]

  def _adj_from_adj_matrix(self, v):
    """returns iterable of vertices adjacent to v from adj matrix"""
    return [index for (index, value) in enumerate(self.adj_matrix[v]) if value == 1]

  def _adj_from_adj_list(self, v):
    """returns iterable of vertices adjacent to v from adj list"""
    return self.adj_list[v]

  def _e_from_edge_list(self):
    """returns number of edges from edge list"""
    return len(self.edge_list)

  def _e_from_adj_matrix(self):
    """returns number of edges from adj matrix"""
    # dividing by 2 because each edge is represented twice: [v][w] and [w][v]
    return reduce(lambda a, b: a + b.count(1), self.adj_matrix, 0) // 2

  def _e_from_adj_list(self):
    """returns number of edges from adj list"""
    # dividing by 2 because each edge is represented twice
    return sum([len(vertex_set) for vertex_set in self.adj_list]) // 2


class GraphConnectivityQueries:
  # TODO Put into own module with graph search as graph queries?
  def __init__(self, graph: Graph):
    """preprocesses a graph into all its maximally-connected components in order to find unions in constant time"""
    self.graph = graph
    self.vertex_count = self.graph.v()
    self.component_of = [None for v in range(self.vertex_count)]
    self.vertex_visited = [False for v in range(self.vertex_count)]
    self.component_count = 0
    self._preprocess()

  def connected(self, v, w):
    """returns True if v and w are connected, else False"""
    # TODO: Rm assert statement in here? put into unit test?
    assert self.component_of[v] is not None and self.component_of[w] is not None
    return self.component_of[v] == self.component_of[w]

  def count(self):
    """returns the number of distinct components"""
    return self.component_count

  def id(self, v):
    """returns the connected component id for a given vertex"""
    return self.component_of[v]

  def _preprocess(self):
    # would run faster if we add a (duplicate) tweaked dfs/bfs method to this class
    # this would mean duplicate dfs/bfs code but we could get rid of the nested for loop
    for v in range(self.vertex_count):
      if self.vertex_visited[v] == False:
        self.component_count += 1
        GS = GraphSearch(self.graph, v)
        for vertex, visited in enumerate(GS.vertex_visited):
          if visited:
            self.vertex_visited[vertex] = True
            self.component_of[vertex] = self.component_count


class GraphSearch:
  # TODO split into own module
  # TODO enable choice between dfs, dfs iterative and bfs for user
  # TODO bonus: enable finding of multiple paths via generator
  def __init__(self, graph, source_vertex):
    self.graph = graph
    self.source = source_vertex
    self.vertex_count = self.graph.v()
    self.vertex_visited = [False for v in range(self.vertex_count)]
    self.parent = [None for v in range(self.vertex_count)]
    self.cycle = []
    self._bfs()

  def is_acyclic(self):
    return bool(self.cycle)

  def source_has_path_to(self, v):
    return self.vertex_visited[v]

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
      self.vertex_visited[v] = True
      for w in self.graph.adj(v):
        if self.vertex_visited[w] == True and not w == self.parent[v]:
          self.cycle = self.source_path_to(w) + list(reversed(self.source_path_to(v)))
        if self.vertex_visited[w] == False:
          self.parent[w] = v
          queue.append(w)

  def _dfs(self, v):
    self.vertex_visited[v] = True
    for w in self.graph.adj(v):
      if self.vertex_visited[w] == True and not w == self.parent[v]:
        self.cycle = self.source_path_to(w) + list(reversed(self.source_path_to(v)))
      if self.vertex_visited[w] == False:
        self.parent[w] = v
        self._dfs(w)

  def _dfs_iterative(self):
    stack = [(self.source, None)]
    while stack:
      (v, parent) = stack.pop()
      if self.vertex_visited[v] == True and not v == self.parent[parent]:
        self.cycle = self.source_path_to(v) + list(reversed(self.source_path_to(parent)))
      if self.vertex_visited[v] == False:
        self.vertex_visited[v] = True
        self.parent[v] = parent
        stack.extend([(adj, v) for adj in self.graph.adj(v)])

  def _has_self_loop(self):
    for v in range(self.vertex_count):
      for w in self.graph.adj(v):
        if w == v:
          self.cycle.extend([v, v])
          return True

  def _has_parallel_edge(self):
    for v in range(self.vertex_count):
      visited = [False for v in range(self.vertex_count)]
      for w in self.graph.adj(v):
        if visited[w]:
          self.cycle.extend([v, w, v])
          return True
        visited[w] = True


# class GraphCycles:
# DOESNT WORK - SEEMS VERY COMLPEX
#   def __init__(self, graph: Graph):
#     self.graph = graph
#     self.vertex_count = self.graph.v()
#     self.vertex_visited = [False for v in range(self.vertex_count)]
#     self.parent = [None for v in range(self.vertex_count)]
#     self.cycles = set()

#   def dfs_with_cycles(self, v, entry):
#     self.vertex_visited[v] = True
#     for w in self.graph.adj(v):
#       if self.vertex_visited[w] == True:
#         cycle = self.path_between()
#       if self.vertex_visited[w] == False:
#         self.vertex_visited[w] = True
#         self.parent[w] = v
#         self.dfs_with_cycles[w, entry]

#   def find_cycles(self):
#     self_loop_generator = self.find_self_loops()
#     parallel_edge_generator = self.find_parallel_edges()
#     for _ in self_loop_generator:
#       yield
#     for _ in parallel_edge_generator:
#       yield
#     CC = GraphConnectivityQueries(self.graph)
#     entry_points = CC.get_one_vertex_per_component()
#     for v in entry_points:

#   def find_self_loops(self):
#     for v in range(self.vertex_count):
#       for w in self.graph.adj(v):
#         if w == v:
#           self.cycles.add([v, v])
#           yield

#   def find_parallel_edges(self):
#     for v in range(self.vertex_count):
#       visited = [False for v in range(self.vertex_count)]
#       for w in self.graph.adj(v):
#         if visited[w]:
#           self.cycles.add([v, w, v])
#           yield
#         visited[w] = True

#   def has_path_between(self, u, v):
#     return self.vertex_visited[u] & self.vertex_visited[v]

#   def path_between(self, u, v):
#     if not self.has_path_to(v):
#       return []
#     path = [v]
#     parent = self.parent[v]
#     while parent is not u: 
#       path.append(parent)
#       parent = self.parent[parent]
#     path.append(u)
#     path.reverse()
#     return path


# TODO translate this into a proper unit test
# if __name__ == "__main__":
#   DG = Digraph(10)
#   print(DG)
#   DG.add_edge(0,9)
#   DG.add_edge(0,9)
#   print(DG)
#   DG.add_edge(0,8)
#   DG.add_edge(0,7)
#   DG.add_edge(1,2)
#   DG.add_edge(1,1)
#   DG.add_edge(2,6)
#   DG.add_edge(2,9)
#   DG.add_edge(9,2)
#   DG.add_edge(3,5)
#   DG.add_edge(6,9)
#   print(f'Vertex count: {DG.v()}')
#   print(f'Edge count: {DG.e()}')
#   print(DG)
#   print('Edges for vertex 0:')
#   print(DG.adj(0))
#   print('Edges for vertex 9:')
#   print(DG.adj(9))
#   print('Edges for vertex 5:')
#   print(DG.adj(5))
#   GS = GraphSearch(DG, 0)
#   print(GS.source_has_path_to(2))
#   print('Path from source to 2:', GS.source_path_to(2))
#   print(GS.source_has_path_to(3))
#   print('Path from source to 3:', GS.source_path_to(3))
#   print('Arbitrary cycle (if any):', GS.cycle)
  # CC = GraphConnectivityQueries(DG)
  # print(CC)
  # assert CC.connected(0, 1) == True
  # assert CC.connected(0, 3) == False
  # assert CC.connected(3, 4) == False
  # assert CC.id(0) == 1
  # assert CC.id(1) == 1
  # assert CC.id(4) == 3
  # assert CC.count() == 3


# Adj List: [[], [], [], [], [], [], [], [], [], []]
# **********************************************
# Adj List: [[9], [], [], [], [], [], [], [], [], []]
# **********************************************
# Vertex count: 10
# Edge count: 10
# Adj List: [[8, 9, 7], [1, 2], [9, 6], [5], [], [], [9], [], [], [2]]
# **********************************************
# Edges for vertex 0:
# [8, 9, 7]
# Edges for vertex 9:
# [2]
# Edges for vertex 5:
# []
# True
# Path from source to 2: [0, 9, 2]
# False
# Path from source to 3: []
# Arbitrary cycle (if any): [0, 9, 6, 2, 9, 0]

if __name__ == "__main__":
  G = Graph(10)
  print(G)
  G.add_edge(0,9)
  G.add_edge(0,9)
  print(G)
  G.add_edge(0,8)
  G.add_edge(0,7)
  G.add_edge(1,2)
  G.add_edge(1,1)
  G.add_edge(2,6)
  G.add_edge(2,9)
  G.add_edge(9,2)
  G.add_edge(3,5)
  G.add_edge(6,9)
  print(f'Vertex count: {G.v()}')
  print(f'Edge count: {G._e_from_edge_list()} / {G._e_from_adj_matrix()} / {G._e_from_adj_list()}')
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
  CC = GraphConnectivityQueries(G)
  print(CC)
  assert CC.connected(0, 1) == True
  assert CC.connected(0, 3) == False
  assert CC.connected(3, 4) == False
  assert CC.id(0) == 1
  assert CC.id(1) == 1
  assert CC.id(4) == 3
  assert CC.count() == 3

# Edge List: []
# Adj Matrix: 
#    0  1  2  3  4  5  6  7  8  9
# 0  0  0  0  0  0  0  0  0  0  0
# 1  0  0  0  0  0  0  0  0  0  0
# 2  0  0  0  0  0  0  0  0  0  0
# 3  0  0  0  0  0  0  0  0  0  0
# 4  0  0  0  0  0  0  0  0  0  0
# 5  0  0  0  0  0  0  0  0  0  0
# 6  0  0  0  0  0  0  0  0  0  0
# 7  0  0  0  0  0  0  0  0  0  0
# 8  0  0  0  0  0  0  0  0  0  0
# 9  0  0  0  0  0  0  0  0  0  0
# Adj List: [set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
# **********************************************
# Edge List: [(0, 9)]
# Adj Matrix: 
#    0  1  2  3  4  5  6  7  8  9
# 0  0  0  0  0  0  0  0  0  0  1
# 1  0  0  0  0  0  0  0  0  0  0
# 2  0  0  0  0  0  0  0  0  0  0
# 3  0  0  0  0  0  0  0  0  0  0
# 4  0  0  0  0  0  0  0  0  0  0
# 5  0  0  0  0  0  0  0  0  0  0
# 6  0  0  0  0  0  0  0  0  0  0
# 7  0  0  0  0  0  0  0  0  0  0
# 8  0  0  0  0  0  0  0  0  0  0
# 9  1  0  0  0  0  0  0  0  0  0
# Adj List: [{9}, set(), set(), set(), set(), set(), set(), set(), set(), {0}]
# **********************************************
# Vertex count: 10
# Edge count: 8 / 8 / 8
# Edge List: [(0, 9), (0, 8), (0, 7), (1, 2), (2, 6), (2, 9), (3, 5), (6, 9)]
# Adj Matrix: 
#    0  1  2  3  4  5  6  7  8  9
# 0  0  0  0  0  0  0  0  1  1  1
# 1  0  0  1  0  0  0  0  0  0  0
# 2  0  1  0  0  0  0  1  0  0  1
# 3  0  0  0  0  0  1  0  0  0  0
# 4  0  0  0  0  0  0  0  0  0  0
# 5  0  0  0  1  0  0  0  0  0  0
# 6  0  0  1  0  0  0  0  0  0  1
# 7  1  0  0  0  0  0  0  0  0  0
# 8  1  0  0  0  0  0  0  0  0  0
# 9  1  0  1  0  0  0  1  0  0  0
# Adj List: [{8, 9, 7}, {2}, {1, 6, 9}, {5}, set(), {3}, {9, 2}, {0}, {0}, {0, 2, 6}]
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
# <__main__.GraphConnectivityQueries object at 0x7f87af109110>