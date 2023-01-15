# mypy: ignore-errors


import typing
import unittest

import numpy as np


def cumprod(mod: int, a: np.ndarray) -> np.ndarray:
    assert a.ndim == 1
    n = a.size
    s = int(n**0.5) + 1
    a = np.resize(a, (s, s))
    for i in range(s - 1):
        a[:, i + 1] = a[:, i + 1] * a[:, i] % mod
    for i in range(s - 1):
        a[i + 1] = a[i + 1] * a[i, -1] % mod
    return a.ravel()[:n]


def make_factorials(p: int, size: int) -> typing.Tuple[np.ndarray, np.ndarray]:
    fact = np.arange(size)
    fact[0] = 1
    fact = cumprod(p, fact)
    ifact = np.arange(size, 0, -1)
    ifact[0] = pow(int(fact[-1]), -1, p)
    return fact, cumprod(p, ifact)[::-1]


class FactorialTablesFrequentOps:
    mod: int
    fact: np.ndarray
    ifact: np.ndarray

    def __init__(self, p: int, size: int) -> None:
        self.mod = p
        self.fact, self.ifact = make_factorials(p, size)

    def p(self, n: np.ndarray, k: np.ndarray) -> np.ndarray:
        ok = (0 <= k) & (k <= n)
        return ok * self.fact[n] * self.ifact[n - k] % self.mod

    def c(self, n: np.ndarray, k: np.ndarray) -> np.ndarray:
        return self.p(n, k) * self.ifact[k] % self.mod

    def h(self, n: np.ndarray, k: np.ndarray) -> np.ndarray:
        return self.c(n - 1 + k, k)

    def inv(self, n: np.ndarray) -> np.ndarray:
        return self.fact[n - 1] * self.ifact[n] % self.mod

    def inv_p(self, n: np.ndarray, k: np.ndarray) -> np.ndarray:
        ok = (0 <= k) & (k <= n)
        return ok * self.ifact[n] * self.fact[n - k] % self.mod

    def inv_c(self, n: np.ndarray, k: np.ndarray) -> np.ndarray:
        return self.inv_p(n, k) * self.fact[k] % self.mod


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        fact, ifact = make_factorials(mod, 10)
        f = FactorialTablesFrequentOps(mod, 100)
        print(f.c(np.arange(10)[:, None], np.arange(10)))


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
