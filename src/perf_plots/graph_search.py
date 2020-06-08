from random import randint

import perfplot

from src.implementations.graphs.representations.graph_undirected import Graph
from src.implementations.graphs.operations.graph_search import GraphSearch
from src.perf_plots.config import SAMPLE_SIZES

SAMPLE_SIZE = SAMPLE_SIZES['GRAPH_SEARCH']


def get_graph_for_n(n: int) -> Graph:
    G = Graph(n)
    for v in range(n):
        # connect each vertices to three other random vertices
        G.add_edge(v, randint(0, n - 1))
        G.add_edge(v, randint(0, n - 1))
        G.add_edge(v, randint(0, n - 1))
    return G


if __name__ == '__main__':
    output = perfplot.bench(
        setup=lambda n: get_graph_for_n(n),
        kernels=[
            lambda G: GraphSearch(G, 0, 'bfs'),
            lambda G: GraphSearch(G, 0, 'dfs_recursive'),
            lambda G: GraphSearch(G, 0, 'dfs_iterative'),
        ],
        labels=['Breadth-first', 'Depth-first (recursive)',
                'Depth-first (iterative)'],
        xlabel="Graph with N vertices, randomly connected",
        title='Searching a graph',
        n_range=range(10, SAMPLE_SIZE),
        equality_check=None
    )

    output.save(f'output/graph-search_sample-size-{SAMPLE_SIZE}.png',
                transparent=False,
                bbox_inches="tight")
