# TODO: un-make this a class?

class MergeSort:
  def __str__(self):
    return "MergeSort"

  def merge_sort_recursive(self, arr):
    """ Sorts arr by implementing 
        https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation"""
    if len(arr) <= 1:
      return arr
    lo, mid, hi = 0, len(arr) // 2, len(arr)
    left = self.merge_sort_recursive(arr[lo:mid])
    right = self.merge_sort_recursive(arr[mid:hi])
    return self._sort_merge(left, right)

  def merge_sort_iterative(self, arr):
    """ Sorts arr by implementing
        https://en.wikipedia.org/wiki/Merge_sort#Bottom-up_implementation"""
    # this one works but is kinda ugly / not self-explenatory
    size = 1
    while size <= len(arr):
      for i in range(0, len(arr), size*2):
        left = arr[i:i+size]
        right_ceiling = min((i+size*2), len(arr))
        right = arr[i+size:right_ceiling]
        arr[i:i+size*2] = self._sort_merge(left, right)
      size *= 2
    return arr

  def _sort_merge(self, left, right):
    """Merge and sort list:left and list:right and return list:res"""
    res, i, j = [], 0, 0
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