from __future__ import annotations

from dsalgo.type import T


def z_algorithm(arr: list[T]) -> list[int]:
    n = len(arr)
    a = [0] * n
    a[0] = n
    left = right = -1
    for i in range(1, n):
        if right >= i:
            a[i] = min(a[i - left], right - i)
        while i + a[i] < n and arr[i + a[i]] == arr[a[i]]:
            a[i] += 1
        if i + a[i] >= right:
            left, right = i, i + a[i]
    return a
