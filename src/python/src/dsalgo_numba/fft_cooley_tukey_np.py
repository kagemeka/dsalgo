# mypy: ignore-errors


import numpy as np

import unittest


def _butterfly(a: np.ndarray, inverse: bool) -> None:
    n = a.size
    b = 1
    sign = 1 if inverse else -1
    while b < n:
        j = np.arange(b)
        w = np.exp(sign * np.pi / b * j * 1j)
        k = np.arange(0, n, 2 * b)[:, None]
        s, t = a[k + j], a[k + j + b] * w
        a[k + j], a[k + j + b] = s + t, s - t
        b <<= 1


def _reverse_bits(a: np.ndarray) -> None:
    n = a.size
    i = np.arange(n)
    h = n.bit_length() - 1
    assert 1 << h == n
    bits = i[:, None] >> np.arange(h) & 1
    j = (bits[:, ::-1] * (1 << np.arange(h))).sum(axis=1)
    a[:] = a[j]
    # return a[j]


def fft_cooley_tukey(a: np.ndarray, inverse: bool) -> np.ndarray:
    a = a.astype(np.complex128)
    _reverse_bits(a)
    _butterfly(a, inverse)
    if inverse:
        a /= a.size
    return a


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
