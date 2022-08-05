import typing

import numba as nb
import numpy as np


@nb.njit
def pow2_table(mod: int, n: int) -> np.ndarray:
    r"""Power of 2 table over a modulo."""
    a = np.ones(n, np.int64)
    for i in range(n - 1):
        a[i + 1] = a[i] * 2 % mod
    return a


@nb.njit
def pow2_inverse_table(p: int, n: int) -> np.ndarray:
    r"""Power of 2 multiplicative inverse table over a prime modulo."""
    inv_2 = (p + 1) >> 1
    a = np.full(inv_2, np.int64)
    a[0] = 1
    cumprod(p, a)
    return a
