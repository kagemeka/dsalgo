import numba as nb
import numpy as np


@nb.njit
def lcp_array_kasai(a: np.array, sa: np.array) -> np.array:
    n = a.size
    assert n > 0 and sa.size == n
    rank = np.empty(n, np.int64)
    for i in range(n):
        rank[sa[i]] = i
    lcp, h = np.empty(n - 1, np.int64), 0
    for i in range(n):
        if h:
            h -= 1
        r = rank[i]
        if r == n - 1:
            continue
        j = sa[r + 1]
        while i + h < n and j + h < n and a[i + h] == a[j + h]:
            h += 1
        lcp[r] = h
    return lcp
