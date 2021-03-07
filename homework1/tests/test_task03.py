import os
import random

import pytest

from homework1.task03 import find_maximum_and_minimum

keys = []


def make_test_file_please():
    os.remove("homework1/tests/test_file.txt")
    global keys

    result = []

    with open("homework1/tests/test_file.txt", "a") as file:
        for i in range(10):
            for z in range(10):
                result.append(random.randint(2, 100))
            keys.append(min(result))
            keys.append(max(result))
            result = str(result)
            file.write(result + "\n")
            result = []
    return keys


make_test_file_please()


@pytest.mark.parametrize(
    ["some_file", "expected_result"],
    [
        ("homework1/tests/test_file.txt", (min(keys), max(keys))),
    ],
)
def test_find_maximum_and_minimum(some_file: str, expected_result: tuple):
    actual_result = find_maximum_and_minimum(some_file)

    assert actual_result == expected_result
