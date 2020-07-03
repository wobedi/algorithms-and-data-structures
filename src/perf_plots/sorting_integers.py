from random import sample

import perfplot

from src.implementations.sorting.basic_sorts import \
    selection_sort, insertion_sort, shell_sort
from src.implementations.sorting.heapsort import heapsort
from src.implementations.sorting.mergesort import \
    mergesort_iterative, mergesort_recursive
from src.implementations.sorting.radixsort import radixsort_LSD
from src.perf_plots.config import SAMPLE_SIZES

SAMPLE_SIZE = SAMPLE_SIZES['SORTING_INTEGERS']


if __name__ == '__main__':
    output = perfplot.bench(
        setup=lambda n: sample(range(n + 1), n + 1),
        kernels=[
            lambda a: selection_sort(a),
            lambda a: insertion_sort(a),
            lambda a: shell_sort(a),
            lambda a: heapsort(a),
            lambda a: mergesort_recursive(a),
            lambda a: mergesort_iterative(a),
        ],
        labels=['selection sort', 'insertion sort', 'shell sort', 'heapsort',
                'mergesort (rec)', 'mergesort (itr)'],
        xlabel="Array of N integers in [0, N)",
        title='Sorting an array of integers',
        n_range=range(1, SAMPLE_SIZE),
        equality_check=None
    )

    output.save(f'output/sorting-integers_sample-size-{SAMPLE_SIZE}.png',
                transparent=False,
                bbox_inches="tight")
