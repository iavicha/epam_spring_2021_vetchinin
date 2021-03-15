import pytest

from homework2.hw3 import combinations


@pytest.mark.parametrize(
    ["list_to_product", "list_to_product2", "producted"],
    [
        (
            [1, 2],
            [3, 4],
            [
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
            ],
        ),
    ],
)
def test_find_maximum_and_minimum(
    list_to_product: list, list_to_product2: list, producted: list
):
    actual_result = combinations(list_to_product, list_to_product2)

    assert actual_result == producted
