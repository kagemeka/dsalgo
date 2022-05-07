import numba as nb
import numpy as np

from ..fft.cooley_turkey.jit import fft

# TODO cut below


@nb.njit((nb.i8[:], nb.i8[:]))
def convolve(
    a: np.ndarray,
    b: np.ndarray,
) -> np.ndarray:
    n = a.size + b.size - 1
    m = 1
    while m < n:
        m <<= 1
    na = np.zeros(m, dtype=np.complex128)
    nb = np.zeros(m, dtype=np.complex128)
    na[: a.size] = a
    nb[: b.size] = b
    a, b = na, nb
    a = fft(a, inverse=False)
    b = fft(b, inverse=False)
    c = fft(a * b, inverse=True)[:n]
    c = np.rint(np.real(c)).astype(np.int64)
    return c
