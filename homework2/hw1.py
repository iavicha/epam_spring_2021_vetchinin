"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""


import re
import string
from typing import List

ACS = [chr(i) for i in range(127)]


def get_longest_diverse_words(file_path: str) -> List[str]:
    words = []
    with open(file_path, "r+", encoding="unicode-escape") as file:
        data = file.read()
        r = re.compile(r"(\w+)")
        words = r.findall(data)
        words = sorted(words, key=len)
        return words[-11:-1]


def get_rarest_char(file_path: str) -> str:
    a = {}
    with open(file_path, "r+", encoding="unicode-escape") as file:
        file = file.read()
        for i in file:
            if i not in a.keys():
                a[i] = file.count(i)
    return min(a, key=a.get)


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "r+", encoding="unicode-escape") as file:
        file = file.read()
        return len([i for i in file if i in string.punctuation])


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as file:
        file = file.read()
        return len([i for i in file if i not in ACS])


def get_most_common_non_ascii_char(file_path: str) -> str:
    d = {}
    with open(file_path, "r", encoding="unicode-escape") as file:
        file = file.read()
        for i in file:
            if i not in ACS and i not in d.keys():
                d[i] = file.count(i)
    return max(d, key=d.get)
