import perfplot

from src.algorithms_and_data_structures.dynamic_programming.fibonacci import (
    fibonacci_recursive, fibonacci_memoized,
    fibonacci_bottom_up, fibonacci_bottom_up_minified
)
from src.performance_plots.config import SAMPLE_SIZES

SAMPLE_SIZE = SAMPLE_SIZES['FIBONACCI']


if __name__ == '__main__':
    output = perfplot.bench(
        setup=lambda n: n,
        kernels=[
            lambda n: fibonacci_recursive(n),
            lambda n: fibonacci_memoized(n, {}),
            lambda n: fibonacci_bottom_up(n, {}),
            lambda n: fibonacci_bottom_up_minified(n)
        ],
        labels=['recursive', 'memoized', 'bottom_up', 'bottom_up_minified'],
        xlabel="n'th Fibonacci number",
        title='Calculating the n\'th Fibonacci number',
        n_range=[n for n in range(1, SAMPLE_SIZE)],
        equality_check=None
    )

    output.save(f'output/fibonacci-plot_sample-size-{SAMPLE_SIZE}.png',
                transparent=False,
                bbox_inches="tight")
