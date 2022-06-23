from __future__ import annotations

import heapq

import numba as nb
import pytest

import nb.binary_heap


@pytest.mark.skip(reason="numba error")
@nb.njit(cache=True)
def test() -> None:
    hq = [0] * 0
    hq_std = [0] * 0
    for i in range(10, -1, -1):
        heapq.heappush(hq_std, i)
        nb.binary_heap.heappush(hq, i)
        assert hq == hq_std
        print(hq)
    while hq:
        x, y = nb.binary_heap.heappop(hq), heapq.heappop(hq_std)
        assert x == y and hq == hq_std
        print(x, hq)


if __name__ == "__main__":
    test()
