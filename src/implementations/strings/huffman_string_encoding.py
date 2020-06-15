import heapq
from collections import defaultdict
from functools import total_ordering


def huffman_encode_into_trie(s: str):
    """Implements https://en.wikipedia.org/wiki/Huffman_coding"""
    count = defaultdict(int)
    for char in s:
        count[char] += 1

    pq = []
    for char, char_count in count.items():
        heapq.heappush(pq, _BinaryNode(char, char_count))

    root = None
    while len(pq) > 1:
        smallest = heapq.heappop(pq)
        second_smallest = heapq.heappop(pq)
        combined_weight = smallest.weight + second_smallest.weight
        parent = _BinaryNode(None, combined_weight, smallest, second_smallest)
        heapq.heappush(pq, parent)
        root = parent

    # Returning pointer to root of resulting trie
    return root


@total_ordering
class _BinaryNode:
    """Implements a binary search trie node"""
    def __init__(self, char: str, weight: int,
                 zero=None,
                 one=None):
        self.char = char
        self.weight = weight
        self.zero: self = zero
        self.one: self = one

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight


if __name__ == '__main__':
    # This test is a bit brittle but it does the job
    s = 'asasuihhaosiaowasoihaaoaisaoiuhoiuhowp'
    root = huffman_encode_into_trie(s)
    expected_codes = [('a', '01'), ('o', '00'), ('i', '111'),
                      ('s', '100'), ('h', '101'), ('u', '1100'),
                      ('w', '11011'), ('p', '11010')]

    for code in expected_codes:
        steps = code[1]
        node = root
        for step in steps:
            if step == '0':
                assert node.zero
                node = node.zero
            else:
                assert node.one
                node = node.one
        assert node.char == code[0]
        assert node.zero is None and node.one is None
        print(f'Char "{node.char}" has weight {node.weight} and code: {steps}')
