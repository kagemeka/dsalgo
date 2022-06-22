# longest common subsequence

import typing
import unittest

T = typing.TypeVar("T")


def dp(
    a: typing.Sequence[T],
    b: typing.Sequence[T],
) -> typing.List[typing.List[int]]:
    n, m = len(a), len(b)
    l = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                l[i + 1][j + 1] = l[i][j] + 1
            else:
                l[i + 1][j + 1] = max(l[i + 1][j], l[i][j + 1])
    return l


def length(dp: typing.List[typing.List[int]]) -> int:
    return dp[-1][-1]


def struct_one(a: typing.Sequence[T], b: typing.Sequence[T]) -> typing.List[T]:
    l = dp(a, b)
    lcs = []
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if l[i][j - 1] == l[i][j]:
            j -= 1
            continue
        if l[i - 1][j] == l[i][j]:
            i -= 1
            continue
        i -= 1
        j -= 1
        lcs.append(a[i])
    return lcs[::-1]


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
