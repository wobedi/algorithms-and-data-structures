from .queue import Queue

class BinarySearchTree:
    """Implements https://en.wikipedia.org/wiki/Binary_search_tree"""    
    def __init__(self):
        self.root = None
        self.upserted_node = None

    class Node:
        def __init__(self, key, value, left=None, right=None):
            self.key, self.value, self.left, self.right = key, value, left, right

    def get(self, key):
        node = self._get(key)
        return node.value if node else False

    def _get(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
        return False

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        return self.upserted_node

    def _put(self, node, key, value):
        if node is None:
            self.upserted_node = self.Node(key, value)
            return self.upserted_node
        if key > node.key:
            node.right = self._put(node.right, key, value)
        elif key < node.key:
            node.left = self._put(node.left, key, value)
        elif key == node.key:
            node.value = value
            self.upserted_node = node
        return node

    def delete(self, key):
        if self.root is None:
            return False
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Implements Hibbard deletion""" 
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

    def del_min(self):
        if self.root is None:
            return False
        self.root = self._del_min(self.root)

    def _del_min(self, node):
        if node.left is None: 
            return node.right
        node.left = self._del_min(node.left)
        return node

    def min(self, node=None):
        node = node or self.root
        while True:
            if node.left is None:
                return node
            else: 
                node = node.left

    def max(self, node=None):
        node = node or self.root
        while True:
            if node.right is None:
                return node
            else: 
                node = node.right

    def is_empty(self, key):
        return self.root is not None

    def keys(self):
        q = Queue()
        self.traverse_inorder(self.root, q)
        return q

    def traverse_inorder(self, node, queue):
        if node is None: 
            return
        self.traverse_inorder(node.left, queue)
        queue.enqueue(node.key)
        self.traverse_inorder(node.right, queue)
