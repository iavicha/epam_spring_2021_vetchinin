import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["value", "value1", "value2", "value3", "expected_result"],
    [
        ([-20, -30], [20, 30], [-100, -200], [100, 200], 4),
    ],
)
def test_chek_sum_of_for(
    value: list, value1: list, value2: list, value3: list, expected_result: int
):
    actual_result = check_sum_of_four(value, value1, value2, value3)
    assert actual_result == expected_result
