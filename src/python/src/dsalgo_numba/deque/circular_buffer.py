"""Mypy Inline Configs.
see https://mypy.readthedocs.io/en/stable/inline_config.html
# mypy: disallow-untyped-defs = False
# mypy:
"""
from __future__ import annotations

import numba
import numpy as np

# from numpy import typing as npt


@numba.njit
def deque_circular_buffer(max_size: int) -> tuple:
    left = 0
    right = 0
    size = 0

    def is_empty():
        return size == 0

    def append_left(data, x):
        nonlocal left
        left -= 1
        data[left] = x
        print(left, data)

    def append_right(data, x):
        nonlocal right
        data[right] = x
        right += 1

    def pop_left(data):
        nonlocal left
        value = data[left]
        left += 1
        return value

    def pop_right(data):
        nonlocal right
        right -= 1
        value = data[right]
        return value

    return append_left, append_right, pop_left, pop_right


# data = np.zeros(10, np.int64)
# append_left, append_right, pop_left, pop_right = deque_circular_buffer(10)
# append_left(data, 1)
# print(data)
# append_right(data, 2)
# print(data)
# print(pop_right(data))
# print(pop_right(data))
