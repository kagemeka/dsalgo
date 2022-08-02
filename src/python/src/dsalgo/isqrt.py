import unittest


# binary search
def isqrt(n: int) -> int:
    assert 0 <= n < 1 << 64
    lo, hi = 0, min(1 << 32, n + 1)
    while hi - lo > 1:
        x = (lo + hi) >> 1
        if x * x <= n:
            lo = x
        else:
            hi = x
    return lo


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
