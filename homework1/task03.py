"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    result = []
    min_max_result = []

    with open(file_name, "r") as file:
        for line in file:
            result = [
                int(i)
                for i in line.replace("[", "")
                .replace("]", "")
                .replace(" ", "")
                .split(",")
            ]
            print(result)
            print(file)
            min_max_result.append(min(result))
            min_max_result.append(max(result))
    return min(min_max_result), max(min_max_result)
