from __future__ import annotations

import functools
import typing


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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
