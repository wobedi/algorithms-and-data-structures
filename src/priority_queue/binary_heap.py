class BinaryHeap:
    """Implements https://en.wikipedia.org/wiki/Binary_heap
    Using positive keys -> max-heap, using negative keys -> min-heap.
    Keys must be comparable.
    """
    def __init__(self, keys=[]):
        self.keys = [None]
        self.keys.extend(keys) if keys else None
        self.heapify()

    def del_max(self):
        """Deletes the maximum value at the top of the heap and returns it"""
        if self.is_empty():
            return Exception("Error: Heap is empty")
        self._swap(1, self.size())
        val = self.keys.pop()
        self._sink(1)
        return val

    def heapify(self):
        """Turns a given array (if provided) into a 1-indexed binary heap"""
        if self.size() <= 1:
            return
        i = self.size() // 2  # first node from the end who has children
        while i > 0:
            self._sink(i)
            i -= 1
        return

    def insert(self, key):
        """Insert key while maintaining heap invariants"""
        self.keys.append(key)
        return self._swim(self.size())

    def is_empty(self):
        """Returns True if heap is empty, else False"""
        return len(self.keys) <= 1  # because keys[0] is empty

    def max(self):
        """Returns the maximum value at the top of the heap if there is one"""
        return self.keys[1] if len(self.keys) > 1 else None

    def size(self):
        """Returns the number of values stored ni the heap"""
        return len(self.keys) - 1  # -1 because keys[0] is empty

    def values(self):
        """Returns an iterable of all values in the heap"""
        return self.keys[1:]

    def _sink(self, i: int, stop=False):
        # Iteratively swaps a value with children values until
        # heap invariants are restored (opposite of self._swim()).
        # Optionally accepts an index at which to stop sinking (to support
        # heapsort)
        stop = stop or self.size() + 1
        while 2*i < stop:
            j = 2*i
            if j < stop - 1 and self.keys[j] < self.keys[j+1]:
                j += 1  # ensures that j is index of *larger* child node
            if self.keys[i] >= self.keys[j]:
                break
            self._swap(i, j)
            i = j
        return i

    def _swap(self, i, j):
        # Swaps two values/nodes
        self.keys[i], self.keys[j] = self.keys[j], self.keys[i]

    def _swim(self, i):
        # Iteratively swaps a value with parent values until
        # heap invariants are restored (opposite of self._sink()).
        parent_i = max(1, i // 2)  # parent = i//2 except for keys[1]
        if self.keys[parent_i] >= self.keys[i]:
            return i
        else:
            self._swap(parent_i, i)
            return self._swim(parent_i)


if __name__ == '__main__':
    keys = [1, 2, 3, 10, 34, 22, 14, 21, 0]
    keys_sorted = sorted(keys)

    # construction should work for empty and non-empty cases
    pq = BinaryHeap()
    pq2 = BinaryHeap(keys)

    # .size() and .is_empty() should work for empty and non-empty cases
    assert pq.size() == 0
    assert pq2.size() == len(keys)
    assert pq.is_empty() is True
    assert pq2.is_empty() is False

    # .max() should work for empty and non-empty cases
    assert pq.max() is None

    # .max() should still work after deletion
    # assert del_max(pq) to raise
    pq2.del_max()
    assert pq2.max() == keys_sorted[-2]
    pq2.del_max()
    assert pq2.max() == keys_sorted[-3]

    # .insert() should work, including subsequent deletions and max() queries
    for key in keys:
        pq.insert(key)
    assert pq.max() == keys_sorted[-1]
    pq.del_max()
    assert pq.max() == keys_sorted[-2]
    pq.del_max()
    assert pq.max() == keys_sorted[-3]
