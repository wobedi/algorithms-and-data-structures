from random import sample
# test

class ArraySearch():
    def __init__(self, array_sorted):
        self.array_sorted = array_sorted  # TODO not sure if we need that here?
        

    class BinarySearch():

        def binary_search_iterative(self, arr, key):
        """Returns index of key in arr (if key is in arr)

        Parameters:
            arr (list of x): Ascendingly sorted list
            key (x): key to be searched for

        Returns:
            index (int): = Index of key in arr or -1
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
            """Returns index of key in arr (if key is in arr)

            Parameters:
                arr (list of x): Ascendingly sorted list
                key (x): key to be searched for

            Returns:
                index (int): = Index of key in arr or -1
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

    


def test_client():
    n = input("Size of random number array:  ")

    # more elegant way of doing this?
    while(n.isdigit() and int(n) < 1 if n.isdigit() else True):
        n = input('Please provide a positive *integer*: ')

    n = int(n)

    array = sample(range(n*2), n)  # n*2 is arbitrary to make it more interesting
    array_sorted = sorted(array)
    print(f"Sorted Array: {array_sorted}")

    AS = ArraySearch(array_sorted)

    key = input("Search for key:  ")

    # more elegant way of doing this?
    while(key.isdigit() and int(key) < 1 if key.isdigit() else True):
        key = input('Please provide a positive *integer*: ')

    position = AS.binary_search(key)

    print(f'Position: {position}')


if __name__ == "__main__":
    test_client()
