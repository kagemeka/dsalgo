# mypy: ignore-errors


import unittest

import numpy as np

from dsalgo.modular_cumprod_np import modular_cumprod


def modular_factorial_table(mod: int, size: int) -> np.ndarray:

    a = np.arange(size)
    a[0] = 1
    return modular_cumprod(mod, a)


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        fact = modular_factorial_table(mod, 20)
        assert np.all(
            fact
            == np.array(
                [
                    1,
                    1,
                    2,
                    6,
                    24,
                    120,
                    720,
                    5040,
                    40320,
                    362880,
                    3628800,
                    39916800,
                    479001600,
                    227020758,
                    178290591,
                    674358851,
                    789741546,
                    425606191,
                    660911389,
                    557316307,
                ]
            )
        )


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
