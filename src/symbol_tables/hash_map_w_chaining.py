from pandas import DataFrame

from src.symbol_tables import config


class HashMap:
    """Implements https://en.wikipedia.org/wiki/Hash_table#Associative_arrays,
    using https://en.wikipedia.org/wiki/Hash_table#Separate_chaining
    for collision resolution
    """

    def __init__(self, size):
        # list of lists implements chaining
        self.size = size
        self.table = [[] for i in range(size)]
        self.load = 0

    def __str__(self):
        return f'{self.table} | size: {self.size} | load: {self.load}'

    def put(self, key, value):
        """Puts key:value into hash map, resizing underlying table if needed"""
        row = self.table[self._modular_hash(key)]
        for tup in row:
            if tup[0] == key:
                tup[1] = value
                return
        row.append((key, value))
        self.load += 1
        if self.load / self.size >= config.chaining['LOAD_FACTOR_MAX']:
            self._upsize()
        return

    def get(self, key):
        """Returns value of key in hash map if key in hash map, else False"""
        row = self.table[self._modular_hash(key)]
        if len(row) < 0:
            print(f'\nKey {key} not in table')
            return False
        for tup in row:
            if tup[0] == key:
                print(tup[1])
                return tup[1]

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

    def _modular_hash(self, key):
        # hashing key and using modulo operator to wrap it into self.size
        return hash(key) % self.size

    def _downsize(self):
        # downsize underlying array (allocate less memory)
        return self._resize(config.chaining['DOWNSIZE_FACTOR'])

    def _upsize(self):
        # upsize underlying array (allocate more memory)
        return self._resize(config.chaining['UPSIZE_FACTOR'])

    def _resize(self, factor: float):
        # resize underlying array by factor:float
        self.size = int(self.size * factor)
        aux_table = [[] for i in range(self.size)]
        for row in self.table:
            for k, v in row:
                aux_table[self._modular_hash(k)].append((k, v))
        self.table = aux_table
        return


# Turn this into a unit test
if __name__ == '__main__':
    HT = HashMap(5)
    print(DataFrame(HT.table))
    HT.get("hello")
    print(DataFrame(HT.table))
    HT.put("hello", "hellov")
    print(DataFrame(HT.table))
    HT.get("hello")
    print(DataFrame(HT.table))
    HT.put(1, "1v")
    print(DataFrame(HT.table))
    HT.put(2, "2v")
    print(DataFrame(HT.table))
    HT.put(3, "3v")
    print(DataFrame(HT.table))
    HT.put(4, "4v")
    print(DataFrame(HT.table))
    HT.put(5, "5v")
    print(DataFrame(HT.table))
    HT.put(6, "6v")
    print(DataFrame(HT.table))
    HT.put(7, "7v")
    print(DataFrame(HT.table))
    HT.delete(7)
    print(DataFrame(HT.table))
    HT.delete(7)
    print(DataFrame(HT.table))
    HT.delete(5)
    print(DataFrame(HT.table))
    HT.delete(3)
    print(DataFrame(HT.table))
    HT.delete(2)
    print(DataFrame(HT.table))
    HT.delete(4)
    print(DataFrame(HT.table))
    HT.delete("hello")
    print(DataFrame(HT.table))
    HT.delete(1)
    print(DataFrame(HT.table))
