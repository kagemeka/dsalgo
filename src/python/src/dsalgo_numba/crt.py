import typing

import numba as nb
import numpy as np

from .extgcd import extgcd


@nb.njit
def crt(r: np.ndarray, m: np.ndarray) -> tuple[int, int]:
    r0, m0 = 0, 1
    assert r.size == m.size
    for i in range(r.size):
        r1, m1 = r[i], m[i]
        assert m1 >= 1
        r1 %= m1
        if m0 < m1:  # avoid overflow
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        g, p, q = extgcd(m0, m1)
        if (r1 - r0) % g:
            return 0, 0
        u1 = m1 // g
        r0 += (r1 - r0) // g % u1 * p % u1 * m0
        m0 *= u1
        r0 %= m0
    return r0, m0
