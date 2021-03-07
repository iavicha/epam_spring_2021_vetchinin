import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [([1, 1, 2, 3, 5, 8], True), ([1, 1, 2, 3, 5, 7], False)],
)
def test_chek_fibonacci(value: list, expected_result: bool):
    actual_result = check_fibonacci(value)
    assert expected_result == actual_result
