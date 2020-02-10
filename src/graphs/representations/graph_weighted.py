from functools import reduce

from edges import DirectedEdge
from src.graphs.operations.graph_shortest_path import GraphShortestPath


class DigraphWeighted:
  """Supports parallel edges and self loops"""
  def __init__(self, vertex_count):
    self.vertex_count = vertex_count
    self.adj_list = [set() for v in range(vertex_count)]

  def __str__(self):
    edges_flat = [e for s in self.adj_list for e in s]
    formatted = [f'{e.from_()}->{e.to()}: {e.weight}' for e in edges_flat]
    return (f'Adj List: {formatted}\n'
            f'**********************************************')
  
  def add_edge(self, e: DirectedEdge):
    """adds edge from v to w"""
    self.adj_list[e.from_()].add(e)

  def adj(self, v):
    """returns edges from v"""
    return [edge for edge in self.adj_list[v]]

  def edge_between(self, v, w):
    """returns True if there is an edge from v to w, else False"""
    return reduce(lambda a, b: a | b.to() == w, self.adj_list, False)

  def edges(self):
    """returns iterable of edges"""
    return [e for s in self.adj_list for e in s]

  def e(self):
    """returns number of edges"""
    return reduce(lambda a, b: a + len(b), self.adj_list, 0)

  def v(self):
    """returns number of vertices"""
    return len(self.adj_list)

if __name__ == '__main__':
  graph_size = 10
  DGW = DigraphWeighted(graph_size)
  for i, j in zip(range(15), range(0, 30, 2)):
    DE = DirectedEdge(i % graph_size, i*(3*i+2)//3 % graph_size, j)
    DGW.add_edge(DE)
  MORE = [(4, 7, 31), (4, 2, 32), (2, 3, 33), (1, 0, 33)]
  for i in MORE:
    DGW.add_edge(DirectedEdge(i[0], i[1], i[2]))
  print(DGW)
  SP = GraphShortestPath(DGW, 4)
  print(f'4 to 5: {SP.source_distance_to(5)} via {SP.source_shortest_path_to(5)}')
  print(f'4 to 3: {SP.source_distance_to(3)} via {SP.source_shortest_path_to(3)}')
  print(f'4 to 6: {SP.source_distance_to(6)} via {SP.source_shortest_path_to(6)}')
  print(f'4 to 7: {SP.source_distance_to(7)} via {SP.source_shortest_path_to(7)}')
  print(f'4 to 4: {SP.source_distance_to(4)} via {SP.source_shortest_path_to(4)}')


# Adj List: ['0->0: 0', '0->6: 20', '1->8: 22', '1->1: 2', '1->0: 33', '2->2: 24', '2->5: 4', '2->3: 33', '3->1: 6', '3->7: 26', '4->5: 28', '4->7: 31', '4->8: 8', '4->2: 32', '5->8: 10', '6->0: 12', '7->3: 14', '8->9: 16', '9->7: 18']
# **********************************************
# 4 to 5: 28 via [4, 5]
# 4 to 3: 45 via [4, 7, 3]
# 4 to 6: 104 via [4, 7, 3, 1, 0, 6]
# 4 to 7: 31 via [4, 7]
# 4 to 4: 0 via [4]