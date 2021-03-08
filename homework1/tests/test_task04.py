import pytest

from homework1.task04 import (check_sum_of_four_first_solution,
                              check_sum_of_four_second_solution)


@pytest.mark.parametrize(
    ["input_list_1", "input_list_2", "input_list_3", "input_list_4", "expected_result"],
    [
        ([-20, -30], [20, 30], [-100, -200], [100, 200], 4),
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
    ],
)
def test_chek_sum_of_four_1(
    input_list_1: list,
    input_list_2: list,
    input_list_3: list,
    input_list_4: list,
    expected_result: int,
):
    actual_result = check_sum_of_four_first_solution(
        input_list_1, input_list_2, input_list_3, input_list_4
    )
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["input_list_1", "input_list_2", "input_list_3", "input_list_4", "expected_result"],
    [
        ([-20, -30], [20, 30], [-100, -200], [100, 200], 4),
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
    ],
)
def test_chek_sum_four_2(
    input_list_1: list,
    input_list_2: list,
    input_list_3: list,
    input_list_4: list,
    expected_result: int,
):
    actual_result = check_sum_of_four_second_solution(
        input_list_1, input_list_2, input_list_3, input_list_4
    )
    assert actual_result == expected_result
