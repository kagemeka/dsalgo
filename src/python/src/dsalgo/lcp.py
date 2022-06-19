# Longest Common Prefix Array


from __future__ import annotations

import unittest
import typing

L = typing.List


def kasai(a: L[int], sa: L[int]) -> L[int]:
    n = len(a)
    assert n > 0
    rank = [0] * n
    for i, j in enumerate(sa):
        rank[j] = i
    lcp, h = [0] * (n - 1), 0
    for i in range(n):
        if h > 0:
            h -= 1
        r = rank[i]
        if r == n - 1:
            continue
        j = sa[r + 1]
        while i + h < n and j + h < n and a[i + h] == a[j + h]:
            h += 1
        lcp[r] = h
    return lcp


class TestKasai(unittest.TestCase):
    def test(self) -> None:
        import dsalgo.suffix_array

        arr = [1, 0, 3, 3, 0, 3, 3, 0, 2, 2, 0]  # mississippi
        sa = dsalgo.suffix_array.sais_recurse(arr)
        """
        sa|lcp |suffix
        -------------------
        10|None|i
        7 |1   |ippi
        4 |1   |issippi
        1 |4   |ississippi
        0 |0   |mississippi
        9 |0   |pi
        8 |1   |ppi
        6 |0   |sippi
        3 |2   |sissippi
        5 |1   |ssippi
        2 |3   |ssissippi
        """
        lcp = [1, 1, 4, 0, 0, 1, 0, 2, 1, 3]
        kasai(arr, sa) == lcp


if __name__ == "__main__":
    unittest.main()
