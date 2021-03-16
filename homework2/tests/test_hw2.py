import pytest

from homework2.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["input", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ],
)
def test_custom_range(input, expected_result):
    actual_result = major_and_minor_elem(input)

    assert actual_result == expected_result
