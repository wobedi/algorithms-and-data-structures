class BinarySearchTree:
    """Implements https://en.wikipedia.org/wiki/Binary_search_tree"""
    def __init__(self):
        self.root = None
        self.upserted_node = None

    def __str__(self):
        return str(self.keys())

    def get(self, key):
        """Returns value of key if key is in tree, else None"""
        node = self._get(key)
        return node.value if node else False

    def put(self, key, value) -> _BinaryNode:
        """Inserts key:value into tree, returns pointer to upserted node"""
        self.root = self._put(self.root, key, value)
        return self.upserted_node

    def delete(self, key) -> None | False:
        """Deletes key from tree. Returns None if successful, False if not."""
        if self.root is None:
            return False
        self.root = self._delete(self.root, key)

    def del_min(self):
        """Deletes the smallest key from the tree"""
        if self.root is None:
            return False
        self.root = self._del_min(self.root)

    def min(self, node=None) -> _BinaryNode | None:
        """Return node with smallest key, leveraging symmetric order of tree"""
        node = node or self.root
        while True:
            if node.left is None:
                return node
            else:
                node = node.left

    def max(self, node=None) -> _BinaryNode | None:
        """Returns node with largest key, leveraging symmetric order of tree"""
        node = node or self.root
        while True:
            if node.right is None:
                return node
            else:
                node = node.right

    def is_empty(self, key) -> bool:
        """Returns True if tree is empty, else False"""
        return self.root is not None

    def keys(self) -> list:
        """Returns an iterable of all keys of the tree"""
        q = []
        self.traverse(self.root, q, 'inorder')
        return q

    def traverse(self, node: _BinaryNode, queue: [], order: str):
        """Traverses the tree in pre-, in-, or postorder
        and stores value in queue
        """
        assert order in {'preorder', 'inorder', 'postorder'}
        if node is None:
            return
        queue.append(node.key) if order == 'preorder' else None
        self.traverse(node.left, queue, order)
        queue.append(node.key) if order == 'inorder' else None
        self.traverse(node.right, queue, order)
        queue.append(node.key) if order == 'postorder' else None

    def _get(self, key) -> _BinaryNode | False:
        # Iteratively search for key in tree
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
        return False

    def _put(self, node: _BinaryNode, key, value) -> _BinaryNode:
        # Recursively put key:value pair into tree
        if node is None:
            self.upserted_node = self._Node(key, value)
            return self.upserted_node
        if key > node.key:
            node.right = self._put(node.right, key, value)
        elif key < node.key:
            node.left = self._put(node.left, key, value)
        elif key == node.key:
            node.value = value
            self.upserted_node = node
        return node

    def _delete(self, node: _BinaryNode, key) -> _BinaryNode | None:
        """Implements
        https://en.wikipedia.org/wiki/Binary_search_tree#Deletion
        """
        if node is None:
            return None
        if key == node.key:
            if node.left is None and node.right is None:
                return None
            elif node.left is None and node.right is not None:
                return node.right
            elif node.left is not None and node.right is None:
                return node.left
            elif node.left is not None and node.right is not None:
                min_node = self.min(node.right)
                new_key, new_value = min_node.key, min_node.value
                node.right = self._del_min(node.right)
                node.key, node.value = new_key, new_value
        elif key > node.key:
            node.right = self._delete(node.right, key)
        elif key < node.key:
            node.left = self._delete(node.left, key)
        return node

    def _del_min(self, node: _BinaryNode) -> _BinaryNode:
        # Traverses tree to the left until leaf node is reached
        if node.left is None:
            return node.right
        node.left = self._del_min(node.left)
        return node


class _BinaryNode:
    """Implements a binary tree node"""
    def __init__(self, key, value,
                 left: _BinaryNode = None,
                 right: _BinaryNode = None):
        self.key, self.value = key, value
        self.left, self.right = left, right


if __name__ == '__main__':
    BST = BinarySearchTree()
    BST.put(7, 7)
    BST.put(4, 4)
    BST.put(3, 3)
    BST.put(5, 5)
    BST.put(10, 10)
    BST.put(8, 8)
    BST.put(12, 12)
    print(BST)
