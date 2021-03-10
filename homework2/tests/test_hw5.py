import string

import pytest

from homework2.hw5 import custom_range


@pytest.mark.parametrize(
    ["data", "a", "b", "c", "expected_result"],
    [
        (string.ascii_lowercase, "g", None, None, ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            "g",
            "p",
            None,
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(data: iter, a: any, b: any, c: any, expected_result: list):
    actual_result = custom_range(data, a, b, c)

    assert actual_result == expected_result
