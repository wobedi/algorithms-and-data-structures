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
    client()   
