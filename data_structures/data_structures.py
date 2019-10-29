# Implement comparable abstraction to make structs and sorts type-independent?

class BinaryHeap:
    # currently only works for keys of ints
    # currently only max binary heap, not min binary heap
    def __init__(self, keys=[]):
        self.keys = [None]
        self.keys[1:] = keys
        self.heapify()

    def change_key(self, i, key):
        if not 1 <= i <= self.size():
            return Exception(f"index {i} is out of range [1,{self.size()}]")
        self.keys[i] = key
        i = self._swim(i)
        i = self._sink(i)
        return i

    def del_max(self):
        if self.is_empty():
            return Exception("Error: Heap is empty")
        self._swap(1, self.size())
        val = self.keys.pop()
        self._sink(1)
        return val 

    def heapify(self):
        # in-place, bottom-up
        # TODO needs testing
        if self.size() <= 1:
            return
        i = self.size()  // 2  # first node from the end who has children
        while i > 0:
            self._sink(i)
            i -= 1
        return

    def heap_sort(self):
        # TODO move to array_sort module?
        # TODO needs testing
        i = self.size()
        while i > 0:
            self._swap(1, i)
            self._sink(1)
            i -= 1
        return

    def insert(self, key):
        self.keys.append(key)
        return self._swim(self.size())

    def is_empty(self):
        return len(self.keys) <= 1  # bc keys[0] is empty

    def max(self):
        return self.keys[1] if self.keys[1] else None

    def remove_key(self, i):
        if not 1 <= i <= self.size():
            return Exception(f"index {i} is out of range [1,{self.size()}]")
        self._swap(i, self.size())
        val = self.keys.pop()
        self._swim(i)
        self._sink(i)
        return val

    def size(self):
        return len(self.keys) - 1  # bc keys[0] is empty

    def _sink(self, i):
        while 2*i <= self.size():
            j = 2*i
            if j < self.size() and self.keys[j] < self.keys[j+1]:
                j += 1  # ensures that j is index of *larger* child node
            if self.keys[i] >= self.keys[j]:
                break
            self._swap(i, j)
            i = j
        return i

    def _swap(self, i1, i2):
        self.keys[i1], self.keys[i2] = self.keys[i2], self.keys[i1]

    def _swim(self, i):
        parent_i = max(1, i // 2)  # parent = i//2 except for keys[1]
        if self.keys[parent_i] >= self.keys[i]:
            return i
        else:
            self._swap(parent_i, i)
            return self._swim(parent_i)

class BinarySearchTree:    
    def __init__(self):
        self.root = None
        self.upserted_node = None

    class Node:
        def __init__(self, key, value, left=None, right=None):
            self.key, self.value, self.left, self.right = key, value, left, right

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

    def del_min(self):
        if self.root is None:
            return False
        self.root = self._del_min(self.root)

    def _del_min(self, node):
        if node.left is None: 
            return node.right
        node.left = self._del_min(node.left)
        return node

    def delete(self, key):
        if self.root is None:
            return False
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # Hibbard deletion 
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

    def find(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
        return False

    def get(self, key):
        node = self.find(key)
        return node.value if node else False

    def max(self, node=None):
        node = node or self.root
        while True:
            if node.right is None:
                return node
            else: 
                node = node.right

    def min(self, node=None):
        node = node or self.root
        while True:
            if node.left is None:
                return node
            else: 
                node = node.left

    def is_empty(self, key):
        return self.root is not None

    def size(self, key):
        pass

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

class RedBlackTree:
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
        # TODO Same as vanilla BST. Inherit/Compose instead?
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
        self.root.isRed = False  # is there a more elegant way?

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

    def delete(self, key):
        # TODO
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


class Stack_Array:
    def __init__(self):
        self.a = []

    def push(self, el):
        return self.a.append(el)

    def pop(self):
        return self.a.pop()

    def is_empty(self):
        return len(self.a) > 0

    def size(self):
        return len(self.a)


class Stack_Singly_Linked_List:
    def __init__(self, init_val):
        self.head = self.Node(init_val, next_node=None)
        self.print_list()

    class Node:
        def __init__(self, node_val=None, next_node=None):
            self.node_val = node_val
            self.next_node = None

    def push(self, new_val):
        new_node = self.Node(node_val=new_val)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        self.head = self.head.next_node if self.head and self.head.next_node else None

    def print_list(self):
        print(self.head.node_val) if self.head and self.head.node_val else print(None)
        next_node = self.head.next_node if self.head and self.head.next_node else None
        while True:
            if next_node == None: 
                    break
            print(next_node.node_val)
            next_node = next_node.next_node

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, key):
        self.q.append(key)
        return len(self.q)-1

    def dequeue(self):
        return self.q.pop(0)


def client():
    init_val = input("First value of Stack: ")
    SLL = Stack_Singly_Linked_List(init_val)

    while(True):
        action = input("What do you want to do? ")
        if action == "push":
            value = input("Which value? ")
            SLL.push(value)
            SLL.print_list()
        elif action == "pop":
            SLL.pop()
            SLL.print_list()
        else:
            print("Error, please choose push or pop")

if __name__ == '__main__':
    BST = RedBlackTree()
    print(BST.put(1,1))
    print(BST.put(5,5))
    print(BST.put(3,3))
    print(BST.put(0.5,0.5))
    print(BST.put(2,2))
