def three_way_partition(arr: list, lower: int, upper: int) -> (int, int):
    """In-place partitioning of arr. Implements:
    https://en.wikipedia.org/wiki/Dutch_national_flag_problem#The_array_case
    """
    lt, gt, i = lower, upper, lower
    # Performance could be improved by using smarter pivot, e.g. median
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


if __name__ == '__main__':
    arr = [4, 5, 4, 4, 1, 8, 3, 2, 9, 6]  # [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]
    lt, gt = three_way_partition(arr, 0, len(arr) - 1)
    print(f'lt: {lt}, gt: {gt}')
    assert lt == 3
    assert gt == 5
