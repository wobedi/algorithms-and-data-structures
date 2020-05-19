from random import randint

import perfplot

from src.implementations.dynamic_programming.knapsack_problem \
  import ks_recursive_weight, ks_bottom_up
from src.perf_plots.config import SAMPLE_SIZES

SAMPLE_SIZE = SAMPLE_SIZES['KNAPSACK']

if __name__ == '__main__':
    output = perfplot.bench(
        setup=lambda n: n,
        kernels=[
            lambda n: ks_recursive_weight(
              [randint(1, n * 2) for _ in range(1, n + 1)],
              [randint(1, n * 2) for _ in range(1, n + 1)],
              n * 3
            ),
            lambda n: ks_bottom_up(
              [randint(1, n * 2) for _ in range(1, n + 1)],
              [randint(1, n * 2) for _ in range(1, n + 1)],
              n * 3
            ),
        ],
        labels=['recursive', 'bottom_up'],
        xlabel="N weights and values at N*3 capacity",
        title='Solving the 0-1 Knapsack problem',
        n_range=[n for n in range(1, SAMPLE_SIZE)],
        equality_check=None
    )

    output.save(f'output/knapsack-plot_sample-size-{SAMPLE_SIZE}.png',
                transparent=False,
                bbox_inches="tight")
