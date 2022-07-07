import typing
from dsalgo.factorial_table import factorial_table
from dsalgo.inverse_factorial_table import inverse_factorial_table

import unittest


def combination(
    mul: typing.Callable[[int, int], int],
    inv: typing.Callable[[int], int],
    size: int,
) -> typing.Callable[[int, int], int]:
    fact = factorial_table(mul, size)
    ifact = inverse_factorial_table(mul, inv, size)

    def f(n: int, k: int) -> int:
        if not 0 <= k <= n:
            return 0
        return mul(mul(fact[n], ifact[n - k]), ifact[k])

    return f


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        f = combination(
            lambda x, y: x * y % mod, lambda x: pow(x, mod - 2, mod), 100
        )
        assert f(10, 2) == 45


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
