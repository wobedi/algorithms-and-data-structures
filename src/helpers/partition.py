def three_way_partition(arr, lower, upper):
  """ Implements 
  https://en.wikipedia.org/wiki/Dutch_national_flag_problem#The_array_case """
  lt, gt, i = lower, upper, lower
  pivot = arr[lower]  # TODO performance could be improved by using smarter pivot

  while i <= gt:
    if arr[i] < pivot:
      arr[lt], arr[i] = arr[i], arr[lt]
      lt, i = lt+1, i+1
    elif arr[i] > pivot:
      arr[gt], arr[i] = arr[i], arr[gt]
      gt -= 1
    else:
      i += 1
  return lt, gt