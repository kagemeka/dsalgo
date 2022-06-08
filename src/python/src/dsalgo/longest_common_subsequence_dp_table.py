import typing
import unittest

T = typing.TypeVar("T")


def lcs_dp_table(
    a: typing.Sequence[T],
    b: typing.Sequence[T],
) -> typing.List[typing.List[int]]:
    n, m = len(a), len(b)
    length = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                length[i + 1][j + 1] = length[i][j] + 1
            else:
                length[i + 1][j + 1] = max(length[i + 1][j], length[i][j + 1])
    return length


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
