import typing

import numba as nb
import numpy as np


@nb.njit
def cumprod(mod: int, arr: np.ndarray) -> np.ndarry:
    r"""Modular cumulative product in place."""
    a = arr.copy()
    for i in range(len(a) - 1):
        a[i + 1] = a[i + 1] * a[i] % mod
    return a


@nb.njit
def factorial(mod: int, n: int) -> np.ndarray:
    r"""Modular factorial table."""
    a = np.arange(n)
    a[0] = 1
    return cumprod(mod, a)


@nb.njit
def factorial_inverse(p: int, n: int) -> np.ndarray:
    r"""Modular factorial inverse table."""
    a = np.arange(1, n + 1)
    a[-1] = inverse_fermat(p, factorial(p, n)[-1])
    cumprod(p, a[::-1])
    return a


@nb.njit
def pow(mod: int, x: int, n: int) -> int:
    r"""Modular power."""
    y = 1
    while n:
        if n & 1:
            y = y * x % mod
        x = x * x % mod
        n >>= 1
    return y


@nb.njit
def pow_recurse(mod: int, x: int, n: int) -> int:
    r"""Modular power recursive implementation."""
    if n == 0:
        return 1
    y = pow_recurse(mod, x, n >> 1)
    y = y * y % mod
    if n & 1:
        y = y * x % mod
    return y


@nb.njit
def pow2_table(mod: int, n: int) -> np.ndarray:
    r"""Power of 2 table over a modulo."""
    a = np.ones(n, np.int64)
    for i in range(n - 1):
        a[i + 1] = a[i] * 2 % mod
    return a


@nb.njit
def inverse_fermat(p: int, n: int) -> int:
    r"""Modular multiplicative inverse with Fermat's little theorem."""
    return pow(p, n, p - 2)


@nb.njit
def inverse_euler(mod: int, n: int) -> int:
    r"""Modular multiplicative inverse with Euler's theorem."""
    assert (
        np.gcd(mod, n) == 1
    ), "Modular multiplicative inverse does not exist."
    return pow(mod, n, euler_totient(mod) - 1)


@nb.njit
def inverse_extgcd(mod: int, a: int) -> int:
    r"""Modular multiplicative inverse with extended Euclidean algorithm."""
    g, p, _ = extgcd(a, mod)
    if g == 1:
        return p % mod
    raise ArithmeticError("Modular multiplicative inverse does not exist.")


@nb.njit
def inverse_table(p: int, n: int) -> np.ndarray:
    r"""Modular multiplicative inverse table."""
    a = factorial_inverse(p, n)
    a[1:] *= factorial(p, n - 1)
    return a % p


@nb.njit
def pow2_inverse_table(p: int, n: int) -> np.ndarray:
    r"""Power of 2 multiplicative inverse table over a prime modulo."""
    inv_2 = (p + 1) >> 1
    a = np.full(inv_2, np.int64)
    a[0] = 1
    cumprod(p, a)
    return a
