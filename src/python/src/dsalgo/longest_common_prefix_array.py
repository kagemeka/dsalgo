from __future__ import annotations


def kasai(arr: list[int], suffix_array: list[int]) -> list[int]:
    n = len(arr)
    assert n > 0
    rank = [0] * n
    for i, j in enumerate(suffix_array):
        rank[j] = i
    lcp, h = [0] * (n - 1), 0
    for i in range(n):
        if h > 0:
            h -= 1
        r = rank[i]
        if r == n - 1:
            continue
        j = suffix_array[r + 1]
        while i + h < n and j + h < n and arr[i + h] == arr[j + h]:
            h += 1
        lcp[r] = h
    return lcp
