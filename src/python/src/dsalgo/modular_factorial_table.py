import typing

import unittest
from dsalgo.factorial_table import factorial_table


def modular_factorial_table(mod: int, size: int) -> typing.List[int]:
    return factorial_table(lambda a, b: a * b % mod, size)


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        fact = modular_factorial_table(mod, 20)
        assert fact == [
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


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
