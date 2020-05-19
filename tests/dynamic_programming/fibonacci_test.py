import pytest

from src.implementations.dynamic_programming.fibonacci import (
    fibonacci_recursive, fibonacci_memoized,
    fibonacci_bottom_up, fibonacci_bottom_up_minified
)


@pytest.fixture()
def N():
    return 35


@pytest.fixture()
def RESULT():
    return 9227465  # Fibonacci number 35


def test_fibonacci_recursive(N, RESULT):
    assert fibonacci_recursive(N) == RESULT


def test_fibonacci_memoized(N, RESULT):
    assert fibonacci_memoized(N, {}) == RESULT


def test_fibonacci_bottom_up(N, RESULT):
    assert fibonacci_bottom_up(N, {}) == RESULT


def test_fibonacci_bottom_up_minified(N, RESULT):
    assert fibonacci_bottom_up_minified(N) == RESULT
