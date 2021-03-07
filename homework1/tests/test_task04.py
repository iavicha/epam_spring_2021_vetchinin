import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["input_list_1", "input_list_2", "input_list_3", "input_list_4", "expected_result"],
    [
        ([-20, -30], [20, 30], [-100, -200], [100, 200], 4),
    ],
)
def test_chek_sum_of_for(
    input_list_1: list,
    input_list_2: list,
    input_list_3: list,
    input_list_4: list,
    expected_result: int,
):
    actual_result = check_sum_of_four(
        input_list_1, input_list_2, input_list_3, input_list_4
    )
    assert actual_result == expected_result
