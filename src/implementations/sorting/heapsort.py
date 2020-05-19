from random import shuffle

from src.algorithms_and_data_structures.priority_queue.binary_heap import BinaryHeap


def heapsort(arr: list) -> list:
    """Implements https://en.wikipedia.org/wiki/Heapsort"""
    shuffle(arr)    # Randomizing for probabilistic performance improvement
    heap = BinaryHeap(arr)

    # Using 'private' ._swap() and ._sink() methods here, a bit hack-ish.
    i = len(arr)
    while i > 0:
        heap._swap(1, i)
        heap._sink(1, i)
        i -= 1
    arr = heap.values()
    return arr


if __name__ == '__main__':
    keys = [1, 2, 3, 10, 34, 22, 14, 21, 0]
    keys_sorted = sorted(keys)
    print(heapsort(keys))
    assert(heapsort(keys)) == keys_sorted
