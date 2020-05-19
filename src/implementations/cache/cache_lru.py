DATABASE = {
    'test1': 123,
    'test2': '456',
    'test3': [7, '8', 9],
    'test4': 123,
    'test5': '456',
    'test6': [7, '8', 9]
}


class DoublyLinkedListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key  # redundant?
        self.value = value
        self.prev = prev
        self.next = next


class LruCache:
    """Implements
    https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
    Both get() and set() are O(1)
    """
    def __init__(self, size=10):
        self.size = size
        self.load = 0
        self.cache_map = {}  # Hash map for O(1) lookup
        self.mru: DoublyLinkedListNode() = None  # End of the linked list
        self.lru: DoublyLinkedListNode() = None  # Start of the linked list

    def __str__(self):
        # Prints linked list representation
        string = '<-> '
        next_node = self.lru
        while next_node is not None:
            string += f'{next_node.key} <-> '
            next_node = next_node.next
        return string

    def get_value(self, key):
        """Returns value at key if key is in cache or database, else -1.
        Upserts cache during execution.
        Evicts LRU cache item if cache is full.
        (Read-through)
        """
        cached_node = self.cache_map.get(key, None)
        # Case 1: Value is in cache -> Update cache
        if cached_node:
            return self._cache_update(cached_node)

        value_db = DATABASE.get(key, None)
        # Case 2: Value is neither in cache nor in db
        if not value_db:
            print(f'Key "{key}" is not in database')
            return -1
        # Case 3: Value is in db but not in cache --> Insert node into cache
        else:
            return self._cache_insert(key, value_db)

    def set_value(self, key, value):
        """Upserts key:value into database and upserts cache.
        Evicts LRU item from cache if cache is full.
        (Write-through)
        """
        cached_node = self.cache_map.get(key, None)
        # Case 1: Value is in cache -> Update cache
        if cached_node:
            self._cache_update(cached_node)
            DATABASE[key] = value
        # Case 2: Value is not yet in cache -> Insert node into cache
        else:
            self._cache_insert(key, value)
            DATABASE[key] = value
        return

    def _cache_insert(self, key, value):
        # Inserts key:value into cache
        # 1: Special case for first node in empty cache
        if self.load == 0:
            new_cache_node = DoublyLinkedListNode(key, value)
            self.lru = new_cache_node
            self.mru = new_cache_node
            self.cache_map[key] = new_cache_node
            self.load += 1
            return value

        # 2: Evict lru if necessary
        if self.load == self.size:
            del self.cache_map[self.lru.key]
            new_lru = self.lru.next
            self.lru.next = None
            self.lru = new_lru
            new_lru.prev = None
            self.load -= 1

        # 3: Insert new node at the head of the linked list & in hash map
        new_cache_node = DoublyLinkedListNode(key, value,
                                              prev=self.mru, next=None)
        if self.mru:
            self.mru.next = new_cache_node
            new_cache_node.prev = self.mru
        self.mru = new_cache_node
        self.cache_map[key] = new_cache_node
        self.load += 1

        return value

    def _cache_update(self, cached_node: DoublyLinkedListNode):
        # updates position of cached_node in linked list
        if cached_node.prev:
            cached_node.prev.next = cached_node.next
        if cached_node.next:
            cached_node.next.prev = cached_node.prev
            if self.lru == cached_node:
                self.lru = cached_node.next
        cached_node.next = None
        cached_node.prev = self.mru
        self.mru.next = cached_node
        self.mru = cached_node
        return cached_node.value


if __name__ == '__main__':
    # Construction
    size = 4
    LRU = LruCache(size=size)

    # Getting while cache is not full yet
    for key in DATABASE.keys():
        value = LRU.get_value(key)
        assert value == DATABASE[key]
        assert LRU.mru.key == key
        assert len(LRU.cache_map.keys()) <= size
        print(LRU)

    # Getting when cache is full
    for key in DATABASE.keys():
        value = LRU.get_value(key)
        assert value == DATABASE[key]
        assert LRU.mru.key == key
        assert len(LRU.cache_map.keys()) == size
        print(LRU)

    # Setting (when cache is full)
    new_entries_1 = [
        ('test7', 7),
        ('test8', 8),
        ('test9', 9),
    ]
    for key, value in new_entries_1:
        LRU.set_value(key, value)
        assert DATABASE[key] == value
        assert LRU.mru.key == key
        assert len(LRU.cache_map.keys()) == size
        print(LRU)
        print('*************************')
        print(DATABASE)

    # Getting and Setting interleaved
    new_entries_2 = [
        ('test10', 10),
        ('test11', 11),
        ('test12', 12),
    ]
    old_keys = [
        'test1',
        'test9',
        'test2',
    ]
    for (new_key, value), old_key in zip(new_entries_2, old_keys):
        value = LRU.get_value(old_key)
        assert value == DATABASE[old_key]
        assert LRU.mru.key == old_key

        LRU.set_value(new_key, value)
        assert DATABASE[new_key] == value
        assert LRU.mru.key == new_key

        assert len(LRU.cache_map.keys()) == size

        print(LRU)
        print('*************************')
        print(DATABASE)
