def mergesort_recursive(arr: list) -> list:
    """Sorts arr by implementing
    https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation
    """
    if len(arr) <= 1:
        return arr
    lo, mid, hi = 0, len(arr) // 2, len(arr)
    left = mergesort_recursive(arr[lo:mid])
    right = mergesort_recursive(arr[mid:hi])
    return _sort_merge(left, right)


def mergesort_iterative(arr: list) -> list:
    """Sorts arr by implementing
    https://en.wikipedia.org/wiki/Merge_sort#Bottom-up_implementation
    """
    chunk = 1
    while chunk <= len(arr):
        for i in range(0, len(arr), chunk*2):
            left = arr[i:i+chunk]
            right_ceiling = min((i+chunk*2), len(arr))
            right = arr[i+chunk:right_ceiling]
            arr[i:i+chunk*2] = _sort_merge(left, right)
        chunk *= 2
    return arr


def _sort_merge(left: list, right: list) -> list:
    """Merge and sort list:left and list:right and return list:res"""
    res = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


if __name__ == '__main__':
    keys = [1, 2, 3, 10, 34, 22, 14, 21, 0]
    keys_sorted = sorted(keys)

    recursively_mergesorted = mergesort_recursive(keys)
    iteratively_mergesorted = mergesort_iterative(keys)

    print(f'Recrusive mergesort output: {recursively_mergesorted}')
    assert recursively_mergesorted == keys_sorted
    print(f'Iterative mergesort output: {iteratively_mergesorted}')
    assert iteratively_mergesorted == keys_sorted
