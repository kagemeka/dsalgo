# mypy: ignore-errors

import numpy as np


def suffix_array(a: np.array) -> np.array:
    n = a.size
    rank, d = np.searchsorted(np.unique(a), a), 1
    while True:
        rank <<= 25
        rank[:-d] |= 1 + (rank[d:] >> 25)
        sa = rank.argsort(kind="mergesort")
        d <<= 1
        if d >= n:
            return sa
        rank[sa[0]], rank[sa[1:]] = 0, np.cumsum(rank[sa[1:]] != rank[sa[:-1]])
