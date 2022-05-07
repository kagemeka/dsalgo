import numpy as np


def cumprod_np(a: np.ndarray, mod: int) -> np.ndarray:
    """Compute cumprod over modular not in place.

    the parameter a must be one dimentional ndarray.
    """
    n = a.size
    assert a.ndim == 1
    m = int(n**0.5) + 1
    a = np.resize(a, (m, m))
    for i in range(m - 1):
        a[:, i + 1] = a[:, i + 1] * a[:, i] % mod
    for i in range(m - 1):
        a[i + 1] = a[i + 1] * a[i, -1] % mod
    return a.ravel()[:n]


def factorial_np(n: int, mod: int) -> np.ndarray:
    a = np.arange(n)
    a[0] = 1
    return cumprod_np(a, mod)


def factorial_inverse_np(n: int, mod: int) -> np.ndarray:
    a = np.arange(1, n + 1)
    a[-1] = inverse(int(factorial_np(n, mod)[-1]), mod)
    return cumprod_np(a[::-1], mod)[::-1]


def inverse_table_np(n: int, mod: int) -> np.ndarray:
    a = factorial_inverse_np(n, mod)
    a[1:] *= factorial_np(n - 1, mod)
    return a % mod
