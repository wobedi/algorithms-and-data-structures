def _input_validation(func):
    """Wrapper that ensures that terminal char is not in pattern.
    Only works for unary functions whose single argument is pattern.
    """
    def wrapped_input_validation(self, pattern: str):
        if self.terminal_char in pattern:
            raise Exception(f'Terminal_char {self.terminal_char}'
                            f'must not be in input pattern')
        return func(self, pattern)
    return wrapped_input_validation


class SuffixTrie:
    """Implements a suffix trie that enables O(L) substring search
    where L is the length of the substring.
    Currently only supports one single contiguous string,
    not a collection of strings (non-generalized).
    """
    def __init__(self, string: str, terminal_char='$'):
        """Simple construction in O(N²).
        More efficient constructions algorithms (e.g. Ukkonen's) possible.
        A suffix trie uses O(N²) space (whereas a suffix tree uses O(N))
        """
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
        # Inserts suffixes as part of the construction of the trie
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
        # Counter is wrapped in list to pass by reference rather than by value
        return self._dfs(node, [0])

    @_input_validation
    def is_suffix_of_T(self, pattern: str) -> bool:
        """Returns True if pattern is a suffix of self.T, else False"""
        node = self._find_last_node_of(pattern)
        if not node:
            return False
        return self.terminal_char in node

    def _dfs(self, node: {}, count: [int]) -> int:
        # Depth-first search for a node, counting its number of occurrences
        if self.terminal_char in node:
            count[0] += 1
        for (_, child) in node.items():
            self._dfs(child, count)
        return count[0]

    @_input_validation
    def _find_last_node_of(self, pattern: str) -> {}:
        # Returns a pointer to the last node of a pattern (if possible)
        node = self.root
        for c in pattern:
            if c not in node:
                return None
            node = node[c]
        return node


if __name__ == '__main__':
    STrie = SuffixTrie('abcdefghijklmnopqrstuvwxyznopqn'
                       'opqfghijklmnobcdefepoqijrmnopqrsoiweroiwn')
    print(STrie)
    pattern_list = ['opq', 'abc', 'oiwn', 'mnopqrsoiweroiwn', 'fg']

    for pattern in pattern_list:
        print(f'Pattern {pattern} appears {STrie.count(pattern)} times in T')
        print(f'Pattern {pattern} is a suffix of T:'
              f'{STrie.is_suffix_of_T(pattern)}')
