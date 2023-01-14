from __future__ import annotations

import typing

import dsalgo.order
from dsalgo.type import T

K = typing.TypeVar("K", bound=dsalgo.order.Order)


def binary_search(
    is_ok: typing.Callable[[T], bool],
    arr: list[T],
    lo: int = 0,
    hi: int | None = None,
) -> int:
    if hi is None:
        hi = len(arr)
    assert 0 <= lo <= hi <= len(arr)
    while hi - lo > 0:
        i = (lo + hi - 1) >> 1
        if is_ok(arr[i]):
            hi = i
        else:
            lo = i + 1
    return hi


def bisect_left(arr: list[K], x: K) -> int:
    return binary_search(lambda y: y >= x, arr)


def bisect_right(arr: list[K], x: K) -> int:
    return binary_search(lambda y: y > x, arr)


lower_bound = bisect_left
upper_bound = bisect_right
