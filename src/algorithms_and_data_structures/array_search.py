import random
import src.algorithms_and_data_structures.helpers as helpers

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

    def quickselect(self, arr, k):
        """Returns kth-smallest item in arr by implementing
        https://en.wikipedia.org/wiki/Quickselect
        """
        k = int(k)
        if k > len(arr)-1 or k < 0:
            raise ValueError(f"k is {k} but array length is {len(arr)}")
        if not all(isinstance(x, (int, float)) for x in arr):
            raise TypeError(f"Arr must only contain integers or floats")
        
        aux = arr.copy()  # Using an aux arr to not modify the original arr
        random.shuffle(aux)  # Ensuring quickselect efficiency
        return self._quickselect(aux, k, lower=0, upper=len(arr)-1)

    def _quickselect(self, arr, k, lower, upper):
        lt, gt = helpers.partition_in_place(arr, lower, upper)
        if k in range(lt, gt+1):
            return arr[gt]  # arbitrary, any value between [lt,gt] would work
        elif k < lt:
            return self._quickselect(arr, k, lower, lt-1)
        elif k > gt:
            return self._quickselect(arr, k, gt+1, upper) 

if __name__ == '__main__':
    AS = ArraySearch()
    AS.quickselect([1,2,3,4,5,6,7,8], 2)    


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
