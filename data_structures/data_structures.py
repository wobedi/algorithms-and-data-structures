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
        self.root = self._Node()
    
    class _Node:
        def __init__(self, key=None, value=None, left=None, right=None):
            self.key, self.value, self.left, self.right = key, value, left, right

    def put(self, key, value):
        if self.root.key == None:
            self.root.key, self.root.value = key, value  # more elegant way?
            return f"Put {key}:{value} at root"
        return self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node.key == key:
            node.value == value
            return f"Put {value} to existing key {key}"
        if node.key > key:
            if node.left is None:
                node.left = self._Node(key, value)
                return f"Created new node with {key}:{value} left of {node.key}"
            else:
                return self._put(node.left, key, value)
        if node.key < key:
            if node.right is None:
                node.right = self._Node(key, value)
                return f"Created new node with {key}:{value} right of {node.key}"
            else:
                return self._put(node.right, key, value)

    def get(self, key):
            return self._get(parent=None, node=self.root, key)

    def _get(self, parent, node, key):
        if node.key == key:
            print(f"Found key {key} with value {node.value} and parent {parent.key}")
            return node, parent
        elif node.key > key:
            if node.left is None:
                return f"Did not find any value for key {key}"
            else:
                return self._get(parent=node, node=node.left, key)
        elif node.key < key:
            if node.right is None:
                return f"Did not find any value for key {key}"
            else:
                return self._get(parent=node, node=node.right, key)

    def delete(self, key):
        pass

    def iterator(self):
        pass

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
    

class Node:
    def __init__(self, node_val=None, next_node=None):
        self.node_val = node_val
        self.next_node = None


class Stack_Singly_Linked_List:
    def __init__(self, init_val):
        self.head = Node(init_val, next_node=None)
        self.print_list()

    def push(self, new_val):
        new_node = Node(node_val=new_val)
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
    pass
