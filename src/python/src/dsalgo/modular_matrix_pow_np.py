"""Mypy Inline Configs.
see https://mypy.readthedocs.io/en/stable/inline_config.html
in all the files importing external untyped packages, disable mypy checks.
# mypy: ignore-errors
"""


import numpy as np

import unittest
from dsalgo.modular_matrix_dot_karatsuba_np import dot_karatsuba


def pow(mod: int, a: np.ndarray, n: int) -> np.ndarray:
    m = len(a)
    assert a.shape == (m, m)
    x = np.identity(m, dtype=np.int64)
    while n:
        if n & 1:
            x = dot_karatsuba(mod, x, a)
        a = dot_karatsuba(mod, a, a)
        n >>= 1
    return x


def pow_recurse(mod: int, a: np.ndarray, n: int) -> np.ndarray:
    m = len(a)
    assert a.shape == (m, m)
    if n == 0:
        return np.identity(m, dtype=np.int64)
    x = pow_recurse(mod, a, n >> 1)
    x = dot_karatsuba(mod, x, x)
    if n & 1:
        x = dot_karatsuba(mod, x, a)
    return x


# TODO:
class Test(unittest.TestCase):
    def test(self) -> None:
        # MOD = 1_000_000_007
        ...


if __name__ == "__main__":
    import unittest

    unittest.main()
