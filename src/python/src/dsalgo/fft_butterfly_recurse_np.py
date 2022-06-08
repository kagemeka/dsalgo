"""Mypy Inline Configs.
see https://mypy.readthedocs.io/en/stable/inline_config.html
in all the files importing external untyped packages, disable mypy checks.
# mypy: ignore-errors
"""


import numpy as np

import unittest


def fft_butterfly_inplace_recurse(a: np.ndarray, inverse: bool) -> None:
    n = a.size
    if n == 1:
        return
    b = a[::2]
    c = a[1::2]
    fft_butterfly_inplace_recurse(b, inverse)
    fft_butterfly_inplace_recurse(c, inverse)
    sign = -1 + 2 * inverse
    m = n >> 1
    zeta = np.exp(sign * 2j * np.pi / n * np.arange(n))
    a[:m], a[m:] = b + zeta[:m] * c, b + zeta[m:] * c


def fft_butterfly_inverse_inplace(a: np.ndarray) -> None:
    fft_butterfly_inplace_recurse(a, inverse=True)
    a /= a.size


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
