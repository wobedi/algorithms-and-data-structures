from src.symbol_tables import config


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
        key_in_set, index = self._linear_probing(key)
        if not key_in_set:
            return f'Deletion error: Key {key} is NOT part of this hash set'
        self.set[index] = None
        self.load -= 1

        # Moving subsequent items backwards to not break linear probing
        next = index + 1
        while self.set[next % self.size] is not None:  # Wrap around via modulo
            self.set[index], self.set[next] = self.set[next], self.set[index]
            index += 1
            next += 1

        if self.load / self.size < config.probing['LOAD_FACTOR_MIN']:
            self._downsize()
        return

    def _linear_probing(self, key, set_=None) -> bool, int:
        """Linear probing for key through hash set.
        Returns tuple:
        (True, index) for search hits at index,
        (False, index) for search misses;
        where index is the final index checked/first index with key==None
        """
        set_ = set_ or self.set
        index = self._modular_hash(key)    # Entry point for linear probing
        while set_[index] is not None:
            if index >= self.size:    # Wrap around
                index = 0
                continue
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
    HT = HashSet(5)
    print(HT.set)
    print(HT.contains("hello"))
    print(HT.set)
    HT.put("hello")
    print(HT.set)
    print(HT.contains("hello"))
    print(HT.set)
    HT.put(1)
    print(HT.set)
    HT.put(2)
    print(HT.set)
    HT.put(3)
    print(HT.set)
    HT.put(4)
    # _linear_probing
    print(HT.set)
    HT.put(5)
    print(HT.set)
    HT.put(6)
    print(HT.set)
    HT.put(7)
    print(HT.set)
    HT.delete(7)
    print(HT.set)
    HT.delete(7)
    print(HT.set)
    HT.delete(5)
    print(HT.set)
    HT.delete(3)
    print(HT.set)
    HT.delete(2)
    print(HT.set)
    HT.delete(4)
    print(HT.set)
    HT.delete("hello")
    print(HT.set)
    HT.delete(1)
    print(HT.set)
