from pandas import DataFrame
import pytest

from src.implementations.dynamic_programming.knapsack_problem \
    import ks_recursive_weight, ks_bottom_up


@pytest.fixture()
def weights():
    return [2, 4, 5, 7, 9]


@pytest.fixture()
def values():
    return [3, 5, 6, 8, 10]


@pytest.fixture()
def capacity():
    return 20


@pytest.fixture()
def solution_weight():
    return 24


@pytest.fixture()
def solution_items():
    return [5, 3, 2, 1]


def test_ks_recursive_weight(weights, values, capacity, solution_weight):
    total_weight_of_solution = ks_recursive_weight(weights, values, capacity)
    assert total_weight_of_solution == solution_weight


def test_ks_bottom_up(weights, values, capacity, solution_items, printer):
    cache, items = ks_bottom_up(weights, values, capacity)
    printer(f'BOTTOM-UP KNAPSACK CACHE:\n{DataFrame(cache)}')
    assert items == solution_items
