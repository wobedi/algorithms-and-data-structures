from functools import reduce

from src.graphs.operations.graph_connectivity import GraphStrongConnectivity
from src.graphs.operations.graph_search import GraphSearch
from src.graphs.operations.graph_topological_sort import topologically_sort


class Digraph:
  def __init__(self, vertex_count):
    """Implements a digraph that supports self loops but not parallel edges"""
    self.vertex_count = vertex_count
    self.adj_list = [set() for v in range(vertex_count)]
    self.adj_list_reversed = [set() for v in range(vertex_count)]

  def __str__(self):
    return (f'Adj List: {[list(v) for v in self.adj_list]}\n'
            f'Adj List reversed: {[list(v) for v in self.adj_list_reversed]}\n'
            f'**********************************************')

  def add_edge(self, v: int, w: int):
    """adds a directional edge from v to w"""
    self.adj_list[v].add(w)
    self.adj_list_reversed[w].add(v)

  def adj(self, v):
    """returns a list of vertices adjacent to v"""
    return list(self.adj_list[v])

  def adj_reversed(self, v):
    """returns a list of vertices adjacent to v in reversed digraph"""
    return list(self.adj_list_reversed[v])

  def e(self):
    """returns number of edges"""
    return reduce(lambda a, b: a + len(b), self.adj_list, 0)

  def edge_between(self, v, w):
    """returns True if there is a directional edge from v to w, else False"""
    return w in self.adj_list[v]

  def edge_between_reversed(self, v, w):
    """returns True if there is a directional edge from v to w in reversed digraph, else False"""
    return w in self.adj_list_reversed[v]

  def v(self):
    """returns number of vertices"""
    return self.vertex_count

if __name__ == "__main__":
  DG = Digraph(10)
  print(DG)
  DG.add_edge(0,9)
  DG.add_edge(0,9)
  print(DG)
  DG.add_edge(0,8)
  DG.add_edge(0,7)
  DG.add_edge(1,2)
  DG.add_edge(1,1)
  DG.add_edge(2,6)
  DG.add_edge(2,9)
  DG.add_edge(9,2)
  DG.add_edge(3,5)
  DG.add_edge(6,9)
  DG.add_edge(7,8)
  DG.add_edge(8,0)
  print(f'Vertex count: {DG.v()}')
  print(f'Edge count: {DG.e()}')
  print(DG)
  print('Edges for vertex 0:')
  print(DG.adj(0))
  print('Edges for vertex 9:')
  print(DG.adj(9))
  print('Edges for vertex 5:')
  print(DG.adj(5))
  GS = GraphSearch(DG, 0)
  print(GS.source_has_path_to(2))
  print('Path from source to 2:', GS.source_path_to(2))
  print(GS.source_has_path_to(3))
  print('Path from source to 3:', GS.source_path_to(3))
  print('Arbitrary cycle (if any):', GS.cycle)
  # print(f'Topologically sorted: {DG.topologically_sorted()}')  EXPECT TO THROW ERROR

  SC = GraphStrongConnectivity(DG)
  print(SC)
  assert SC.strongly_connected(0, 7) == True
  assert SC.strongly_connected(6, 2) == True
  assert SC.strongly_connected(1, 1) == True
  assert SC.strongly_connected(0, 9) == False
  assert SC.strongly_connected(3, 5) == False
  assert SC.count() == 6

  DG2 = Digraph(7)
  print(DG2)
  DG2.add_edge(0,1)
  DG2.add_edge(1,2)
  DG2.add_edge(1,3)
  DG2.add_edge(0,4)
  DG2.add_edge(4,5)
  DG2.add_edge(4,6)
  print(DG2)
  print(f'Topologically sorted: {topologically_sort(DG2)}')

# Adj List: [[], [], [], [], [], [], [], [], [], []]
# Adj List reversed: [[], [], [], [], [], [], [], [], [], []]
# **********************************************
# Adj List: [[9], [], [], [], [], [], [], [], [], []]
# Adj List reversed: [[], [], [], [], [], [], [], [], [], [0]]
# **********************************************
# Vertex count: 10
# Edge count: 12
# Adj List: [[8, 9, 7], [1, 2], [9, 6], [5], [], [], [9], [8], [0], [2]]
# Adj List reversed: [[8], [1], [1, 9], [], [], [3], [2], [0], [0, 7], [0, 2, 6]]
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
# Arbitrary cycle (if any): [0, 8, 7, 0]
# Strong components: [[5], [4], [3], [2, 6, 9], [1], [0, 7, 8]]
# Adj List: [[], [], [], [], [], [], []]
# Adj List reversed: [[], [], [], [], [], [], []]
# **********************************************
# Adj List: [[1, 4], [2, 3], [], [], [5, 6], [], []]
# Adj List reversed: [[], [0], [1], [1], [0], [4], [4]]
# **********************************************
# Topologically sorted: [0, 4, 6, 5, 1, 3, 2]