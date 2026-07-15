from __future__ import annotations

from functools import wraps
from time import perf_counter


def timed(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):

        start = perf_counter()

        result = fn(*args, **kwargs)

        duration = perf_counter() - start

        return result, duration * 1000

    return wrapper
