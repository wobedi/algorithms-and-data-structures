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


class Graph:
  # TODO: Missing error handling
  # TODO: What about self loops?
  # TODO: What about parallel edges?
  def __init__(self, vertex_count):
    # implementing three graph representation variants for illustration purposes:
    # list of edges, adjaceny matrix, adjacency list
    self.vertex_count = vertex_count
    self.edge_list = []
    self.adj_matrix = ([
      [0 for i in range(vertex_count)] for i in range(vertex_count)
    ])
    self.adj_list = [ListItem(None) for i in range(vertex_count)]
    # TODO: Switch adjacency list to array of arrays for simplicity and cache perf
    # TODO: Bonus: Switch adjacency list to list of dicts for ultimate perf

  def __str__(self):
    return (f'Edge List: {self.edge_list}\n'
            f'Adj Matrix: \n{DataFrame(self.adj_matrix)}\n' 
            f'Adj List: {[v.all() for v in self.adj_list]}\n'
            f'**********************************************')

  def add_edge(self, v, w):
    """adds edge between v and w"""
    if v == w: 
      return
  
    # add edge to edge list
    (self.edge_list.append((v, w)) 
      if not (v, w) in self.edge_list 
      and not (w, v) in self.edge_list
      else None)

    # add edge to adj matrix
    self.adj_matrix[v][w] = self.adj_matrix[w][v] = 1
    
    # add edge to adj list
    if not self.adj_list[v].contains(w):
      self.adj_list[v].final().next = ListItem(w)
      self.adj_list[w].final().next = ListItem(v)

  def edge_between(self, v, w):
    """returns True if there is and edge between v and w, else False"""
    # using only adjacency list here to not overcomplicate this code
    return self.adj_list[v].contains(w)

  def adj_from_edge_list(self, v):
    """returns iterable of vertices adjacent to v from edge list"""
    return [edge[0] if edge[1] == v else edge[1]
            for edge in self.edge_list
            if edge[0] == v or edge[1] == v]

  def adj_from_adj_matrix(self, v):
    """returns iterable of vertices adjacent to v from adj matrix"""
    return [index for (index, value) in enumerate(self.adj_matrix[v]) if value == 1]

  def adj_from_adj_list(self, v):
    """returns iterable of vertices adjacent to v from adj list"""
    return self.adj_list[v].all()

  def v(self):
    return self.vertex_count

  def e_from_edge_list(self):
    """returns number of edges from edge list"""
    return len(self.edge_list)

  def e_from_adj_matrix(self):
    """returns number of edges from adj matrix"""
    # dividing by 2 because each edge is represented twice: [v][w] and [w][v]
    return reduce(lambda a, b: a + b.count(1), self.adj_matrix, 0) // 2

  def e_from_adj_list(self):
    """returns number of edges from adj list"""
    # dividing by 2 because each edge is represented twice
    return sum([vertex.count() for vertex in self.adj_list]) // 2


class GraphSearch:
  # TODO split into own module
  # TODO enable choice between dfs and bfs for user
  def __init__(self, graph, source_vertex):
    self.graph = graph
    self.source = source_vertex
    self.vertex_visited = [False for v in range(graph.v())]
    self.parent = [None for v in range(graph.v())]
    self.bfs()

  def bfs(self):
    queue = [self.source]
    self.vertex_visited[self.source] = True
    while queue:
      v = queue.pop(0)
      for w in self.graph.adj_from_adj_list(v):
        if self.vertex_visited[w] == False:
          self.vertex_visited[w] = True
          self.parent[w] = v
          queue.append(w)

  def dfs(self, v):
    self.vertex_visited[v] = True
    for w in self.graph.adj_from_adj_list(v):
      if self.vertex_visited[w] == False:
        self.parent[w] = v
        self.dfs(w)

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


# TODO translate this into a proper unit test
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
  print(f'Vertex count: {G.vertex_count}')
  print(f'Edge count: {G.e_from_edge_list()} / {G.e_from_adj_matrix()} / {G.e_from_adj_list()}')
  print(G)
  print('Edges for vertex 0:')
  print(G.adj_from_edge_list(0))
  print(G.adj_from_adj_matrix(0))
  print(G.adj_from_adj_list(0))
  print('Edges for vertex 9:')
  print(G.adj_from_edge_list(9))
  print(G.adj_from_adj_matrix(9))
  print(G.adj_from_adj_list(9))
  print('Edges for vertex 5:')
  print(G.adj_from_edge_list(5))
  print(G.adj_from_adj_matrix(5))
  print(G.adj_from_adj_list(5))
  DFS = GraphSearch(G, 0)
  print(DFS.source_has_path_to(6))
  print(DFS.source_path_to(6))
  print(DFS.source_has_path_to(3))
  print(DFS.source_path_to(3))

# **********************************************
# Vertex count: 10
# Edge count: 7 / 7 / 7
# Edge List: [(0, 9), (0, 8), (0, 7), (1, 2), (2, 6), (2, 9), (3, 5)]
# Adj Matrix: 
#    0  1  2  3  4  5  6  7  8  9
# 0  0  0  0  0  0  0  0  1  1  1
# 1  0  0  1  0  0  0  0  0  0  0
# 2  0  1  0  0  0  0  1  0  0  1
# 3  0  0  0  0  0  1  0  0  0  0
# 4  0  0  0  0  0  0  0  0  0  0
# 5  0  0  0  1  0  0  0  0  0  0
# 6  0  0  1  0  0  0  0  0  0  0
# 7  1  0  0  0  0  0  0  0  0  0
# 8  1  0  0  0  0  0  0  0  0  0
# 9  1  0  1  0  0  0  0  0  0  0
# Adj List: [[9, 8, 7], [2], [1, 6, 9], [5], [], [3], [2], [0], [0], [0, 2]]
# **********************************************
# Edges for vertex 0:
# [9, 8, 7]
# [7, 8, 9]
# [9, 8, 7]
# Edges for vertex 9:
# [0, 2]
# [0, 2]
# [0, 2]
# Edges for vertex 5:
# [3]
# [3]
# [3]
# True
# [0, 9, 2, 6]
# False
# []
