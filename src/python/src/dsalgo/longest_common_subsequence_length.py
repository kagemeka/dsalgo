import typing
import unittest

T = typing.TypeVar("T")


def lcs_length(length_dp_table: typing.List[typing.List[int]]) -> int:
    return length_dp_table[-1][-1]


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
