# mypy: ignore-errors

import typing

import numba as nb
import numpy as np


@nb.njit
def sa_is(a: np.ndarray) -> np.ndarray:
    def preprocess(a):
        n = a.size
        is_s = np.ones(n, np.bool8)
        for i in range(n - 2, -1, -1):
            is_s[i] = is_s[i + 1] if a[i] == a[i + 1] else a[i] < a[i + 1]
        is_lms = np.zeros(n, np.bool8)
        is_lms[1:][~is_s[:-1] & is_s[1:]] = True
        lms = np.flatnonzero(is_lms)
        bucket = np.bincount(a)
        return is_s, is_lms, lms, bucket

    def induce(a, is_s, lms, bucket):
        n, m = a.size, bucket.size
        sa = np.full(n, -1, np.int64)
        sa_idx = bucket.cumsum()
        for i in lms[::-1]:
            sa_idx[a[i]] -= 1
            sa[sa_idx[a[i]]] = i

        sa_idx = bucket.copy()
        s = 0
        for i in range(m):
            s, sa_idx[i] = s + sa_idx[i], s
        for i in range(n):
            i = sa[i] - 1
            if i < 0 or is_s[i]:
                continue
            sa[sa_idx[a[i]]] = i
            sa_idx[a[i]] += 1

        sa_idx = bucket.cumsum()
        for i in range(n - 1, -1, -1):
            i = sa[i] - 1
            if i < 0 or not is_s[i]:
                continue
            sa_idx[a[i]] -= 1
            sa[sa_idx[a[i]]] = i
        return sa

    def compute_lms_rank(a, sa, is_lms):
        n = a.size
        lms_idx = sa[is_lms[sa]]
        l = lms_idx.size
        rank = np.full(n, -1, dtype=np.int64)
        rank[-1] = r = 0
        for i in range(l - 1):
            i, j = lms_idx[i], lms_idx[i + 1]
            for d in range(n):
                i_is_lms = is_lms[i + d]
                j_is_lms = is_lms[j + d]
                if a[i + d] != a[j + d] or i_is_lms ^ j_is_lms:
                    r += 1
                    break
                if d > 0 and i_is_lms | j_is_lms:
                    break
            rank[j] = r
        return rank[rank >= 0]

    a = np.hstack((a - a.min() + 1, np.array([0])))
    st: list[tuple[np.ndarray]] = []
    while True:
        is_s, is_lms, lms, b = preprocess(a)
        sa = induce(a, is_s, lms, b)
        st.append((a, is_s, lms, b))
        a = compute_lms_rank(a, sa, is_lms)
        l = lms.size
        if a.max() < l - 1:
            continue
        lms_order = np.empty(l, np.int64)
        for i in range(l):
            lms_order[a[i]] = i
        break
    while st:
        a, is_s, lms, b = st.pop()
        lms_order = induce(a, is_s, lms[lms_order], b)
    return lms_order[1:]


@nb.njit
def sa_doubling(a: np.array) -> np.array:
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


@nb.njit
def sa_doubling_countsort(a: np.array) -> np.array:
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
