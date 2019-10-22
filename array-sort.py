from random import choices, shuffle
from time import perf_counter

# add explainer links for algos?
# fix function order in a way that make sense
# TODO: Implement proper testing
# TODO: Github


def selection_sort(arr):
    for i in range(0, len(arr)):
        min_ = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_]:
                min_ = j
        arr[i], arr[min_] = arr[min_], arr[i]
    return arr


def insertion_sort(arr, increment=1):
    for i in range(increment, len(arr)):
        for j in range(i - increment, -1, -increment):
            if arr[j] > arr[j+increment]:
                arr[j+increment], arr[j] = arr[j], arr[j+increment]
            else:
                break
    return arr


def shell_sort(arr):
    seq = reversed(list(knuth_3xplus1_sequence(len(arr))))
    for increment in seq:
        insertion_sort(arr, increment=increment)


def knuth_3xplus1_sequence(arr_len):
    x = 1
    while(x < arr_len):
        yield x
        x = 3*x + 1


class MergeSort():
    def __str__(self):
        return "MergeSort"

    def merge_sort_recursive(self, arr):
        if len(arr) <= 1:
            return arr
        lo, mid, hi = 0, len(arr) // 2, len(arr)
        left = self.merge_sort_recursive(arr[lo:mid])
        right = self.merge_sort_recursive(arr[mid:hi])

        return self._sort_merge(left, right)

    def merge_sort_iterative(self, arr):
        # "bottom-up merge sort"
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


class QuickSort():
    def __str__(self):
        return "QuickSort"

    # MOVE TO ARRAY SEARCH MODULE?
    def quick_select(self, arr, k):
        k = int(k)
        if k > len(arr):
            return f"Error - k is {k} but array length is {len(arr)}"
        aux = arr.copy()  # Using an aux arr to not modify the original arr
        self.random_shuffle(aux)
        return self._quick_select(aux, k, lower=0, upper=len(arr)-1)

    # optimize via Use insertion sort for small (e.g. <10) sub-arrays to avoid the overhead of QS // AND use median of three as pivot
    # choose between median of 3 and turkey's ninther
    # THEN no random shuffle
    def quick_sort(self, arr):
        self.random_shuffle(arr)
        print("Shuffled: ", arr)
        return self._quick_sort_in_place(arr, lower=0, upper=len(arr)-1)

    def random_shuffle(self, arr):
        return shuffle(arr)

    def _quick_select(self, arr, k, lower, upper):
        lt, gt = self._partition_in_place(arr, lower, upper)
        if k in range(lt, gt+1):
            print("Final arr: ", arr)
            return arr[gt]  # arbitrary, any value between [l,r] would work
        elif k < lt:
            return self._quick_select(arr, k, lower, lt-2)
        elif k > gt:
            return self._quick_select(arr, k, gt, upper) 

    def _quick_sort_aux_arr(self, arr):
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

    def _quick_sort_in_place(self, arr, lower, upper):
        if upper <= lower:
            return
        lt, gt = self._partition_in_place(arr, lower, upper)
        self._quick_sort_in_place(arr, lower, lt-1)
        self._quick_sort_in_place(arr, gt+1, upper)
        return arr

    def _partition_in_place(self, arr, lower, upper):
        # dijkstra's 3-way partitioning
        lt, gt, i = lower, upper, lower
        pivot = arr[lower]

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


def test_client():
    # combine w array search code into one client
    n = input("Size of random number array:  ")

    # more elegant way of doing this?
    while(n.isdigit() and int(n) < 1 if n.isdigit() else True):
        n = input('Please provide a positive *integer*: ')

    n = int(n)

    arr = choices(population=range(n*2), k=n)  # n*2 is arbitrary to make it more interesting
    print("Pre:", arr)

    Sort = QuickSort()
    # k = input("k to find k-th smallest value in arr: ")
    # print(f"{k}-th smallest value is {Sort.quick_select(arr, k)}")

    print(f"\u001b[44m Using {Sort.__str__()} \u001b[0m")  # background color codes
    start = perf_counter()
    print("Post:", Sort.quick_sort(arr))
    stop = perf_counter()
    print(f"Elapsed time: {stop - start}")


if __name__ == "__main__":
    test_client()
