"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""

from typing import Any, Callable


def hashable(users_input):
    try:
        hash(users_input)
        return True
    except:
        return False


def make_key(*args: Any, **kwargs: Any):
    hashable_output = []

    if all(map(hashable, args)):
        hashable_output.append(tuple(i for i in args))
    else:
        for arg in args:
            hashable_output.append(make_key(*arg))

    if all(map(hashable, kwargs.values())):
        hashable_output.append(tuple(tuple([i, kwargs[i]]) for i in kwargs))
    else:
        for value in kwargs.values():
            hashable_output.append(tuple([i, make_key(*value)]) for i in kwargs)

    return tuple(hashable_output)


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs):

        key = make_key(*args, *kwargs)

        if key in results:
            return results[key]
        else:
            result = func(*args, **kwargs)
            results[key] = result
            return result

    return wrapper
