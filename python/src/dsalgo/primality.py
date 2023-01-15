from __future__ import annotations

import math
import random
import typing
import unittest

from dsalgo.psieve import erat_ps

random.seed(1 << 10)

CARMICHAEL_NUMS: typing.Final[list[int]] = [
    561,
    1105,
    1729,
    2465,
    2821,
    6601,
    8911,
    10585,
    15841,
    29341,
    41041,
    46657,
    52633,
    62745,
    63973,
    75361,
    101101,
    115921,
    126217,
    162401,
    172081,
    188461,
    252601,
    278545,
    294409,
    314821,
    334153,
    340561,
    399001,
    410041,
    449065,
    488881,
    512461,
]

_PRIMES = [2, 998_244_353, 1_000_000_007]
_NON_PRIEMS = [0, 1, 561, 512_461]


def trial_division(n: int) -> bool:
    # naive test
    ...


def is_p_t(sz: int) -> list[bool]:
    is_p = [False] * sz
    for p in erat_ps(sz):
        is_p[p] = True
    return is_p


def trivial_primality(n: int) -> typing.Optional[bool]:
    if n == 2:
        return True
    if n < 2 or n & 1 == 0:
        return False
    return None


def mr(n: int) -> bool:
    # miller rabin's test
    MR_BASES = (
        (2, 7, 61),  # < 2^32
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37),  # < 2^64
        (2, 325, 9375, 28178, 450775, 9780504, 1795265022),  # < 2^64
    )

    bl = trivial_primality(n)
    if bl is not None:
        return bl

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = (n - 1) >> s
    # n - 1 = d2^s

    def is_c(b: int) -> bool:
        x = pow(b, d, n)
        if x == 1:
            return False
        for _ in range(s):
            if x == n - 1:
                return False
            x = x * x % n
        return True

    b = (a % n for a in MR_BASES[2])
    return all(not is_c(a) for a in b if 2 <= a and a < n - 1)


class TestMR(unittest.TestCase):
    def test(self) -> None:
        for x in _PRIMES:
            assert mr(x)
        for x in _NON_PRIEMS:
            assert not mr(x)


def fermat(b: typing.Iterable[int], n: int) -> bool:
    # fermat's test
    bl = trivial_primality(n)
    if bl is not None:
        return bl
    b = (a % n for a in b)
    return all(
        math.gcd(n, a) == 1 and pow(a, n - 1, n) == 1
        for a in b
        if 2 <= a and a < n - 1
    )
    # constraint by also gcd to answer for carmichael nums.


class TestFermat(unittest.TestCase):
    def test(self) -> None:
        import random

        bases = [random.randint(0, (1 << 64) - 1) for _ in range(10)]

        for x in _PRIMES:
            assert fermat(bases, x)
        for x in _NON_PRIEMS:
            assert not fermat(bases, x)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
