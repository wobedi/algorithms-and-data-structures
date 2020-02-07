import random
from time import perf_counter

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
    # print("Post:", selection_sort(arr))
    stop = perf_counter()
    print(f"Elapsed time: {stop - start}")


if __name__ == "__main__":
    test_client()
