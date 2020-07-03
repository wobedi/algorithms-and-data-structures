from pandas import DataFrame

from src.implementations.symbol_tables import config


class HashMap:
    """Implements https://en.wikipedia.org/wiki/Hash_table#Associative_arrays,
    using https://en.wikipedia.org/wiki/Hash_table#Separate_chaining
    for collision resolution
    """

    def __init__(self, size: int):
        # List of lists implements chaining
        self.size = size
        self.table = [[] for i in range(size)]
        self.load = 0

    def __str__(self):
        return f'{self.table} | size: {self.size} | load: {self.load}'

    def get(self, key):
        """Returns value of key in hash map if key in hash map, else None"""
        row = self.table[self._modular_hash(key)]
        if len(row) < 0:
            print(f'\nKey {key} not in table')
            return None
        for tup in row:
            if tup[0] == key:
                return tup[1]

    def put(self, key, value):
        """Puts key:value into hash map, resizing underlying table if needed"""
        row = self.table[self._modular_hash(key)]
        for tup in row:
            if tup[0] == key:
                tup[1] = value
                return
        row.append([key, value])
        self.load += 1
        if self.load / self.size >= config.chaining['LOAD_FACTOR_MAX']:
            self._upsize()
        return

    def delete(self, key):
        """Deletes key from hash map. Returns True if successful, else False"""
        row = self.table[self._modular_hash(key)]
        if len(row) <= 0:
            print(f'Key {key} not in table')
            return False
        for i, tup in enumerate(row):
            if tup[0] == key:
                del row[i]
                self.load -= 1
                if self.load / self.size <= config.chaining['LOAD_FACTOR_MIN']:
                    self._downsize()
                print(f'Deleted key {key} from table')
                return True

    def _modular_hash(self, key) -> int:
        # Hashing key and using modulo operator to wrap it into self.size
        return hash(key) % self.size

    def _downsize(self):
        # Downsize underlying array (allocate less memory)
        return self._resize(config.chaining['DOWNSIZE_FACTOR'])

    def _upsize(self):
        # Upsize underlying array (allocate more memory)
        return self._resize(config.chaining['UPSIZE_FACTOR'])

    def _resize(self, factor: float):
        # Resize underlying array by factor:float
        self.size = int(self.size * factor)
        aux_table = [[] for i in range(self.size)]
        for row in self.table:
            for k, v in row:
                aux_table[self._modular_hash(k)].append([k, v])
        self.table = aux_table
        return


if __name__ == '__main__':
    initial_size = 5
    HM = HashMap(initial_size)
    test_items = [
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4],
        [5, 5],
        [12, 12]
    ]
    print(f'INITIAL EMPTY HM:\n{DataFrame(HM.table)}\n*********************')

    # .get() should work if HM is empty
    for key, _ in test_items:
        assert HM.get(key) is None

    # .put() and, .get() should work if HM has items
    for key, value in test_items:
        assert HM.get(key) is None
        HM.put(key, value)
        assert HM.get(key) == value
    print(f'HM AFTER PUTS:\n{DataFrame(HM.table)}\n*********************')

    # delete() should work, .get() should work after items have been deleted
    for key, value in test_items:
        assert HM.get(key) == value
        HM.delete(key)
        assert HM.get(key) is None
    print(f'HM AFTER DELETES:\n{DataFrame(HM.table)}\n*********************')

    # subsequent puts should override previous puts
    HM.put(1, 1)
    HM.put(1, 2)
    assert HM.get(1) == 2

    # upsize should work
    HM2 = HashMap(initial_size)
    assert len(test_items) > initial_size
    assert len(test_items) < initial_size * config.chaining['UPSIZE_FACTOR']

    added_items_counter = 0
    while HM2.load / initial_size < config.chaining['LOAD_FACTOR_MAX']:
        key = test_items[added_items_counter][0]
        value = test_items[added_items_counter][1]
        HM2.put(key, value)
        added_items_counter += 1

    print(f'HM2 AFTER UPSIZING:\n{DataFrame(HM2.table)}\n********************')
    assert HM2.load == added_items_counter
    assert HM2.size == len(HM2.table)
    assert HM2.size == initial_size * config.chaining['UPSIZE_FACTOR']

    # downsize should work
    old_size = HM2.size
    old_load = HM2.load
    deleted_items_counter = 0
    while HM2.load / old_size > config.chaining['LOAD_FACTOR_MIN']:
        key = test_items[deleted_items_counter][0]
        HM2.delete(key)
        deleted_items_counter += 1

    print(f'HM2 AFTER DOWNSIZING:\n{DataFrame(HM2.table)}\n******************')
    assert HM2.load == old_load - deleted_items_counter
    assert HM2.size == len(HM2.table)
    assert HM2.size == old_size * config.chaining['DOWNSIZE_FACTOR']
