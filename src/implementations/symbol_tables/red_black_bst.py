class _RBNode:
    """Implements a Binary Node with additional color bit"""
    def __init__(self, key, value, isRed, left=None, right=None):
        self.key, self.value = key, value
        self.left, self.right = left, right
        self.isRed = isRed


class RedBlackTree:
    """Implements https://en.wikipedia.org/wiki/Red%E2%80%93black_tree"""
    def __init__(self):
        self.root = None

    def get(self, key):
        """Returns value of key if key in tree, else False"""
        node = self._get(self.root, key)
        return (node.value if node else None)

    def put(self, key, value):
        """Upserts key:value into tree"""
        self.root = self._put(self.root, key, value)
        self.root.isRed = False

    def delete(self, key):
        """Currently not implemented"""
        pass

    def _get(self, node: _RBNode, key) -> _RBNode or None:
        # Iteratively traverse tree in search of key
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
        return None

    def _put(self, node: _RBNode, key, value) -> _RBNode:
        """Recursively upsert key:value
        while maintaining Red-black RBT invariants.
        """
        if node is None:
            return _RBNode(key, value, isRed=True)
        elif key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)

        # Maintaining invariants:
        # 1. Rotate left if node has a right-leaning red link
        if (node.right and node.right.isRed
                and (node.left is None or node.left.isRed is False)):
            node = self._rotate_left(node)
        # 2. Rotate right if node has red child link and a red grandchild link
        if (node.left and node.left.left
                and node.left.isRed and node.left.left.isRed):
            node = self._rotate_right(node)
        # 3. Color-flip if node has two red children links
        if (node.left and node.left.isRed
                and node.right and node.right.isRed):
            self._flip_colors(node)
        return node

    def _rotate_left(self, parent: _RBNode) -> _RBNode:
        # Fixes right-leaning red link to maintain the following invariant:
        # No right-leaning red links
        assert parent.right.isRed is True
        assert parent.left is None or parent.left.isRed is False
        new_parent = parent.right
        parent.right = new_parent.left
        new_parent.left = parent
        new_parent.isRed = parent.isRed
        parent.isRed = True
        return new_parent

    def _rotate_right(self, parent: _RBNode) -> _RBNode:
        # Fixes two red links in a row to maintain the following invariant:
        # Perfect black balance (same black link distance to all leaves)
        assert parent.left.isRed is True
        new_parent = parent.left
        parent.left = new_parent.right
        new_parent.right = parent
        new_parent.isRed = parent.isRed
        parent.isRed = True
        return new_parent

    def _flip_colors(self, parent: _RBNode):
        # Fixes parent with two red child links to maintain the invariant:
        # Not more than two keys per (implicit) 2-3 node
        assert parent.left.isRed == parent.right.isRed is True
        parent.left.isRed = parent.right.isRed = False
        parent.isRed = True
        return


if __name__ == '__main__':
    RBT = RedBlackTree()
    test_items = [
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4],
        [5, 5],
        [12, 12]
    ]

    # .get() should work if RBT is empty
    for key, _ in test_items:
        assert RBT.get(key) is None

    # .put() should work, .get() should work if RBT has items
    for key, value in test_items:
        assert RBT.get(key) is None
        RBT.put(key, value)
        assert RBT.get(key) == value

    # subsequent puts should override previous puts
    RBT.put(1, 1)
    RBT.put(1, 2)
    assert RBT.get(1) == 2
