# mypy: ignore-errors


import numba as nb
import numpy as np


@nb.njit
def suffix_array(a: np.array) -> np.array:
    n = a.size

    def counting_sort_key(a):
        cnt = np.zeros(n + 2, dtype=np.int32)
        for x in a:
            cnt[x + 1] += 1
        for i in range(n):
            cnt[i + 1] += cnt[i]
        key = np.empty(n, dtype=np.int32)
        for i in range(n):
            key[cnt[a[i]]] = i
            cnt[a[i]] += 1
        return key

    rank, k = np.searchsorted(np.unique(a), a), 1
    while True:
        second = np.zeros(n, dtype=np.int64)
        second[:-k] = 1 + rank[k:]
        rank_second = counting_sort_key(second)
        first = rank[rank_second]
        rank_first = counting_sort_key(first)
        sa = rank_second[rank_first]
        key = first[rank_first] << 30 | second[sa]
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[i + 1] > key[i])
        k <<= 1
        if k >= n:
            break
    return sa
