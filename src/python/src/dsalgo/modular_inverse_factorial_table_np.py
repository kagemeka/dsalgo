# mypy: ignore-errors


import unittest

import numpy as np

from dsalgo.modular_cumprod_np import modular_cumprod
from dsalgo.modular_factorial_table_np import modular_factorial_table
from dsalgo.modular_inverse_extgcd import modular_inverse_extgcd


def modular_inverse_factorial_table(mod: int, size: int) -> np.ndarray:
    a = np.arange(1, size + 1)
    a[-1] = modular_inverse_extgcd(
        mod,
        int(modular_factorial_table(mod, size)[-1]),
    )
    return modular_cumprod(mod, a[::-1])[::-1]


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        ifact = modular_inverse_factorial_table(mod, 20)
        assert np.all(
            ifact
            == np.array(
                [
                    1,
                    1,
                    500000004,
                    166666668,
                    41666667,
                    808333339,
                    301388891,
                    900198419,
                    487524805,
                    831947206,
                    283194722,
                    571199524,
                    380933296,
                    490841026,
                    320774361,
                    821384963,
                    738836565,
                    514049213,
                    639669405,
                    402087866,
                ]
            )
        )


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
