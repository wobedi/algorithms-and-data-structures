import random
from .helpers import partition_in_place

class ArraySearch:
    def binary_search_iterative(self, arr, key):
        """Returns int:index of key in sorted arr if key is in arr, else -1
        by implementing
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
        

    def binary_search_recursive(self, arr, key):
        """Returns int:index of key in sorted arr if key is in arr, else -1
        by implementing
        https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorithm
        """
        if len(arr) == 1:
            return 0 if arr[0] == key else -1
        mid = len(arr) // 2
        if arr[mid] > key:
            self.binary_search_recursive(arr[:mid], key)
        elif arr[mid] < key:
            self.binary_search_recursive(arr[mid+1:], key)
        elif arr[mid] == key:
            return mid

    def quick_select(self, arr, k):
        """Returns kth-smallest item in sorted arr if arr is sorted
        ascendingly and kth-largest item if arr is sorted descendingly
        by implementing https://en.wikipedia.org/wiki/Quickselect
        """
        k = int(k)
        if k > len(arr):
            return f"Error - k is {k} but array length is {len(arr)}"
        aux = arr.copy()  # Using an aux arr to not modify the original arr
        random.shuffle(aux)
        return self._quick_select(aux, k, lower=0, upper=len(arr)-1)

    def _quick_select(self, arr, k, lower, upper):
        lt, gt = partition_in_place(arr, lower, upper)
        if k in range(lt, gt+1):
            print("Final arr: ", arr)
            return arr[gt]  # arbitrary, any value between [lt,gt] would work
        elif k < lt:
            return self._quick_select(arr, k, lower, lt-2)
        elif k > gt:
            return self._quick_select(arr, k, gt, upper) 

    


def test_client():
    n = input("Size of random number array:  ")

    # more elegant way of doing this?
    while(n.isdigit() and int(n) < 1 if n.isdigit() else True):
        n = input('Please provide a positive *integer*: ')

    n = int(n)

    array = random.sample(range(n*2), n)  # n*2 is arbitrary to make it more interesting
    array_sorted = sorted(array)
    print(f"Sorted Array: {array_sorted}")

    AS = ArraySearch(array_sorted)

    key = input("Search for key:  ")

    # more elegant way of doing this?
    while(key.isdigit() and int(key) < 1 if key.isdigit() else True):
        key = input('Please provide a positive *integer*: ')

    position = AS.binary_search_recursive(array_sorted, key)

    print(f'Position: {position}')


if __name__ == "__main__":
    test_client()
