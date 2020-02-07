from random import shuffle
from basic_sorts import insertion_sort
from src.helpers.partition import three_way_partition
# TODO: un-make this a class?

class QuickSort:
  def __str__(self):
    return "QuickSort"

  def quick_sort(self, arr):
    """Sorts arr by implementing https://en.wikipedia.org/wiki/Quicksort"""
    shuffle(arr)
    print("Shuffled: ", arr)
    return self._quick_sort_in_place(arr, lower=0, upper=len(arr)-1)

  def _quick_sort_in_place(self, arr, lower, upper):
    if upper <= lower:
      return
    if upper - lower < 10:
      # optimizing performance by using insertion sort for small arrs
      insertion_sort(arr)
    else:
      lt, gt = three_way_partition(arr, lower, upper)
      self._quick_sort_in_place(arr, lower, lt-1)
      self._quick_sort_in_place(arr, gt+1, upper)
    return arr

  def _quick_sort_aux_arr(self, arr):
    """Uses auxiliary array to make sort stable, using O(N) extra space"""
    if len(arr) <= 1:
      return arr
    pivot = arr[0]
    less, equal, greater = [], [], []

    for el in arr:
      if el < pivot:
        less.append(el)
      if el == pivot:
        equal.append(el)
      if el > pivot:
        greater.append(el)

    less = self._quick_sort_aux_arr(less)
    greater = self._quick_sort_aux_arr(greater)
    return less + equal + greater