from functools import reduce
from pandas import DataFrame

class ListItem:
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
  def __init__(self, vertex_count):
    # implementing three graph representation variants for illustration purposes:
    # list of edges, adjaceny matrix, adjacency list
    self.vertex_count = vertex_count
    self.edge_list = []
    self.adj_matrix = ([
      [0 for i in range(vertex_count)] for i in range(vertex_count)
    ])
    self.adj_list = [ListItem(None) for i in range(vertex_count)]

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
  G.add_edge(0,2)
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
  