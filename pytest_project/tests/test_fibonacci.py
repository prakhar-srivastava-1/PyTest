from source.fibonacci import fibonacci
import pytest


def test_fibonacci():
    """tests fibonacci numbers"""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 14, "mismatch; test failed"


# convert the above test into a parametrized test
@pytest.mark.parametrize(
    "nth_term, fibonacci_number",
    [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 14)],
)
def test_fibonacci_parametrized(nth_term, fibonacci_number):
    assert fibonacci(nth_term) == fibonacci_number
