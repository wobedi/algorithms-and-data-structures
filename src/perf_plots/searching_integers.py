from random import sample

import perfplot

from src.implementations.symbol_tables.binary_search_tree import \
    BinarySearchTree
from src.implementations.symbol_tables.hash_map_w_chaining import \
    HashMap
from src.implementations.symbol_tables.hash_set_w_probing import \
    HashSet
from src.implementations.symbol_tables.red_black_bst import \
    RedBlackTree
from src.perf_plots.config import SAMPLE_SIZES

SAMPLE_SIZE = SAMPLE_SIZES['SEARCHING_INTEGERS']


def get_symbol_tables(n: int) -> {}:
    random_integer_sample = sample(range(n + 1), n + 1)
    HM_CHAINING = HashMap(2)
    HS_PROBING = HashSet(2)
    BST = BinarySearchTree()
    RBT = RedBlackTree()

    for i in random_integer_sample:
        HM_CHAINING.put(i, i)
        HS_PROBING.put(i)
        BST.put(i, i)
        RBT.put(i, i)

    return {
        'HM_CHAINING': HM_CHAINING,
        'HS_PROBING': HS_PROBING,
        'BST': BST,
        'RBT': RBT,
    }


def search_for_integer_in_symbol_table(symbol_table, n):
    try:
        symbol_table.get(n)
    except:
        symbol_table.contains(n)


if __name__ == '__main__':
    output = perfplot.bench(
        setup=lambda n: get_symbol_tables(n),
        kernels=[
            lambda ST: search_for_integer_in_symbol_table(
                ST['HM_CHAINING'], 1),
            lambda ST: search_for_integer_in_symbol_table(
                ST['HS_PROBING'], 1),
            lambda ST: search_for_integer_in_symbol_table(
                ST['BST'], 1),
            lambda ST: search_for_integer_in_symbol_table(
                ST['RBT'], 1)
        ],
        labels=[
            'HashMap with separate chaining',
            'HashSet with linear probing',
            'Binary Search Tree',
            'Red-Black Tree'
        ],
        xlabel="Searching for one integer in a collection of N integers",
        title='Integer search',
        n_range=range(1, SAMPLE_SIZE),
        equality_check=None
    )

    output.save(f'output/searching-integers_sample-size-{SAMPLE_SIZE}.png',
                transparent=False,
                bbox_inches="tight")
