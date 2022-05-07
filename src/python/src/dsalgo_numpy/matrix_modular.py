"""
Algebra
Tensor
"""

import typing

import numpy as np


def dot_np(mod: int, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    assert np.ndim(a) == np.ndim(b) == 2 and a.shape[1] == b.shape[0]
    c = a[:, None, :] * b.T[None, ...] % mod
    return c.sum(axis=-1) % mod


def dot_karatsuba_np(mod: int, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    N: typing.Final[int] = 15
    MASK: typing.Final[int] = (1 << N) - 1
    assert np.ndim(a) == np.ndim(b) == 2 and a.shape[1] == b.shape[0]
    a0, a1 = a & MASK, a >> N
    b0, b1 = b & MASK, b >> N
    c0 = np.dot(a0, b0) % mod
    c2 = np.dot(a1, b1) % mod
    c1 = np.dot(a0 + a1, b0 + b1) - c0 - c2
    c1 %= mod
    c = (c1 << N * 2) + (c1 << N) + c0
    return c % mod


def pow_np(mod: int, a: np.ndarray, n: int) -> np.ndarray:
    m = len(a)
    assert a.shape == (m, m)
    x = np.identity(m, dtype=np.int64)
    while n:
        if n & 1:
            x = dot_karatsuba_np(mod, x, a)
        a = dot_karatsuba_np(mod, a, a)
        n >>= 1
    return x


def pow_recurse_np(mod: int, a: np.ndarray, n: int) -> np.ndarray:
    m = len(a)
    assert a.shape == (m, m)
    if n == 0:
        return np.identity(m, dtype=np.int64)
    x = pow_recurse_np(mod, a, n >> 1)
    x = dot_karatsuba_np(mod, x, x)
    if n & 1:
        x = dot_karatsuba_np(mod, x, a)
    return x
