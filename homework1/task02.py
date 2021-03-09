"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) == 0:
        return False

    elif data[0] not in (0, 1):
        return False

    elif len(data) > 1 and data[1] != 1:
        return False

    for index, numb in enumerate(data):
        if index > 1:
            if data[index - 2] + data[index - 1] != numb:
                return False

    return True
