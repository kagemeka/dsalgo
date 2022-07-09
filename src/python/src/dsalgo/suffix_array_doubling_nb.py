# mypy: ignore-errors


import numba as nb
import numpy as np


@nb.njit
def suffix_array(a: np.array) -> np.array:
    n = a.size
    rank, k = np.searchsorted(np.unique(a), a), 1
    while True:
        key = rank << 30
        key[:-k] |= 1 + rank[k:]
        sa = key.argsort(kind="mergesort")
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[sa[i + 1]] > key[sa[i]])
        k <<= 1
        if k >= n:
            break
    return sa
