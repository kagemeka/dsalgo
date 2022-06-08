import unittest
from dsalgo.int_sqrt_binary_search import int_sqrt_binary_search


def floor_sqrt(n: int) -> int:
    return int_sqrt_binary_search(n)


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
