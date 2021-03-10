"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(data, a=None, b=None, c=None):
    if a is not None and b is None and c is None:
        return [i for i in data if i < a]

    elif a is not None and b is not None and c is None:
        return [i for i in data if a <= i < b]

    elif a is not None and b is not None and c > 0:
        result = []
        counter = 0
        for i in data:
            if a <= i < b and counter == 0:
                result.append(i)
                counter += 1
            elif counter < c:
                counter += 1
            elif counter == c:
                counter = 0
                result.append(i)
                counter += 1
        return result

    elif a is not None and b is not None and c < 0:
        c = c * -1
        counter = 0
        result = []
        for i in reversed(data):
            if type(i) != int or float:
                if a >= i > b and counter == 0:
                    result.append(i)
                    counter += 1
                elif counter < c:
                    counter += 1
                elif a >= i > b and counter == c:
                    counter = 0
                    result.append(i)
                    counter += 1
        return result
