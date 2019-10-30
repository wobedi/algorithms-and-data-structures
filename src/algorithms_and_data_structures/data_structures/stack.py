class Stack:
    class StackArray:
        """Implements
        https://en.wikipedia.org/wiki/Stack_(abstract_data_type)#Array
        """
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
    
    class StackSinglyLinkedList:
        """Implements 
        https://en.wikipedia.org/wiki/Stack_(abstract_data_type)#Linked_list
        """
        def __init__(self, init_value):
            self.head = self.Node(init_value, next_node=None)
            self.print_list()

        class Node:
            def __init__(self, value=None, next_node=None):
                self.value = value
                self.next_node = None

        def push(self, new_val):
            new_node = self.Node(value=new_val)
            new_node.next_node = self.head
            self.head = new_node

        def pop(self):
            self.head = (self.head.next_node
                        if self.head and self.head.next_node else None)

        def print_list(self):
            print(self.head.value 
                  if self.head and self.head.value else None)
            next_node = (self.head.next_node
                         if self.head and self.head.next_node else None)
            while True:
                if next_node == None: 
                        break
                print(next_node.value)
                next_node = next_node.next_node
