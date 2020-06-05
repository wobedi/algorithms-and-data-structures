from random import shuffle

from src.implementations.sorting.basic_sorts import insertion_sort
from src.implementations.helpers.partition import three_way_partition


def quicksort(arr: list) -> list:
    """Sorts arr in-place
    by implementing https://en.wikipedia.org/wiki/Quicksort
    """
    shuffle(arr)
    return _quicksort(arr, lower=0, upper=len(arr)-1)


def _quicksort(arr: list, lower: int, upper: int) -> list:
    """Recursive implementation of quicksort"""
    if upper <= lower:
        return
    if upper - lower < 10:
        # Optimizing performance by using insertion sort for small sub arrays
        insertion_sort(arr)
    else:
        lt, gt = three_way_partition(arr, lower, upper)
        _quicksort(arr, lower, lt-1)
        _quicksort(arr, gt+1, upper)
    return arr
