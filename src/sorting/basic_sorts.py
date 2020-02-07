def selection_sort(arr):
  """Sorts arr by implementing https://en.wikipedia.org/wiki/Selection_sort"""
  for i in range(0, len(arr)):
    min_ = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_]:
          min_ = j
    arr[i], arr[min_] = arr[min_], arr[i]
  return arr

def insertion_sort(arr, increment=1):
  """Sorts arr by implementing https://en.wikipedia.org/wiki/Insertion_sort"""
  for i in range(increment, len(arr)):
    for j in range(i - increment, -1, -increment):
        if arr[j] > arr[j+increment]:
          arr[j+increment], arr[j] = arr[j], arr[j+increment]
        else:
          break
  return arr

def shell_sort(arr):
  """Sorts arr by implementing https://en.wikipedia.org/wiki/Shellsort"""
  seq = reversed(list(knuth_sequence(len(arr))))
  for increment in seq:
    insertion_sort(arr, increment=increment)

def knuth_sequence(arr_len):
  """Generates sequence as per https://oeis.org/A003462 until arr_len is hit"""
  x = 1
  while(x < arr_len):
    yield x
    x = 3*x + 1