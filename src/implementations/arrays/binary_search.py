def binary_search_iterative(arr: list, key) -> int:
    """Returns index of key in sorted arr if key is in arr, else -1.
    Implements:
    https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorithm
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            hi = mid - 1
        if arr[mid] < key:
            lo = mid + 1
    return -1


def binary_search_recursive(arr: list, key) -> int:
    """Returns index of key in sorted arr if key is in arr, else -1.
    Implements:
    https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorithm
    """
    return _binary_search_recursive(arr, 0, len(arr) - 1, key)


def _binary_search_recursive(arr: list, start: int, end: int, key) -> int:
    if end - start <= 1:
        return (start if arr[start] == key else -1)
    mid = (end + start) // 2
    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return _binary_search_recursive(arr, start, mid - 1, key)
    if arr[mid] < key:
        return _binary_search_recursive(arr, mid + 1, end, key)


if __name__ == '__main__':
    test_cases: [([int], int, int)] = [
        ([1, 2, 3, 4, 5, 6], 1, 0),
        ([1, 2, 3, 4, 5, 6], 3, 2),
        ([1, 2, 3, 4, 5, 6], 6, 5),
        ([1, 2, 3, 4, 5, 6], 7, -1),
        ([1, 2, 3, 4, 5, 6], 0, -1),
    ]

    for (arr, key, result) in test_cases:
        assert binary_search_iterative(arr, key) == result
        assert binary_search_recursive(arr, key) == result
