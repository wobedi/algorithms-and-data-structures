def radixsort_LSD(string_list: [str], string_length: int, radix=256) -> [str]:
    """Sorts a list of strings and returns it.
    Characters are compared by their Unicode order, which can lead to
    unexpected results for e.g. lower- and uppercase characters.
    Currently only supports a list of strings of equal length.
    Implements https://en.wikipedia.org/wiki/Radix_sort#Least_significant_digit
    """
    aux = [None for _ in range(len(string_list))]

    for c in range(string_length-1, -1, -1):
        count = [0 for _ in range(radix + 1)]
        for string in string_list:
            # Key-indexed counting
            code_point = ord(string[c])
            count[code_point + 1] += 1
        for r in range(radix):
            # Making count cumulative
            count[r+1] += count[r]
        for string in string_list:
            # Key-indexed sorting
            code_point = ord(string[c])
            aux[count[code_point]] = string
            count[code_point] += 1
        string_list = [s for s in aux]

    return string_list


if __name__ == '__main__':
    string_list = [
        'Testr',
        'Bestr',
        'sistr',
        'brotr',
        'hello',
        'bello',
        'cello',
        'oteee'
    ]
    print(radixsort_LSD(string_list, 5))
    # ['Bestr', 'Testr', 'bello', 'brotr', 'cello', 'hello', 'oteee', 'sistr']
