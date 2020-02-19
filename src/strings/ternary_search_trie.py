class TernarySearchTrie:
    """Implements https://en.wikipedia.org/wiki/Ternary_search_tree"""
    def __init__(self):
        self.root = None

    def get(self, s: str) -> bool:
        """Return True if string s is in trie, else False"""
        return self._get(s, 0, self.root)

    def put(self, s: str, label):
        """Upsert string s into trie"""
        self.root = self._put(s, 0, label, self.root)

    def delete(self, s: str):
        """Delete string s from trie"""
        self.root = self._delete(s, 0, self.root)

    def _get(self, s: str, i: int, node: _TernarySearchTrieNode):
        """Recursively traverse trie to find string s"""
        c = s[i]
        if node is None:
            print(f'String {s} is not in trie')
            return False

        if c < node.c:
            return self._get(s, i, node.left)
        elif c > node.c:
            return self._get(s, i, node.right)
        elif i < len(s) - 1:
            return self._get(s, i + 1, node.down)
        else:
            if node.label:
                print(f'String {s} is in trie with label {node.label}')
                return True
            print(f'String {s} is not in trie')
            return False

    def _put(self, s: str, i: int, label, node: _TernarySearchTrieNode):
        """Recursively upsert string s with label into trie"""
        c = s[i]
        if node is None:
            node = _TernarySearchTrieNode(c)

        if c < node.c:
            node.left = self._put(s, i, label, node.left)
        elif c > node.c:
            node.right = self._put(s, i, label, node.right)
        elif i < len(s) - 1:
            node.down = self._put(s, i + 1, label, node.down)
        else:
            node.label = label

        return node

    def _delete(self, s: str, i: int, node: _TernarySearchTrieNode):
        """Recursively delete string s from trie, including cleaning up trie"""
        c = s[i]
        if node is None:
            print(f'String {s} is not in trie')
            return None

        if c < node.c:
            node.left = self._delete(s, i, node.left)
        elif c > node.c:
            node.right = self._delete(s, i, node.right)
        elif i < len(s) - 1:
            node.down = self._delete(s, i + 1, node.down)
        else:
            node.label = None

        return (None
                if not node.left and not node.down and not node.right
                else node)


class _TernarySearchTrieNode:
    """Implements a TST node, storing a char, a label and three pointers"""
    def __init__(self, c: str, label=None):
        self.c = c
        self.label = label
        self.left = self.down = self.right = None


if __name__ == '__main__':
    T = TernarySearchTrie()
    print(T)
    assert T.get('a') is False
    TEST_STRINGS = ['appleE', "donkey'][]", 'donner',
                    'garfield123', 'garfunkel']
    for i, s in enumerate(TEST_STRINGS):
        T.put(s, i + 1)
    assert T.get('a') is False
    for s in TEST_STRINGS:
        assert T.get(s) is True
    T.delete('garfield123')
    assert T.get('garfield123') is False
    assert T.get("garfunkel") is True
    assert T.get('a') is False
    print(T)

# <__main__.TernarySearchTrie object at 0x7fcbdd062b10>
# String a is not in Trie
# String a is not in Trie
# String appleE is in Trie with label 1
# String donkey'][] is in Trie with label 2
# <__main__.TernarySearchTrie object at 0x7fcbdd062b10>
# String a is not in Trie
# String a is not in Trie
# String appleE is in Trie with label 1
# String donkey'][] is in Trie with label 2
# String donner is in Trie with label 3
# String garfield123 is in Trie with label 4
# String garfunkel is in Trie with label 5
# String garfield123 is not in Trie
# String garfunkel is in Trie with label 5
# String a is not in Trie
# <__main__.TernarySearchTrie object at 0x7fcbdd062b10>
# String donner is in Trie with label 3
# String garfield123 is in Trie with label 4
# String garfunkel is in Trie with label 5
# String garfield123 is not in Trie
# String garfunkel is in Trie with label 5
# String a is not in Trie
# <__main__.TernarySearchTrie object at 0x7fcbdd062b10>
