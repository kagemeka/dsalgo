from __future__ import annotations

import math
import random
import re
import typing


def is_prime(n: int) -> bool:
    # naive test
    ...


def sieve_of_eratosthenes(sieve_size: int) -> list[bool]:
    assert sieve_size > 1
    is_prime = [True] * sieve_size
    is_prime[0] = is_prime[1] = False
    for i in range(2, sieve_size):
        if i * i >= sieve_size:
            break
        if not is_prime[i]:
            continue
        for j in range(i * i, sieve_size, i):
            is_prime[j] = False
    return is_prime


def is_prime_table(size: int) -> list[bool]:
    return sieve_of_eratosthenes(size)


def trivial_primality(n: int) -> typing.Optional[bool]:
    if n == 2:
        return True
    if n < 2 or n & 1 == 0:
        return False
    return None


def mr(n: int) -> bool:
    MR_BASES = (
        (2, 7, 61),  # < 2^32
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37),  # < 2^64
        (2, 325, 9375, 28178, 450775, 9780504, 1795265022),  # < 2^64
    )

    bl = trivial_primality(n)
    if bl is not None:
        return bl

    def is_c(b: int) -> bool:
        assert n >= 3
        r, d = 0, n - 1
        while d & 1 == 0:
            r += 1
            d >>= 1
        # n - 1 = d2^r
        x = pow(b, d, n)
        if x == 1:
            return False
        for _ in range(r):
            if x == n - 1:
                return False
            x = x * x % n
        return True

    return all(not is_c(b) for b in MR_BASES)


def fermat_test(n: int, check_times: int = 100) -> bool:
    assert n >= 1
    if n == 1:
        return False
    if n == 2:
        return True

    def n_is_composite(base: int) -> bool:
        nonlocal n
        if math.gcd(n, base) != 1:
            return True
        if pow(base, n - 1, n) != 1:
            return True
        return False

    checked_bases = set()

    for _ in range(check_times):
        base = random.randint(2, n - 1)
        if base in checked_bases:
            continue
        if n_is_composite(base):  # the base is called witness.
            return False
        checked_bases.add(base)

    # might be pseudo prime like Carmichael number.
    # if not prime actually, each checked base is called liar.
    return True


CARMICHAEL_NUMBERS: typing.Final[list[int]] = [
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
