import numba as nb
import numpy as np


@nb.njit
def mod_fibonacci_sequence(n: int, mod: int) -> np.ndarray:
    assert n >= 2
    f = np.empty(n, np.int64)
    f[0], f[1] = 0, 1
    for i in range(2, n):
        f[i] = (f[i - 1] + f[i - 2]) % mod
    return f


@nb.njit
def mod_tribonacci_sequence(n: int, mod: int) -> np.ndarray:
    assert n >= 3
    t = np.zeros(n, np.int64)
    t[2] = 1
    for i in range(3, n):
        t[i] = (t[i - 1] + t[i - 2] + t[i - 3]) % mod
    return t
