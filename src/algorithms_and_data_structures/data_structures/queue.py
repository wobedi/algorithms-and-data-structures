class Queue:
    """Implements https://en.wikipedia.org/wiki/Queue_(abstract_data_type)"""
    def __init__(self):
        self.q = []

    def enqueue(self, key):
        self.q.append(key)
        return len(self.q)-1

    def dequeue(self):
        return self.q.pop(0)
