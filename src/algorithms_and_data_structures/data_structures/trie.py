from functools import reduce

class TrieNode:
  def __init__(self, radix: int, value=None):
    self.next = [None for _ in range(radix)]
    self.value = value


class RWayTrie:
  """Implements an R-Way trie that defaults to a radix of 256 (extended ASCII)"""
  def __init__(self, radix=256):
    self.radix = radix
    self.root = TrieNode(radix)

  def get(self, string: str):
    self._throw_if_out_of_radix(string)
    node = self.root
    for c in string:
      i = ord(c)
      if node.next[i] is None:
        return False, f'Key "{string}" is NOT in trie'
      node = node.next[i]
    return True, f'Value at key "{string}" is {node.value}'

  def put(self, string: str, value):
    self._throw_if_out_of_radix(string)
    node = self.root
    for c in string:
      i = ord(c)
      if node.next[i] is None:
        node.next[i] = TrieNode(self.radix)
      node = node.next[i]

    if node.value:
      node.value = value
      return f'UPDATED Key "{string}" with value "{value}"'
    node.value = value
    return f'CREATED Key "{string}" with value "{value}"'
    
  def delete(self, string: str):
    self._throw_if_out_of_radix(string)
    self._delete(string, 0, self.root)
    
  def _delete(self, string: str, index: int, node):
    # base condition I: reached end of string and am still in trie
    if index == len(string):
      node.value = None
      return self._none_if_node_is_null_else_node(node)
    
    next_index = ord(string[index])
    next_node = node.next[next_index]
    
    # base condition II: trie ends but string has not yet ended
    if next_node is None:
      return f'Key "{string}" is NOT in trie'
    node.next[next_index] = self._delete(string, index + 1, next_node)
    return self._none_if_node_is_null_else_node(node)

  def _none_if_node_is_null_else_node(self, node: TrieNode):
    node_has_children = reduce(lambda a, b: b != None, node.next, None)
    if not node_has_children and not node.value:
      return None
    return node

  def _throw_if_out_of_radix(self, string: str):
    if len(string) < 1:
      raise ValueError('Please provide non-empty string')
    if not all(ord(c) < self.radix for c in string):
      raise ValueError(f'String "{string}" includes characters which '
                       f'encode to value outside of radix range {self.radix}')
    return

if __name__ == '__main__':
  T = RWayTrie()
  TEST_STRINGS = ['appleE', "donkey'][]", "garfield123"]
  print(T)
  T.get('a')
  for c in 'bcdeIUOHEWR$5345':
    T.put(c, ord(c))
  print(T)
  for s in TEST_STRINGS:
    T.put(s, s)
  for s in TEST_STRINGS:
    assert T.get(s)[0] != False
  T.delete('appleE')
  assert T.get('appleE')[0] == False
  assert T.get('a')[0] == False
  print(T)