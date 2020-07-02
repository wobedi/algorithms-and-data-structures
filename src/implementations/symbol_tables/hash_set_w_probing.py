from src.implementations.symbol_tables import config


class HashSet:
    """Implements https://en.wikipedia.org/wiki/Hash_table#Sets,
    using https://en.wikipedia.org/wiki/Linear_probing
    for collision resolution
    """
    def __init__(self, size):
        self.size = size
        self.set = [None for i in range(size)]
        self.load = 0

    def contains(self, key) -> bool:
        """Returns True if key is in hash set, else False"""
        return self._linear_probing(key)[0]

    def put(self, key):
        """Inserts key into hash set"""
        key_in_set, index = self._linear_probing(key)
        if key_in_set:
            return f'Insertion error: Key {key} is already in hash set'
        self.set[index] = key
        self.load += 1
        if self.load / self.size >= config.probing['LOAD_FACTOR_MAX']:
            self._upsize()
        return

    def delete(self, key):
        """Deletes key from hash set"""
        key_in_set, i = self._linear_probing(key)
        if not key_in_set:
            return f'Deletion error: Key {key} is NOT part of this hash set'
        self.set[i] = None
        self.load -= 1

        # Moving subsequent items backwards to not break linear probing
        if not self.set[(i + len(self.set) - 1) % len(self.set)] is None:
            next = i + 1
            while self.set[next % self.size] is not None:  # Wrap around
                self.set[i], self.set[next] = self.set[next], self.set[i]
                i += 1
                next += 1

        if self.load / self.size < config.probing['LOAD_FACTOR_MIN']:
            self._downsize()
        return

    def _linear_probing(self, key, set_=None) -> bool or int:
        """Linear probing for key through hash set.
        Returns tuple:
        (True, index) for search hits at index,
        (False, index) for search misses;
        where index is the final index checked/first index with key==None
        """
        set_ = set_ or self.set
        index = self._modular_hash(key)  # Entry point for linear probing
        while set_[index] is not None:
            if index >= self.size:  # Wrap around
                index = 0
            if set_[index] == key:
                return (True, index)
            index += 1
        return (False, index)

    def _modular_hash(self, key) -> int:
        # Hashing key and using modulo operator to wrap it into self.size
        return hash(key) % self.size

    def _downsize(self):
        # Downsize underlying array (allocate less memory)
        return self._resize(config.probing['DOWNSIZE_FACTOR'])

    def _upsize(self):
        # Upsize underlying array (allocate more memory)
        return self._resize(config.probing['UPSIZE_FACTOR'])

    def _resize(self, factor: float):
        # Resize underlying array by factor:float
        self.size = int(self.size * factor)
        new_set = [None for i in range(self.size)]
        for key in self.set:
            if key is None:
                continue
            key_in_set, index = self._linear_probing(key, new_set)
            if key_in_set:
                return 'Syntax Error while resizing'
            new_set[index] = key
        self.set = new_set
        return


# Turn this into a unit test
if __name__ == '__main__':
    initial_size = 5
    HS = HashSet(initial_size)
    test_items = [1, 2, 3, 4, 5, 12]

    # .contains() should work if HS is empty
    for key in test_items:
        assert HS.contains(key) is False

    # .put() should work, .contains() should work if HS has items
    for key in test_items:
        assert HS.contains(key) is False
        HS.put(key)
        assert HS.contains(key) is True

    # delete() should work, .contains() should work after items deletion
    for key in test_items:
        assert HS.contains(key) is True
        HS.delete(key)
        assert HS.contains(key) is False

    # puts should be idempotent
    HS.put(1)
    HS.put(1)
    assert HS.contains(1) is True

    # upsize should work
    HS2 = HashSet(initial_size)
    assert len(test_items) > initial_size
    assert len(test_items) < initial_size * config.probing['UPSIZE_FACTOR']

    added_items_counter = 0
    while HS2.load / initial_size < config.probing['LOAD_FACTOR_MAX']:
        key = test_items[added_items_counter]
        HS2.put(key)
        added_items_counter += 1

    assert HS2.load == added_items_counter
    assert HS2.size == len(HS2.set)
    assert HS2.size == initial_size * config.probing['UPSIZE_FACTOR']

    # downsize should work
    old_size = HS2.size
    old_load = HS2.load
    deleted_items_counter = 0
    while HS2.load / old_size > config.probing['LOAD_FACTOR_MIN']:
        key = test_items[deleted_items_counter]
        HS2.delete(key)
        deleted_items_counter += 1

    assert HS2.load == old_load - deleted_items_counter
    assert HS2.size == len(HS2.set)
    assert HS2.size == old_size * config.probing['DOWNSIZE_FACTOR']
