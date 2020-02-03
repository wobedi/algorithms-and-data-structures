from functools import reduce

# TODO: Understand: Why does it work efficiently for 32 bit ints? 

class TernarySearchTrieNode:
  def __init__(self, char, value=None):
    self.c = char
    self.value = value
    self.left = self.down = self.right = None

  def __str__(self):
    # TODO might break if self.left/.down/.right are None
    return f'<Char: {self.c}; Value: {self.value}; Left: {self.left.c}; Down: {self.down.c}; Right: {self.right.c}>'


class TernarySearchTrie:
  # TODO (maybe): keys(), longestPrefix(s) and keysWithPrefix(s)?
  def __init__(self):
    self.root = None

  def get(self, string: str):
    return self._get(string, 0, self.root)

  def put(self, string: str, value):
    self.root = self._put(string, 0, value, self.root)

  def delete(self, string: str):
    self.root = self._delete(string, 0, self.root)

  def _get(self, string: str, index, node: TernarySearchTrieNode):
    c = string[index]
    if node is None:
      print(f'String {string} is not in Trie')
      return False
    if c < node.c:
      return self._get(string, index, node.left)
    elif c > node.c:
      return self._get(string, index, node.right)
    elif index < len(string) - 1:
      return self._get(string, index + 1, node.down)
    else:
      if node.value:
        print(f'String {string} is in Trie with value {node.value}')
        return True
      print(f'String {string} is not in Trie')
      return False

  def _put(self, string: str, index, value, node: TernarySearchTrieNode):  
    c = string[index]
    if node is None:
      node = TernarySearchTrieNode(c)
    if c < node.c:
      node.left = self._put(string, index, value, node.left)
    elif c > node.c:
      node.right = self._put(string, index, value, node.right)
    elif index < len(string) - 1:
      node.down = self._put(string, index + 1, value, node.down)
    else:
      node.value = value
    return node

  def _delete(self, string: str, index, node: TernarySearchTrieNode):
    c = string[index]
    if node is None:
      print(f'String {string} is not in Trie')
      return None
    if c < node.c:
      node.left = self._delete(string, index, node.left)
    elif c > node.c:
      node.right = self._delete(string, index, node.right)
    elif index < len(string) - 1:
      node.down = self._delete(string, index + 1, node.down)
    else: 
      node.value = None
    return (None if not node.left and not node.down and not node.right else node)


class RWayTriNode:
  def __init__(self, radix: int, value=None):
    self.next = [None for _ in range(radix)]
    self.value = value


class RWayTrie:
  """Implements an R-Way trie that defaults to a radix of 256 (extended ASCII)"""
  def __init__(self, radix=256):
    self.radix = radix
    self.root = RWayTriNode(radix)

  def keys(self, node=None):
    res = []
    self._keys(node or self.root, '', res)
    return res

  def longest_prefix_of(self, s: str):
    # TODO only if value present?
    res = ''
    node = self.root
    for c in s:
      code = ord(c)
      if not node.next[code]:
        break
      res = res + c
      node = node.next[code]
    return res

  def keys_with_prefix(self, p: str):
    node = self.root
    for c in p:
      code = ord(c)
      if not node.next[code]:
        print(f'Prefix {p} is not in Trie')
        return False
      node = node.next[code]
    return [p + s for s in self.keys(node)]
    
  def get(self, string: str):
    self._throw_if_out_of_radix(string)
    node = self.root
    for c in string:
      i = ord(c)  # typecasts char to int representation
      if node.next[i] is None:
        return False, f'Key "{string}" is NOT in trie'
      node = node.next[i]
    if node.value:
      return True, f'Value at key "{string}" is {node.value}'
    return False, f'Key "{string}" is NOT in trie'

  def put(self, string: str, value):
    self._throw_if_out_of_radix(string)
    node = self.root
    for c in string:
      i = ord(c)
      if node.next[i] is None:
        node.next[i] = RWayTriNode(self.radix)
      node = node.next[i]
    node.value = value
    return f'UPSERTED Key "{string}" with value "{value}"'
    
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

  def _none_if_node_is_null_else_node(self, node: RWayTriNode):
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

  def _keys(self, node: RWayTriNode, prefix, result):
    if node is None:
      return
    if node.value is not None:
      result.append(prefix)
    i = 0
    while i < self.radix:
      self._keys(node.next[i], prefix + chr(i), result)
      i += 1
    
      
if __name__ == '__main__':
  T = RWayTrie()
  TEST_STRINGS = ['appleE', "donkey'][]", "garfield123", "garfunkel"]
  print(T)
  T.get('a')
  for s in TEST_STRINGS:
    T.put(s, s)
  for s in TEST_STRINGS:
    assert T.get(s)[0] == True
  assert set(T.keys()) == {'appleE', "donkey'][]", "garfield123", "garfunkel"}
  assert T.longest_prefix_of('donkendonuTs') == 'donke'
  assert set(T.keys_with_prefix('garf')) == {"garfield123", "garfunkel"} 
  T.delete('appleE')
  assert T.get('appleE')[0] == False
  assert set(T.keys()) == {"donkey'][]", "garfield123", "garfunkel"}
  assert T.get('a')[0] == False
  assert T.get('a')[0] == False
  assert T.get('a')[0] == False
  print(T)

# if __name__ == '__main__':
#   T = TernarySearchTrie()
#   print(T)
#   assert T.get('a') == False
#   TEST_STRINGS = ['appleE', "donkey'][]", "donner", "garfield123", "garfunkel"]
#   for i, s in enumerate(TEST_STRINGS):
#     T.put(s, i + 1)
#   assert T.get('a') == False
#   for s in TEST_STRINGS:
#     assert T.get(s) == True
#   T.delete('garfield123')
#   assert T.get('garfield123') == False
#   assert T.get("garfunkel") == True
#   assert T.get('a') == False
#   print(T)

# <__main__.TernarySearchTrie object at 0x7fcbdd062b10>
# String a is not in Trie
# String a is not in Trie
# String appleE is in Trie with value 1
# String donkey'][] is in Trie with value 2
# <__main__.TernarySearchTrie object at 0x7fcbdd062b10>
# String a is not in Trie
# String a is not in Trie
# String appleE is in Trie with value 1
# String donkey'][] is in Trie with value 2
# String donner is in Trie with value 3
# String garfield123 is in Trie with value 4
# String garfunkel is in Trie with value 5
# String garfield123 is not in Trie
# String garfunkel is in Trie with value 5
# String a is not in Trie
# <__main__.TernarySearchTrie object at 0x7fcbdd062b10>
# String donner is in Trie with value 3
# String garfield123 is in Trie with value 4
# String garfunkel is in Trie with value 5
# String garfield123 is not in Trie
# String garfunkel is in Trie with value 5
# String a is not in Trie
# <__main__.TernarySearchTrie object at 0x7fcbdd062b10>