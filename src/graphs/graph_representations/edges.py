class Edge:
  def __init__(self, v, w, weight=0):
    self.v = v
    self.w = w
    self.weight = weight

  def __str__(self):
    return f'{self.v} - {self.w}: {self.weight}'

  def either(self):
    return self.v

  def both(self):
    return self.v, self.w

  def other(self, vertex):
    if vertex != self.v and vertex != self.w:
      print(f'Error: This Edge connects {self.v} and {self.w} - not {vertex}')
      return
    return self.v if vertex == self.w else self.w
  
  def compare_to(self, other):
    if self.weight < other.weight:
      return -1
    if self.weight > other.weight:
      return 1
    return 0

class DirectedEdge:
  # TODO: Inherit here?
  def __init__(self, v, w, weight=0):
    self.v = v
    self.w = w
    self.weight = weight
  
  def __str__(self):
    return f'{self.v} - {self.w}: {self.weight}'

  def from_(self):
    return self.v

  def to(self):
    return self.w
  
  def compare_to(self, other):
    if self.weight < other.weight:
      return -1
    if self.weight > other.weight:
      return 1
    return 0


