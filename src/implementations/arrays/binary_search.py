
def binary_search_iterative(arr: list, key) -> int:
    """Returns index of key in sorted arr if key is in arr, else -1.
    Implements:
    https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorithm
    """
    lo, mid, hi = 0, len(arr) // 2, len(arr)
    while hi > lo:
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            hi = mid
            mid = (hi + lo) // 2
        if arr[mid] < key:
            lo = mid
            mid = (hi + lo) // 2
    return -1


def binary_search_recursive(arr: list, key) -> int:
    """Returns index of key in sorted arr if key is in arr, else -1.
    Implements:
    https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorithm
    """
    if len(arr) == 1:
        return (0 if arr[0] == key else -1)
    mid = len(arr) // 2
    if arr[mid] == key:
        return mid

    if arr[mid] > key:
        return binary_search_recursive(arr[:mid], key)
    if arr[mid] < key:
        return binary_search_recursive(arr[mid+1:], key)


# import random
# def test_client():
#         n = input('Size of random number array:    ')

#         # more elegant way of doing this?
#         while(n.isdigit() and int(n) < 1 if n.isdigit() else True):
#                 n = input('Please provide a positive *integer*: ')

#         n = int(n)

#         array = random.sample(range(n*2), n)
# # n*2 is arbitrary to make it more interesting
#         array_sorted = sorted(array)
#         print(f'Sorted Array: {array_sorted}')

#         # AS = ArraySearch(array_sorted)

#         # more elegant way of doing this?
#         while(key.isdigit() and int(key) < 1 if key.isdigit() else True):
#                 key = input('Please provide a positive *integer*: ')

#         position = binary_search_recursive(array_sorted, key)

#         print(f'Position: {position}')
