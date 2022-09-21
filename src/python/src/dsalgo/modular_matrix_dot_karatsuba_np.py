"""Mypy Inline Configs.
see https://mypy.readthedocs.io/en/stable/inline_config.html
in all the files importing external untyped packages, disable mypy checks.
# mypy: ignore-errors
"""


import unittest

import numpy as np


def mul(mod: int, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    B = 16
    MASK = (1 << B) - 1
    assert np.ndim(a) == np.ndim(b) == 2 and a.shape[1] == b.shape[0]
    assert 0 < mod < 1 << (B << 1)
    a %= mod
    b %= mod
    a0, a1, b0, b1 = a & MASK, a >> B, b & MASK, b >> B
    c0 = np.dot(a0, b0) % mod
    c2 = np.dot(a1, b1) % mod
    c1 = np.dot(a0 + a1, b0 + b1) - c0 - c2
    c1 %= mod
    c = (c2 << (B << 1)) + (c1 << B) + c0
    return c % mod


def power(mod: int, a: np.ndarray, n: int) -> np.ndarray:
    if n == 0:
        m = len(a)
        return np.eye(m, dtype=np.int64)
    y = power(mod, a, n >> 1)
    y = mul(mod, y, y)
    if n & 1:
        y = mul(mod, y, a)
    return y


class Test(unittest.TestCase):
    def test(self) -> None:
        MOD = 1_000_000_007
        a = np.array([[-1, 0], [0, -1]])
        b = np.array([[0, 1, 1], [1, 0, 1]])
        print(a)
        print(b)
        print(mul(MOD, a, b))
        ans = np.array([[0, -1, -1], [-1, 0, -1]])
        ans %= MOD
        assert np.all(mul(MOD, a, b) == ans)


if __name__ == "__main__":
    import unittest

    unittest.main()
