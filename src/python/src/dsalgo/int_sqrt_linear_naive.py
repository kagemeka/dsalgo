import unittest


def int_sqrt_linear_naive(n: int) -> int:
    assert n >= 0
    x = 0
    while x * x <= n:
        x += 1
    return x - 1


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
