import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "value1", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-1, -3, -4, -5, 8, 10, 4, 12, 3, 3], 3, 26),
        ([-1, -2, -3], 3, -1),
    ],
)
def test_find_maximal_subarray_sum(value: list, value1: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(value, value1)

    assert actual_result == expected_result
