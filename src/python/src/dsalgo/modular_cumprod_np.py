# mypy: ignore-errors


import unittest

import numpy as np

from dsalgo.floor_sqrt import floor_sqrt


def modular_cumprod(mod: int, a: np.ndarray) -> np.ndarray:
    """Compute cumprod over modular not in place.

    the parameter a must be one dimentional ndarray.
    """
    assert a.ndim == 1
    n = a.size
    s = floor_sqrt(n) + 1
    a = np.resize(a, (s, s))
    for i in range(s - 1):
        a[:, i + 1] = a[:, i + 1] * a[:, i] % mod
    for i in range(s - 1):
        a[i + 1] = a[i + 1] * a[i, -1] % mod
    return a.ravel()[:n]


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        a = np.array([-1, 2, 3]) % mod
        res = modular_cumprod(mod, a)
        assert np.all(res == [1000000006, 1000000005, 1000000001])


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
