class RedBlackTree:
    """Implements https://en.wikipedia.org/wiki/Red%E2%80%93black_tree"""
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, key, value, isRed, left=None, right=None):
            self.key, self.value = key, value
            self.left, self.right, self.isRed = left, right, isRed

    def get(self, key):
        node = self._get(self.root, key)
        return node.value if node else False

    def _get(self, node, key):
        # TODO Same as vanilla BST. Inherit/compose instead?
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
        return False

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.isRed = False

    def _put(self, node, key, value):
        if node is None:
            return self.Node(key, value, isRed=True)
        elif key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        
        if (node.right and node.right.isRed 
                and (node.left is None or node.left.isRed == False)):
            node = self._rotate_left(node)
        if (node.left and node.left.left
                and node.left.isRed and node.left.left.isRed):
            node = self._rotate_right(node)
        if (node.left and node.left.isRed
                and node.right and node.right.isRed):
            self._flip_colors(node)

        return node

    def _delete(self, key):
        """Currently not implemented"""
        pass

    def _rotate_left(self, parent):
        assert parent.right.isRed == True
        assert parent.left is None or parent.left.isRed == False
        new_parent = parent.right
        parent.right = new_parent.left
        new_parent.left = parent
        new_parent.isRed = parent.isRed
        parent.isRed = True
        return new_parent

    def _rotate_right(self, parent):
        assert parent.left.isRed == True
        new_parent = parent.left
        parent.left = new_parent.right
        new_parent.right = parent
        new_parent.isRed = parent.isRed
        parent.isRed = True
        return new_parent 

    def _flip_colors(self, parent):
        assert parent.left.isRed == parent.right.isRed == True
        parent.left.isRed = parent.right.isRed = False
        parent.isRed = True
        return
