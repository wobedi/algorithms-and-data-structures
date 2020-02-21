import random

import src.helpers.partition as partition


def quickselect(arr: list, k: int):
    """Returns kth-smallest item in arr by implementing
    https://en.wikipedia.org/wiki/Quickselect
    """
    if k > len(arr)-1 or k < 0:
        raise ValueError(f"k must be in range [0, {len(arr)}) but is {k}")
    aux = arr.copy()
    random.shuffle(aux)    # Randomizing is ensuring probabilisitic efficiency
    return _quickselect(aux, k, lower=0, upper=len(arr)-1)


def _quickselect(arr: list, k: int, lower: int, upper: int):
    """Recursive implementation of quickselect"""
    lt, gt = partition.three_way_partition(arr, lower, upper)
    if k in range(lt, gt+1):
        return arr[gt]    # gt is arbitrary, any value in range [lt,gt] works
    elif k < lt:
        return _quickselect(arr, k, lower, lt-1)
    elif k > gt:
        return _quickselect(arr, k, gt+1, upper)


if __name__ == '__main__':
    quickselect([1, 2, 3, 4, 5, 6, 7, 8], 2)
