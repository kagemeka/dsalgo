from __future__ import annotations

import math
import typing


def greatest_common_divisor_recurse(a: int, b: int) -> int:
    return greatest_common_divisor_recurse(b, a % b) if b else a


def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def array_gcd(arr: typing.Sequence[int]) -> int | None:
    if len(arr) == 0:
        return None
    gcd = arr[0]
    for x in arr:
        gcd = math.gcd(gcd, x)
    return gcd


def least_common_multiple(a: int, b: int) -> int:
    return 0 if a == b == 0 else a // math.gcd(a, b) * b


def extended_euclidean_gcd_modular_inverse(
    mod: int,
    n: int,
) -> tuple[int, int | None]:
    assert mod > 1 and 0 <= n < mod
    if n == 0:
        mod, None
    a, b = n, mod
    x00, x01 = 1, 0  # first row of matrix identity element.
    while b:
        q, r = divmod(a, b)
        x00, x01 = x01, x00 - q * x01
        a, b = b, r
    gcd = a
    if x00 < 0:
        x00 += mod // gcd
    assert 0 <= x00 < mod // gcd
    return gcd, x00


def extended_euclidean_recurse(a: int, b: int) -> tuple[int, int, int]:
    if not b:
        return a, 1, 0
    gcd, s, t = extended_euclidean_recurse(b, a % b)

    return gcd, t, s - a // b * t


def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    x00, x01, x10, x11 = 1, 0, 0, 1  # matrix identity element.
    while b:
        q, r = divmod(a, b)
        x00, x01 = x01, x00 - q * x01
        x10, x11 = x11, x10 - q * x11
        a, b = b, r
    return a, x00, x10
