import random
from time import perf_counter
# from .helpers import partition_in_place

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

def heap_sort(arr):
    # TODO using import data_structures.binary_heap
    pass


class MergeSort:
    def __str__(self):
        return "MergeSort"

    def merge_sort_recursive(self, arr):
        """Sorts arr by implementing 
        https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation
        """
        if len(arr) <= 1:
            return arr
        lo, mid, hi = 0, len(arr) // 2, len(arr)
        left = self.merge_sort_recursive(arr[lo:mid])
        right = self.merge_sort_recursive(arr[mid:hi])
        return self._sort_merge(left, right)

    def merge_sort_iterative(self, arr):
        """Sorts arr by implementing
        https://en.wikipedia.org/wiki/Merge_sort#Bottom-up_implementation
        """
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


class QuickSort:
    def __str__(self):
        return "QuickSort"

    def quick_sort(self, arr):
        """Sorts arr by implementing https://en.wikipedia.org/wiki/Quicksort"""
        random.shuffle(arr)
        print("Shuffled: ", arr)
        return self._quick_sort_in_place(arr, lower=0, upper=len(arr)-1)

    def _quick_sort_in_place(self, arr, lower, upper):
        if upper <= lower:
            return
        if upper - lower < 10:
            # optimizing performance by using insertion sort for small arrs
            insertion_sort(arr)
        else:
            lt, gt = partition_in_place(arr, lower, upper)
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


# def key_indexed_sorting(arr: [int], radix: int):
#     # count # of occurrences per radix variant
#     count = [0 for _ in range(radix)]
#     for el in arr:
#         count[el] += 1
    
#     # cumulate it to get offsets
#     for i in range(1, len(count)):
#         count[i] += count[i-1]

#     # sort stuff by moving at index and increment offset         
#     sorted_arr = [None for _ in range(len(arr))]
#     for el in arr:
#         sorted_arr[count[el]] = el
#         count[el] += 1
    
#     return sorted_arr

def test_client():
    # combine w array search code into one client
    n = input("Size of random number array:  ")

    # more elegant way of doing this?
    while(n.isdigit() and int(n) < 1 if n.isdigit() else True):
        n = input('Please provide a positive *integer*: ')

    n = int(n)

    arr = random.choices(population=range(n*2), k=n)  # n*2 is arbitrary to make it more interesting
    print("Pre:", arr)

    # Sort = MergeSort()
    # k = input("k to find k-th smallest value in arr: ")
    # print(f"{k}-th smallest value is {Sort.quick_select(arr, k)}")

    # print(f"\u001b[44m Using {Sort.__str__()} \u001b[0m")  # background color codes
    start = perf_counter()
    print("Post:", selection_sort(arr))
    stop = perf_counter()
    print(f"Elapsed time: {stop - start}")


if __name__ == "__main__":
    test_client()
