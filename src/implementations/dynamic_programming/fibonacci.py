def fibonacci_recursive(x: int) -> int:
    """Calculates x'th Fibnoacci number in O(2^N) time, O(2^N) space"""
    # ignoring x<=0
    if x == 1 or x == 2:
        return 1
    return fibonacci_recursive(x-1) + fibonacci_recursive(x-2)


def fibonacci_memoized(x: int, cache: {}) -> int:
    """Calculates x'th Fibnoacci number in O(N) time, O(N) space"""
    # ignoring x<=0
    if x == 1 or x == 2:
        return 1
    if x not in cache:
        cache[x] = (fibonacci_memoized(x-1, cache)
                    + fibonacci_memoized(x-2, cache))
    return cache[x]


def fibonacci_bottom_up(x: int, cache: {}) -> int:
    """Calculates x'th Fibnoacci number in O(N) time, O(N) space"""
    # ignoring x<=0
    if x == 1 or x == 2:
        return 1
    cache[1] = cache[2] = 1
    for i in range(3, x + 1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[x]


def fibonacci_bottom_up_minified(x: int) -> int:
    """Calculates x'th Fibnoacci number in O(N) time, O(1) space"""
    # ignoring x<=0
    if x == 1 or x == 2:
        return 1
    res = 0
    first = second = 1
    for _ in range(3, x + 1):
        res = first + second
        first = second
        second = res
    return res


if __name__ == '__main__':
    test_cases: [(int, int)] = [
        (1, 1),  # 1st Fibonacci number
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (35, 9227465)  # 35th Fibonacci number
    ]
    for (x, result) in test_cases:
        assert fibonacci_recursive(x) == result
        assert fibonacci_memoized(x, {}) == result
        assert fibonacci_bottom_up(x, {}) == result
        assert fibonacci_bottom_up_minified(x) == result
        print(f'fibonacci({x}) == {result} correct for all functions')
