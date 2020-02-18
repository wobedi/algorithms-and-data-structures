from random import shuffle

from basic_sorts import insertion_sort
from src.helpers.partition import three_way_partition


def quick_sort(arr):
    """Sorts arr by implementing https://en.wikipedia.org/wiki/Quicksort"""
    shuffle(arr)
    print("Shuffled: ", arr)
    return _quick_sort(arr, lower=0, upper=len(arr)-1)


def _quick_sort(arr, lower, upper):
    """Recursive implementation of quicksort"""
    if upper <= lower:
        return
    if upper - lower < 10:
        # optimizing performance by using insertion sort for small sub arrays
        insertion_sort(arr)
    else:
        lt, gt = three_way_partition(arr, lower, upper)
        _quick_sort(arr, lower, lt-1)
        _quick_sort(arr, gt+1, upper)
    return arr
