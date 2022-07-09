from __future__ import annotations

import dsalgo.array_compression
import dsalgo.sort


def doubling(arr: list[int]) -> list[int]:
    n = len(arr)
    rank, k = dsalgo.array_compression.compress(arr).compressed_array, 1
    while True:
        key = [r << 30 for r in rank]
        for i in range(n - k):
            key[i] |= 1 + rank[i + k]
        sa = sorted(range(n), key=lambda x: key[x])
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[sa[i + 1]] > key[sa[i]])
        k <<= 1
        if k >= n:
            break
    return sa


def doubling_counting_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    rank, k = dsalgo.array_compression.compress(arr).compressed_array, 1
    while True:
        second_key = [0] * n
        for i in range(n - k):
            second_key[i] = 1 + rank[i + k]
        order_second = dsalgo.sort.counting_sort_index(second_key)
        first_key = [rank[i] for i in order_second]
        order_first = dsalgo.sort.counting_sort_index(first_key)
        suffix_array = [order_second[i] for i in order_first]
        key = [
            first_key[i] << 30 | second_key[j]
            for i, j in zip(order_first, suffix_array)
        ]
        rank[suffix_array[0]] = 0
        for i in range(n - 1):
            rank_delta = int(key[i + 1] > key[i])
            rank[suffix_array[i + 1]] = rank[suffix_array[i]] + rank_delta
        k <<= 1
        if k >= n:
            break
    return suffix_array
