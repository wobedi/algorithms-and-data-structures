from random import randint

import perfplot

from src.implementations.priority_queue.binary_heap import BinaryHeap
from src.perf_plots.config import SAMPLE_SIZES

SAMPLE_SIZE = SAMPLE_SIZES['PRIORITY_QUEUE']


def get_n_random_items(n):
    return [randint(0, n) for _ in range(n)]


def insert_n_items_into_binary_heap(n_items):
    PQ = BinaryHeap()
    for item in n_items:
        PQ.insert(item)


if __name__ == '__main__':
    output = perfplot.bench(
        setup=lambda n: get_n_random_items(n),
        kernels=[
            lambda n_items: insert_n_items_into_binary_heap(n_items)
        ],
        labels=['Binary heap'],
        xlabel="Inserting n items into a priority queue",
        title='Priority Queue',
        n_range=range(1, SAMPLE_SIZE + 1),
        equality_check=None
    )

    output.save(f'output/priority-queue_sample-size-{SAMPLE_SIZE}.png',
                transparent=False,
                bbox_inches="tight")
