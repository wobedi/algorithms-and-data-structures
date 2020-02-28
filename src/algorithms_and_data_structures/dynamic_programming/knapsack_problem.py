from pandas import DataFrame


def ks_recursive_weight(weights: [int], values: [int], capacity: int) -> int:
    """Recursive solution for
    https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
    """
    assert len(weights) == len(values)
    weights.insert(0, 0)
    values.insert(0, 0)
    return _ks_recursive_weight(weights, values, len(values) - 1, capacity)


def _ks_recursive_weight(weights: [int], values: [int], i: int, w: int) -> int:
    if i <= 0 or w <= 0:
        return 0

    if weights[i] > w:
        solution = _ks_recursive_weight(weights[:i], values[:i], i-1, w)
    else:
        pack_item = (_ks_recursive_weight(weights[:i], values[:i], i-1, w-weights[i])
                     + values[i])
        leave_item = _ks_recursive_weight(weights[:i], values[:i], i-1, w)
        solution = max([pack_item, leave_item])
    return solution


def ks_bottom_up(weights: [int], values: [int], capacity: int):
    """Bottom-up solution for
    https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
    """
    cache = [[0 for _ in range(capacity+1)] for _ in range(len(values))]
    keep = [[0 for _ in range(capacity+1)] for _ in range(len(values))]

    # Populating cache with max_value per itembase X capacity combo
    for w in range(1, capacity+1):
        for i in range(1, len(values)):
            if weights[i-1] > capacity:
                cache[i][w] = cache[i-1][w]
            else:
                leave_item = cache[i-1][w]
                pack_item = cache[i-1][w - weights[i]] + values[i]
                keep[i][w] = 1 if pack_item > leave_item else 0
                cache[i][w] = max(leave_item, pack_item)

    # Identifying packed items based on cache
    items = []
    k = capacity
    for i in range(len(weights)-1, 0, -1):
        if keep[i][k]:
            items.append(i)
            k -= weights[i]

    return cache, items
