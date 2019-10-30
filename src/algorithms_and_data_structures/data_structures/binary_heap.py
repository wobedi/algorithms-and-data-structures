class BinaryHeap:
    """Implements https://en.wikipedia.org/wiki/Binary_heap"""
    # TODO currently only works for keys of ints
    # TODO currently only max binary heap, not min binary heap
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
