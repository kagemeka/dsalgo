import numba as nb
import numpy as np


@nb.njit
def matrix_identity(n: int) -> np.ndarray:
    and_e = (1 << 63) - 1
    e = np.zeros((n, n), np.int64)
    for i in range(n):
        e[i, i] = and_e
    return e


@nb.njit
def matrix_dot(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    n, m = a.shape
    h, w = b.shape
    assert m == h
    c = np.zeros((n, w), np.int64)
    for i in range(n):
        for j in range(w):
            for k in range(m):
                c[i, j] ^= a[i, k] & b[k, j]
    return c


@nb.njit
def matrix_power(a: np.ndarray, n: int) -> np.ndarray:
    b = matrix_identity(len(a))
    while n:
        if n & 1:
            b = matrix_dot(b, a)
        a = matrix_dot(a, a)
        n >>= 1
    return b
