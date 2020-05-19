import pytest

from src.implementations.priority_queue.binary_heap import (
    BinaryHeap
)


@pytest.fixture()
def keys():
    return [1, 2, 3, 10, 34, 22, 14, 21, 0]


@pytest.fixture()
def keys_sorted():
    return sorted([1, 2, 3, 10, 34, 22, 14, 21, 0])


@pytest.fixture()
def pq_empty():
    return BinaryHeap()


@pytest.fixture()
def pq_filled():
    return BinaryHeap([1, 2, 3, 10, 34, 22, 14, 21, 0])


def test_construction(pq_empty, pq_filled, keys):
    # Construction should work for empty and non-empty cases
    pq_empty = BinaryHeap()
    pq_filled = BinaryHeap(keys)
    assert isinstance(pq_empty, BinaryHeap)
    assert isinstance(pq_filled, BinaryHeap)


def test_size(pq_empty, pq_filled, keys):
    # .size() should work for empty and non-empty cases
    assert pq_empty.size() == 0
    assert pq_filled.size() == len(keys)


def test_is_empty(pq_empty, pq_filled):
    # .is_empty() should work for empty and non-empty cases
    assert pq_empty.is_empty() is True
    assert pq_filled.is_empty() is False


def test_max(pq_empty, pq_filled, keys_sorted):
    # .max() should work for empty and non-empty cases
    assert pq_empty.max() is None
    assert pq_filled.max() == keys_sorted[-1]

    # max() should throw if heap is empty
    with pytest.raises(Exception):
        assert del_max(pq_empty)


def test_del_max(pq_filled, keys_sorted):
    # .del_max() should work
    pq_filled.del_max()

    # .max() should still work after deletion
    assert pq_filled.max() == keys_sorted[-2]
    pq_filled.del_max()
    assert pq_filled.max() == keys_sorted[-3]


def test_insert(pq_empty, keys, keys_sorted):
    # .insert() should work, including subsequent deletions and max() calls
    for key in keys:
        pq_empty.insert(key)
    assert pq_empty.max() == keys_sorted[-1]
    pq_empty.del_max()
    assert pq_empty.max() == keys_sorted[-2]
    pq_empty.del_max()
    assert pq_empty.max() == keys_sorted[-3]
