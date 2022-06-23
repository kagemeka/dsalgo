import numba as nb
import numpy as np
from dsa.algebra.modular.inverse.ext_gcd.jit import mod_inv

# TODO cut below


@nb.njit((nb.i8[:], nb.i8[:], nb.i8), cache=True)
def garner_calc_x_mod(
    r: np.ndarray,
    m: np.ndarray,
    mod: int,
) -> int:
    n = r.size
    assert m.size == n
    m = np.hstack((m, np.array([mod])))
    s = np.zeros(n + 1, np.int64)
    m_prod = np.full(n + 1, 1, np.int64)
    for i in range(n):
        t = (r[i] - s[i]) * mod_inv(m_prod[i], m[i]) % m[i]
        s[i + 1 :] += t * m_prod[i + 1 :]
        s %= m
        m_prod = m_prod * m[i] % m
    return s[-1]


@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def garner_restore_x(
    r: np.ndarray,
    m: np.ndarray,
) -> int:
    n = r.size
    assert m.size == n
    x = 0
    m_prod = 1
    for i in range(n):
        t = (r[i] - x) * mod_inv(m_prod, m[i]) % m[i]
        x += t * m_prod
        m_prod *= m[i]
    return x
