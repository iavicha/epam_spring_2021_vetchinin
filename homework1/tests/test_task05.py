import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-1, -3, -4, -5, 8, 10, 4, 12, 3, 3], 3, 26),
        ([-1, -2, -3], 3, -1),
    ],
)
def test_find_maximal_subarray_sum(nums: list, k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(nums, k)

    assert actual_result == expected_result
