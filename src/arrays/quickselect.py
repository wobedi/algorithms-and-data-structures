import random
import src.helpers.partition as partition

def quickselect(arr, k):
  """ Returns kth-smallest item in arr by implementing
      https://en.wikipedia.org/wiki/Quickselect"""
  k = int(k)
  if k > len(arr)-1 or k < 0:
    raise ValueError(f"k is {k} but array length is {len(arr)}")
  if not all(isinstance(x, (int, float)) for x in arr):
    raise TypeError(f"Arr must only contain integers or floats")
  
  aux = arr.copy()  # Using an aux arr to not modify the original arr
  random.shuffle(aux)  # Ensuring quickselect efficiency
  return _quickselect(aux, k, lower=0, upper=len(arr)-1)

def _quickselect(arr, k, lower, upper):
  lt, gt = partition.three_way_partition(arr, lower, upper)
  if k in range(lt, gt+1):
      return arr[gt]  # arbitrary, any value between [lt,gt] would work
  elif k < lt:
      return _quickselect(arr, k, lower, lt-1)
  elif k > gt:
      return _quickselect(arr, k, gt+1, upper) 

if __name__ == '__main__':
    quickselect([1,2,3,4,5,6,7,8], 2)  