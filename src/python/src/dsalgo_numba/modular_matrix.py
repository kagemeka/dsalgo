import numba as nb
import numpy as np


@nb.njit
def dot(mod: int, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    ha, wa = a.shape
    hb, wb = b.shape
    assert wa == hb
    c = np.zeros((ha, wb), np.int64)
    for i in range(ha):
        for j in range(wb):
            c[i, j] = np.sum(a[i] * b[:, j] % mod) % mod
    return c


@nb.njit
def pow_(mod: int, a: np.ndarray, n: int) -> np.ndarray:
    m = len(a)
    assert a.shape == (m, m)
    x = np.eye(m, dtype=np.int64)
    while n:
        if n & 1:
            x = dot(mod, x, a)
        a = dot(mod, a, a)
        n >>= 1
    return x


@nb.njit
def pow_recurse(mod: int, a: np.ndarray, n: int) -> np.ndarray:
    m = len(a)
    assert a.shape == (m, m)
    if n == 0:
        return np.eye(m, dtype=np.int64)
    x = pow_recurse(mod, a, n >> 1)
    x = dot(mod, x, x)
    if n & 1:
        x = dot(mod, x, a)
    return x
