from functools import reduce


class RWayTrie:
    """Implements an R-way trie with a default radix of 256 (extended ASCII)"""
    def __init__(self, radix=256):
        self.radix = radix
        self.root = _RWayTriNode(radix)

    def get(self, s: str):
        """Returns node.value if string s is in Trie, else False"""
        self._throw_if_out_of_radix(s)
        node = self.root
        for c in s:
            i = ord(c)    # Typecasts char to code_point:int representation
            if node.next[i] is None:
                print(f'Key "{s}" is NOT in trie')
                return False
            node = node.next[i]
        if node.value:
            print(f'Value at key "{s}" is {node.value}')
            return node.value
        print(f'Key "{s}" is NOT in trie')
        return False

    def put(self, s: str, value):
        """Inserts string s with value into Trie"""
        self._throw_if_out_of_radix(s)
        node = self.root
        for c in s:
            i = ord(c)
            if node.next[i] is None:
                node.next[i] = _RWayTriNode(self.radix)
            node = node.next[i]
        node.value = value
        print(f'UPSERTED Key "{s}" with value "{value}"')
        return

    def delete(self, s: str):
        """Deletes string s from Trie"""
        self._throw_if_out_of_radix(s)
        self._delete(s, 0, self.root)

    def longest_prefix_of(self, s: str) -> str:
        """Returns longest prefix of s in trie"""
        res = ''
        node = self.root
        for c in s:
            code = ord(c)
            if not node.next[code]:
                break
            res = res + c
            node = node.next[code]
        return res

    def keys(self, node=None) -> list:
        """Returns an iterable of all keys in trie"""
        res = []
        self._keys(node or self.root, '', res)
        return res

    def keys_with_prefix(self, p: str) -> list:
        """Returns all keys with prefix p that are in Trie"""
        node = self.root
        for c in p:
            code = ord(c)
            if not node.next[code]:
                print(f'Prefix {p} is not in Trie')
                return False
            node = node.next[code]
        return [p + s for s in self.keys(node)]

    def _delete(self, string: str, index: int, node):
        # Base condition I: reached end of string and am still in trie
        if index == len(string):
            node.value = None
            return self._none_if_node_is_null_else_node(node)

        next_index = ord(string[index])
        next_node = node.next[next_index]

        # Base condition II: trie ends but string has not yet ended
        if next_node is None:
            return f'Key "{string}" is NOT in trie'
        node.next[next_index] = self._delete(string, index + 1, next_node)
        return self._none_if_node_is_null_else_node(node)

    def _none_if_node_is_null_else_node(self, node):
        # Returns None if node is null, else returns node
        node_has_children = reduce(lambda a, b: b is not None, node.next, None)
        if not node_has_children and not node.value:
            return None
        return node

    def _keys(self, node, prefix: str, result: []):
        # Stores all keys that are children of node in result
        if node is None:
            return
        if node.value is not None:
            result.append(prefix)
        i = 0
        while i < self.radix:
            self._keys(node.next[i], prefix + chr(i), result)
            i += 1

    def _throw_if_out_of_radix(self, s: str):
        # Throws error if string s is out of radix or empty
        if len(s) < 1:
            raise ValueError('Please provide non-empty string')
        if not all(ord(c) < self.radix for c in s):
            raise ValueError(f'String "{s}" includes characters which '
                             f'encode to value outside of radix range'
                             f'{self.radix}')


class _RWayTriNode:
    """Implements a single node of an R-way trie"""
    def __init__(self, radix: int, value=None):
        self.next = [None for _ in range(radix)]
        self.value = value


if __name__ == '__main__':
    T = RWayTrie()
    TEST_STRINGS = ['appleE', 'donkey[]', 'garfield123', 'garfunkel']
    print(T)

    for s in TEST_STRINGS:
        T.put(s, s)

    for s in TEST_STRINGS:
        assert T.get(s) == s
    assert set(T.keys()) == {'appleE', 'donkey[]', 'garfield123', 'garfunkel'}
    assert T.longest_prefix_of('donkendonuTs') == 'donke'
    assert set(T.keys_with_prefix('garf')) == {'garfield123', 'garfunkel'}

    T.delete('appleE')
    assert T.get('appleE') is False

    assert set(T.keys()) == {'donkey[]', 'garfield123', 'garfunkel'}
    assert T.get('a') is False
    assert T.get('a') is False
    assert T.get('a') is False
