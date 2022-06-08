from __future__ import annotations

import math
import random
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


def _is_trivial_composite(n: int) -> bool:
    return n > 2 and n & 1 == 0


def _is_composite(n: int, base: int) -> bool:
    assert n >= 3
    r, d = 0, n - 1
    while d & 1 == 0:
        r += 1
        d >>= 1
    # n - 1 = d2^r
    x = pow(base, d, n)
    if x == 1:
        return False
    for _ in range(r):
        if x == n - 1:
            return False
        x = x * x % n
    return True


def _miller_rabin_fixed_bases(n: int, bases: list[int]) -> bool:
    assert n >= 1
    if _is_trivial_composite(n):
        return False
    if n == 2:
        return True
    for base in bases:
        if _is_composite(n, base):
            return False
    return True


def miller_rabin_test(n: int, check_times: int = 20) -> bool:
    assert n >= 1
    if n == 1:
        return False
    bases = list(set(random.randint(1, n - 1) for _ in range(check_times)))
    return _miller_rabin_fixed_bases(n, bases)


def miller_rabin_test_32(n: int) -> bool:
    BASES = [2, 7, 61]
    return _miller_rabin_fixed_bases(n, BASES)


def miller_rabin_test_64(n: int) -> bool:
    BASES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    return _miller_rabin_fixed_bases(n, BASES)


def miller_rabin_test_64_v2(n: int) -> bool:
    BASES = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    return _miller_rabin_fixed_bases(n, BASES)


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
