import typing
import unittest

T = typing.TypeVar("T")


def struct_lcs(
    a: typing.Sequence[T],
    b: typing.Sequence[T],
    length_dp_table: typing.List[typing.List[int]],
) -> typing.List[T]:
    length = length_dp_table
    lcs = []
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if length[i][j - 1] == length[i][j]:
            j -= 1
            continue
        if length[i - 1][j] == length[i][j]:
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
