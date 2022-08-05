# mypy: ignore-errors

import numpy as np

# slower than argsort
def suffix_array(a: np.array) -> np.array:
    n = a.size
    rank, d = np.searchsorted(np.unique(a), a), 1
    while True:
        rank <<= 25
        rank[:-d] |= 1 + (rank[d:] >> 25)
        rank = np.searchsorted(np.unique(rank), rank)
        d <<= 1
        if d >= n:
            return rank.argsort(kind="mergesort")
