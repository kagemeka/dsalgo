# mypy: ignore-errors


import unittest


import numpy as np

from dsalgo.modular_factorial_table_np import modular_factorial_table
from dsalgo.modular_inverse_factorial_table_np import (
    modular_inverse_factorial_table,
)


class ModularCombination:
    __mod: int
    __fact: np.ndarray
    __ifact: np.ndarray

    @property
    def mod(self) -> int:
        return self.__mod

    def __init__(self, mod: int, size: int) -> None:
        self.__mod = mod
        self.__fact = modular_factorial_table(mod, size)
        self.__ifact = modular_inverse_factorial_table(mod, size)

    def __call__(self, n: np.ndarray, k: np.ndarray) -> int:
        ok = (0 <= k) & (k <= n)
        return (
            self.__fact[n]
            * self.__ifact[n - k]
            % self.mod
            * self.__ifact[k]
            % self.mod
            * ok
        )

    def inv(self, n: np.ndarray, k: np.ndarray) -> int:
        ok = (0 <= k) & (k <= n)
        assert np.all(ok)
        return (
            self.__ifact[n]
            * self.__fact[n - k]
            % self.mod
            * self.__fact[k]
            % self.mod
        )


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        size = 1 << 10
        choose = ModularCombination(mod, size)
        n = np.arange(100)[:, None]
        k = np.arange(100)[None, :]
        res = choose(n, k)
        assert res[99][2] == 4851


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
