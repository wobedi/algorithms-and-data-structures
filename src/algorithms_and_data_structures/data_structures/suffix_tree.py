

def _input_validation(func):
    def wrapped_input_validation(self, pattern):
      if self.terminal_char in pattern:
        raise f'Terminal_char {self.terminal_char} must not be in input pattern'
      return func(self, pattern)
    return wrapped_input_validation


class SuffixTrie:
  """ Implements a suffix trie that enables O(L) substring search where L is the length of the substring
      Currently only supports one single contiguous string, not a collection of strings (non-generalized)."""
  def __init__(self, string: str, terminal_char='$'):
    """ Simple construction in O(N²). More efficient constructions algorithms possible.
        A suffix trie uses O(N²) space (whereas a suffix tree uses O(N))"""
    self.root = {}
    self.string = string
    self.terminal_char = terminal_char
    if terminal_char in string:
      raise f'Terminal_char {self.terminal_char} must not be in text'
    offset = 0
    while offset < len(string):
      self._insert(string[offset:], offset)    
      offset += 1

  def __str__(self):
    offset = 0
    res = ''
    while offset < len(self.string):
      res += '\n' + offset*' ' + self.string[offset:]
      offset += 1
    return res

  def _insert(self, suffix: str, offset: int):
    index = 0
    node = self.root
    while index < len(suffix):
      char = suffix[index]
      if char not in node:
        node[char] = {}
      node = node[char]
      index += 1
    node[self.terminal_char] = {}

  @_input_validation
  def count(self, pattern: str) -> int:
    """Returns the number of times a pattern p appears in text self.T"""
    node = self._find_last_node_of(pattern)
    if not node:
      return 0
    return self._dfs(node, [0])

  def _dfs(self, node: {}, count):
    if self.terminal_char in node:
      count[0] += 1
    for (_, child) in node.items():
      self._dfs(child, count)
    return count[0]

  @_input_validation
  def is_suffix_of_T(self, pattern: str) -> bool:
    """Returns True if pattern is a suffix of self.T, else False"""
    node = self._find_last_node_of(pattern)
    if not node:
      return False
    return self.terminal_char in node

  @_input_validation
  def _find_last_node_of(self, pattern: str) -> {}:
    node = self.root
    for c in pattern:
      if c not in node: 
        return None
      node = node[c]
    return node

  
if __name__ == '__main__':
  STrie = SuffixTrie('abcdefghijklmnopqrstuvwxyznopqnopqfghijklmnobcdefepoqijrmnopqrsoiweroiwn')
  print(STrie)
  pattern_list = ['opq', 'abc', 'oiwn', 'mnopqrsoiweroiwn', 'fg']
  for pattern in pattern_list:
    print(f'Pattern {pattern} appears {STrie.count(pattern)} times in T')
    print(f'Pattern {pattern} is a suffix of T: {STrie.is_suffix_of_T(pattern)}')
  # STrie.count('werewrew!$er')
  # STrie = SuffixTrie('werewrew!$er')

# class SuffixEdge:
#   def __init__(self, offset: int, length: int):
#     self.offset = offset
#     self.length = length
#     self.next = {}


# class SuffixTree:
#   """ Implements a suffix trie that enables O(L) substring search where L is the length of the substring
#       Currently only supports one single contiguous string, not a collection of strings (non-generalized)."""
#   def __init__(self, string: str, terminal_char='$', suffix_trie=None):
#     """ Simple construction in O(N²). Ukkonen's algorithm would enable construction in O(N)
#         A suffix tree uses O(N) space (whereas a suffix trie uses O(N²))"""
#     self.root: dict(SuffixEdge) = {}  # keys = first chars
#     self.terminal_char = terminal_char
#     self.string = string
#     if suffix_trie:
#       self.construct_via_suffix_trie(suffix_trie)
#     else:
#       self.construct_from_scratch()

#   def construct_via_suffix_trie(self, suffix_trie: SuffixTrie):
#     pass
#     # node = suffix_trie.root
#     # dfs
#     # stack chars
#     # as you pop, store in reverse until you hit branching one, append it there
#     # ...

#   def construct_from_scratch(self):
#     for offset in range(0, len(self.string)):
#       node = self.root
#       for index, char in enumerate(self.string[offset:]):
#         edge = node.get(char, None)
#         # case 0: add when its not there
#         if not edge:
#           node[char] = SuffixEdge(offset + index)
        
#         # case 1: stretch when it's there but not single
#         if edge.length > 1:
#           for i in range(edge.length)

        
#         # case 2: traverse if its there and single
        

#   def count(self, pattern: str) -> int:
#     """Returns the number of times a pattern p appears in text self.T"""
#     pass

#   def occurrences(self, pattern: str) -> [int]:
#     """Returns all occurrences of pattern p in self.T by their offset"""
#     pass

#   def is_suffix_of_T(self, pattern: str) -> bool:
#     """Returns True if pattern is a suffix of self.T, else False"""
#     pass

