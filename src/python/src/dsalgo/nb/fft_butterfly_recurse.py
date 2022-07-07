import numba as nb
import numpy as np


@nb.njit((nb.c16[:], nb.optional(nb.b1)))
def fft(a: np.ndarray, inverse: bool = False) -> np.ndarray:
    n = a.size
    if n == 1:
        return a
    h = 1
    while 1 << h < n:
        h += 1
    assert 1 << h == n

    b = fft(a[::2], inverse)
    c = fft(a[1::2], inverse)

    a = np.zeros(n, dtype=np.complex128)
    sign = -1 + 2 * inverse
    zeta = np.exp(sign * 2j * np.pi / n * np.arange(n))
    m = n // 2
    a[:m] = a[m:] = c
    a *= zeta
    a[:m] += b
    a[m:] += b
    return a


@nb.njit((nb.c16[:],))
def ifft(
    a: np.ndarray,
) -> np.ndarray:
    return fft(a, inverse=True) / a.size
