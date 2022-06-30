import typing
import unittest

from dsalgo.factorial_table import factorial_table


def inverse_factorial_table(
    mul: typing.Callable[[int, int], int],
    inv: typing.Callable[[int], int],
    size: int,
) -> typing.List[int]:
    import itertools

    a = list(range(1, size + 1))
    a[-1] = inv(factorial_table(mul, size)[-1])
    return list(itertools.accumulate(a[::-1], mul))[::-1]


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        ifact = inverse_factorial_table(
            lambda x, y: x * y % mod,
            lambda x: pow(x, mod - 2, mod),
            10,
        )
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
        ]


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
