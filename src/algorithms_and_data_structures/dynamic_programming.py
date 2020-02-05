from time import perf_counter
from pandas import DataFrame

## TODO: Split this up into two modules under folder 'dynamic programming'

def lcs_length_recursive(a: str, b: str):
  """ Calculates the length of the longest common subsequence of two strings 
      in O(2^n)/O(2^m) where n an m are the lengths of the strings"""
  if len(a) < 1 or len(b) < 1:
    raise Exception('Please provide two non-empty strings')
  return _lcs_length_recursive(a, b, 0, 0)

def _lcs_length_recursive(a: str, b: str, i: int, j: int):
  if i >= len(a) or j >= len(b):
    return 0
  if a[i] == b[j]:
    return 1 + _lcs_length_recursive(a, b, i+1, j+1)
  return max([
              _lcs_length_recursive(a, b, i+1, j),
              _lcs_length_recursive(a, b, i, j+1)
            ])

def lcs_length_memoized(a: str, b: str):
  """ Calculates the length of the longest common subsequence of two strings 
      in O(nm) where n an m are the lengths of the strings"""
  if len(a) < 1 or len(b) < 1:
    raise Exception('Please provide two non-empty strings')
  cache = [[0 for _ in range(len(b))] for _ in range(len(a))]
  return _lcs_length_memoized(a, b, 0, 0, cache), cache

def _lcs_length_memoized(a: str, b: str, i: int, j: int, cache: [[int]]):
  # TODO cache seems buggy here
  if i >= len(a) or j >= len(b):
    return 0
  if not cache[i][j]:
    if a[i] == b[j]:
      cache[i][j] = 1 + _lcs_length_memoized(a, b, i+1, j+1, cache)
    else:
      cache[i][j] = max([
                          _lcs_length_memoized(a, b, i+1, j, cache),
                          _lcs_length_memoized(a, b, i, j+1, cache)
                        ])
  return cache[i][j]

def lcs_length_bottom_up(a: str, b: str):
  """ Calculates the length of the longest common subsequence of two strings 
      in O(nm) where n an m are the lengths of the strings"""
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

#################################

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
  first, second = 1, 2
  for _ in range(4, x + 1):
    res = first + second
    first = second
    second = res
  return res


# if __name__ == '__main__':
#   print('#####################')
#   print('### FIBONACCI(35) ###')
#   print('#####################')
#   print('RECURSIVE IMPLEMENTATION:')
#   start = perf_counter()
#   print(fibonacci_recursive(35))
#   stop = perf_counter()
#   print(f'Secs: {stop - start}\n')

#   print('MEMOIZED IMPLEMENTATION:')
#   start = perf_counter()
#   print(fibonacci_memoized(35, {}))
#   stop = perf_counter()
#   print(f'Secs: {stop - start}\n')

#   print('BOTTOM-UP IMPLEMENTATION:')
#   start = perf_counter()
#   print(fibonacci_bottom_up(35, {}))
#   stop = perf_counter()
#   print(f'Secs: {stop - start}\n')

#   print('BOTTOM-UP (MINIFIED) IMPLEMENTATION:')
#   start = perf_counter()
#   print(fibonacci_bottom_up_minified(35))
#   stop = perf_counter()
#   print(f'Secs: {stop - start}\n')


if __name__ == '__main__':
  print('#################################################')
  print('### LCS("nematode knowledge", "empty bottle") ###')
  print('#################################################')
  a, b = "nematode knowledge", "empty bottle"
  # print('RECURSIVE IMPLEMENTATION:')
  # start = perf_counter()
  # print(lcs_length_recursive('nematode knowledge', 'empty bottle'))
  # stop = perf_counter()
  # print(f'Secs: {stop - start}\n')

  # print('MEMOIZED IMPLEMENTATION:')
  # start = perf_counter()
  # length, cache = lcs_length_memoized(a, b)
  # lcs = lcs_from_length_cache(a, b, cache)
  # stop = perf_counter()
  # print(f'Length: {length}')
  # print(f'LCS: {lcs}')
  # print(f'Cache:\n{DataFrame(cache)}')
  # print(f'Secs: {stop - start}\n')

  print('BOTTOM-UP IMPLEMENTATION:')
  start = perf_counter()
  length, cache = lcs_length_bottom_up(a, b)
  lcs = lcs_from_length_cache(a, b, cache)
  stop = perf_counter()
  print(f'Length: {length}')
  print(f'LCS: {lcs}')
  print(f'Cache:\n{DataFrame(cache)}')
  print(f'Secs: {stop - start}\n')

