from time import perf_counter

from pandas import DataFrame


def lcs_length_recursive(a: str, b: str):
    """Calculates the length of the longest common subsequence of two strings
    in O(2^n)/O(2^m) where n an m are the lengths of the strings
    """
    if len(a) < 1 or len(b) < 1:
        raise Exception('Please provide two non-empty strings')
    return _lcs_length_recursive(a, b, 0, 0)


def _lcs_length_recursive(a: str, b: str, i: int, j: int):
    # Recursively find LCS of a and b, looping through their indices i and j
    if i >= len(a) or j >= len(b):
        return 0
    if a[i] == b[j]:
        return 1 + _lcs_length_recursive(a, b, i+1, j+1)
    return max([
                _lcs_length_recursive(a, b, i+1, j),
                _lcs_length_recursive(a, b, i, j+1)
               ])


def lcs_length_bottom_up(a: str, b: str):
    """Calculates the length of the longest common subsequence of two strings
    in O(nm) where n an m are the lengths of the strings
    """
    # cache has one extra row and column of zeroes for convenience
    cache = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(a)-1, -1, -1):
        for j in range(len(b)-1, -1, -1):
            if a[i] == b[j]:
                cache[i][j] = 1 + cache[i+1][j+1]
            else:
                cache[i][j] = max([cache[i+1][j], cache[i][j+1]])
    return cache[0][0], cache


def lcs_from_length_cache(a: str, b: str, cache: [[int]]) -> str:
    """Returns the actual LCS based on the LCS length cache[][]"""
    i = j = 0
    lcs = ''
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            lcs += a[i]
        if cache[i+1][j] >= cache[i][j+1]:
            i += 1
        else:
            j += 1
    return lcs


if __name__ == '__main__':
    print('#################################################')
    print('### LCS("nematode knowledge", "empty bottle") ###')
    print('#################################################')
    a, b = "nematode knowledge", "empty bottle"
    print('RECURSIVE IMPLEMENTATION:')
    start = perf_counter()
    print(lcs_length_recursive('nematode knowledge', 'empty bottle'))
    stop = perf_counter()
    print(f'Secs: {stop - start}\n')

    print('BOTTOM-UP IMPLEMENTATION:')
    start = perf_counter()
    length, cache = lcs_length_bottom_up(a, b)
    lcs = lcs_from_length_cache(a, b, cache)
    stop = perf_counter()
    print(f'Length: {length}')
    print(f'LCS: {lcs}')
    print(f'Cache:\n{DataFrame(cache)}')
    print(f'Secs: {stop - start}\n')
