import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("homework1/some_file.txt", (1, 5)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: tuple):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
