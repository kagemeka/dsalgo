import numba as nb
import numpy as np


@nb.njit((nb.c16[:], nb.optional(nb.b1)))
def fft(a: np.ndarray, inverse: bool = False) -> np.ndarray:
    n = a.size
    h = 1
    while 1 << h < n:
        h += 1
    assert 1 << h == n

    def reverse_bits():
        idx = np.empty(n, dtype=np.int64)
        for i in range(n):
            j = 0
            for k in range(h):
                j |= (i >> k & 1) << (h - 1 - k)
            idx[i] = j
        nonlocal a
        a = a[idx]

    def butterfly():
        sign = -1 + 2 * inverse
        b = 1
        while b < n:
            for j in range(b):
                w = np.exp(sign * np.pi / b * j * 1j)
                for k in range(0, n, 2 * b):
                    s, t = a[k + j], a[k + j + b] * w
                    a[k + j], a[k + j + b] = s + t, s - t
            b <<= 1

    reverse_bits()
    butterfly()
    if inverse:
        a /= n
    return a
