from __future__ import annotations

import functools
import typing


def reverse_bit(n: int) -> int:
    ...


def reset_least_bit_naive(n: int) -> int:
    """
    Examples:
        >>> reset_least_bit_naive(0b0110) == 0b0100
        True
    """
    return n - (n & -n)


def reset_least_bit(n: int) -> int:
    """
    Examples:
        >>> reset_least_bit(0b0110) == 0b0100
        True
    """
    assert n >= 0
    return n & (n - 1)


def bit_length_std(n: int) -> int:
    return n.bit_length()


def bit_length_naive(n: int) -> int:
    assert n >= 0
    length = 0
    while 1 << length <= n:
        length += 1
    return length


def bit_length(n: int) -> int:
    assert n >= 0
    if n == 0:
        return 0
    length = 1
    for i in range(5, -1, -1):
        i = 1 << i
        if n >> i == 0:
            continue
        length += i
        n >>= i
    return length


def bit_length_table(n: int) -> list[int]:
    """
    Notes:
        - std implementation is faster than table implementation.
    """
    length = [0] * n
    for i in range(1, n):
        length[i] = length[i >> 1] + 1
    return length


def next_power_of_two(n: int) -> int:
    assert n >= 0
    return 1 if n == 0 else 1 << (n - 1).bit_length()


def invert_bit(n: int) -> int:
    ...


def popcount_naive(n: int) -> int:
    """
    Examples:
        >>> popcount_naive(0b1010)
        2
        >>> popcount_naive(0b1100100)
        3
        >>> popcount_naive(-1)
        Traceback (most recent call last):
        ...
        AssertionError: n must be unsinged integer.
    """
    assert n >= 0, "n must be unsinged integer."
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt


@functools.lru_cache(maxsize=None)
def popcount_cached(n: int) -> int:
    r"""Popcount Cashed.

    Examples:
        >>> popcount_naive(0b1010)
        2
        >>> popcount_naive(0b1100100)
        3
        >>> popcount_naive(-1)
        Traceback (most recent call last):
        ...
        AssertionError: n must be unsinged integer.
    """
    assert n >= 0, "n must be unsinged integer."
    if n == 0:
        return 0
    return popcount_cached(n >> 1) + (n & 1)


def popcount_table(n: int) -> list[int]:
    cnt = [0] * n
    for i in range(n):
        cnt[i] = cnt[i >> 1] + (i & 1)
    return cnt


def popcount(n: int) -> int:
    """
    Examples:
        >>> popcount(0b1010)
        2
        >>> popcount(0b1100100)
        3
        >>> popcount(-1)
        64
    """
    n -= (n >> 1) & 0x5555555555555555
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n + (n >> 4)) & 0x0F0F0F0F0F0F0F0F
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x0000007F


def define_popcount(mask_size: int = 8) -> typing.Callable[[int], int]:
    count_table = popcount_table(1 << mask_size)
    mask = (1 << mask_size) - 1

    def popcount(n: int) -> int:
        count = 0
        while n:
            count += count_table[n & mask]
            n >>= mask_size
        return count

    return popcount


def least_significant_bit(n: int) -> int | None:
    """
    Examples:
        >>> least_significant_bit(0b01010)
        1
    """
    assert n >= 0
    if n == 0:
        return None
    return (n & -n).bit_length() - 1


def most_significant_bit_naive(n: int) -> int | None:
    """
    Examples:
        >>> most_significant_bit_naive(0b01010)
        3
    """
    assert n >= 0
    if n == 0:
        return None
    return n.bit_length() - 1


def most_significant_bit(n: int) -> typing.Optional[int]:
    """
    Examples:
        >>> most_significant_bit(0b01010)
        3
    """
    assert n >= 0
    if n == 0:
        return None
    if n & 0xFFFFFFFF00000000 > 0:
        n &= 0xFFFFFFFF00000000
    if n & 0xFFFF0000FFFF0000 > 0:
        n &= 0xFFFF0000FFFF0000
    if n & 0xFF00FF00FF00FF00 > 0:
        n &= 0xFF00FF00FF00FF00
    if n & 0xF0F0F0F0F0F0F0F0 > 0:
        n &= 0xF0F0F0F0F0F0F0F0
    if n & 0xCCCCCCCCCCCCCCCC > 0:
        n &= 0xCCCCCCCCCCCCCCCC
    if n & 0xAAAAAAAAAAAAAAAA > 0:
        n &= 0xAAAAAAAAAAAAAAAA
    return n.bit_length() - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
