# integer sqrt

import unittest


# linear naive
def naive(n: int) -> int:
    assert n >= 0
    x = 0
    while x * x <= n:
        x += 1
    return x - 1


# binary search
def binsrch(n: int) -> int:
    assert 0 <= n < 1 << 64
    lo, hi = 0, min(1 << 32, n + 1)
    while hi - lo > 1:
        x = (lo + hi) >> 1
        if x * x <= n:
            lo = x
        else:
            hi = x
    return lo


# newton's method
def newton(n: int) -> int:
    ...


def floor(n: int) -> int:
    return binsrch(n)


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
