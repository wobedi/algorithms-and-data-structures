import pytest

from src.algorithms_and_data_structures.priority_queue.binary_heap import BinaryHeap


keys = [1, 2, 3, 10, 34, 22, 14, 21, 0]
keys_sorted = sorted(keys)
pq = BinaryHeap()
pq2 = BinaryHeap(keys)


def test_binary_heap():
    def construction():
        # Construction should work for empty and non-empty cases
        pq = BinaryHeap()
        pq2 = BinaryHeap(keys)

    def size():
        # .size() should work for empty and non-empty cases
        assert pq.size() == 0
        assert pq2.size() == len(keys)

    def is_empty():
        # .is_empty() should work for empty and non-empty cases
        assert pq.is_empty() is True
        assert pq2.is_empty() is False

    def max():
        # .max() should work for empty and non-empty cases
        assert pq.max() is None
        assert pq2.max() == keys_sorted[-1]

        # .max() should still work after deletion
        pq2.del_max()
        assert pq2.max() == keys_sorted[-2]
        pq2.del_max()
        assert pq2.max() == keys_sorted[-3]

        # max() should throw if heap is empty
        with pytest.raises(Exception("Error: Heap is empty")):
            assert del_max(pq)

    def insert():
        # .insert() should work, including subsequent deletions and max() calls
        for key in keys:
            pq.insert(key)
        assert pq.max() == keys_sorted[-1]
        pq.del_max()
        assert pq.max() == keys_sorted[-2]
        pq.del_max()
        assert pq.max() == keys_sorted[-3]
