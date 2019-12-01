### TODO: Put magic numbers from here and from hash map into config

class HashSet:
  def __init__(self, size):
    self.size = size
    self.set = [None for i in range(size)]
    self.load = 0

  def contains(self, key):
    return self._find_index(key)[0]

  def put(self, key):
    key_in_set, index = self._find_index(key)
    if key_in_set:
      return f'Insertion error: Key {key} is already part of this hash set'
    self.set[index] = key
    self.load += 1
    if self.load / self.size > 0.75:
      self._upsize()
    return

  def delete(self, key):
    key_in_set, index = self._find_index(key)
    if not key_in_set:
      return f'Deletion error: Key {key} is NOT part of this hash set'
    self.set[index] = None
    self.load -= 1

    # moving subsequent items backwards to not break linear probing
    next = index + 1 
    while self.set[next % self.size] is not None:  # wrap around via modulo
       self.set[index], self.set[next] = self.set[next], self.set[index]
       index += 1
       next += 1
    
    if self.load / self.size < 0.25:
      self._downsize()
    return

  def _find_index(self, key, set_=None):
    """Linear probing for key through hash set. Returns tuple: (True, index) for search hits at index, (False, index) for search misses where index is the final index checked/first index with key==None"""
    set_ = set_ or self.set
    index = self._modular_hash(key)  # entry point for linear probing
    while set_[index] is not None:
      if index >= self.size:  # wrap around
        index = 0
        continue
      if set_[index] == key:
        return (True, index)
      index += 1
    return (False, index)

  def _modular_hash(self, key):
    return hash(key) % self.size

  def _upsize(self):
    return self._resize(2)

  def _downsize(self):
    return self._resize(0.5)

  def _resize(self, factor):
    self.size = int(self.size * factor)
    new_set = [None for i in range(self.size)]
    for key in self.set:
      if key is None: continue
      key_in_set, index = self._find_index(key, new_set)
      if key_in_set: return 'Syntax Error while resizing'
      new_set[index] = key
    self.set = new_set
    return

# Turn this into a unit test
if __name__ == '__main__':
  HT = HashSet(5)
  print(HT.set)
  print(HT.contains("hello"))
  print(HT.set)
  HT.put("hello")
  print(HT.set)
  print(HT.contains("hello"))
  print(HT.set)
  HT.put(1)
  print(HT.set)
  HT.put(2)
  print(HT.set)
  HT.put(3)
  print(HT.set)
  HT.put(4)
  print(HT.set)
  HT.put(5)
  print(HT.set)
  HT.put(6)
  print(HT.set)
  HT.put(7)
  print(HT.set)
  HT.delete(7)
  print(HT.set)
  HT.delete(7)
  print(HT.set)
  HT.delete(5)
  print(HT.set)
  HT.delete(3)
  print(HT.set)
  HT.delete(2)
  print(HT.set)
  HT.delete(4)
  print(HT.set)
  HT.delete("hello")
  print(HT.set)
  HT.delete(1)
  print(HT.set)