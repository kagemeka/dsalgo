import typing

import unittest
from dsalgo.inverse_factorial_table import inverse_factorial_table


def modular_inverse_factorial_table(p: int, size: int) -> typing.List[int]:
    return inverse_factorial_table(
        lambda a, b: a * b % p,
        lambda a: pow(a, p - 2, p),
        size,
    )


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        ifact = modular_inverse_factorial_table(mod, 20)
        assert ifact == [
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


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
