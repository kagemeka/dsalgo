from __future__ import annotations

import typing

import numba as nb
import numpy as np

T = typing.TypeVar("T")


@nb.njit
def heappush(hq: list[T], x: T) -> None:
    i = len(hq)
    hq.append(x)
    while i > 0:
        j = (i - 1) >> 1
        if hq[i] >= hq[j]:
            break
        hq[i], hq[j] = hq[j], hq[i]
        i = j


@nb.njit
def heappop(hq: list[T]) -> T:
    hq[0], hq[-1] = hq[-1], hq[0]
    x = hq.pop()
    i, n = 0, len(hq)
    while 1:
        j = (i << 1) | 1
        if j >= n:
            break
        j += j < n - 1 and hq[j + 1] < hq[j]
        if hq[i] <= hq[j]:
            break
        hq[i], hq[j] = hq[j], hq[i]
        i = j
    return x
