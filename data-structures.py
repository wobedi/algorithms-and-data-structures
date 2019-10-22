#test1

class BinaryHeap:
    def __init__(self, keys=[]):
        self.keys = []
        self.keys[1:] = sorted(keys reverse=True)  # heapify

    def change_key(self, i, key):
        self.keys[i] = key
        i = self._swim(i)
        i = self._sink(i)
        return i

    def del_max(self):
        self._swap(1, self.size())
        self._sink(1)
        return self.keys.pop()

    def insert(self, key):
        self.keys.append(key)
        return self._swim(self.size())

    def is_empty(self):
        return len(self.keys) <= 1  # bc keys[0] is empty

    def max(self):
        return self.keys[1]

    def size(self):
        return len(self.keys) - 1  # bc keys[0] is empty

    def _sink(self, i):
        child1, child2 = self.keys[i*2], self.keys[i*2+1]
        if child1 <= self.keys[i] and child2 <= self.keys[i]:
            return i
        elif child1 >= child2:
            self._swap(i, i*2)
            return self._sink(i*2)
        elif child1 < child2:
            self._swap(i, i*2+1)
            return self._sink(i*2+1)

    def _swim(self, i):
        parent_i = max(1, i // 2)  # parent = i//2 except for keys[1]
        if self.keys[parent_i] >= self.keys[i]:
            return i
        else:
            self._swap(parent_i, i)
            return self._swim(parent_i)

    def _swap(self, i2, i2):
        self.keys[i1], self.keys[i2] = self.keys[i2], self.keys[i1]


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

            # test 2
            # test 3

if __name__ == '__main__':
    client()   
