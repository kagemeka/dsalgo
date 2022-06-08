"""
Tag
- numbe theory
"""

from dsalgo.floor_sqrt import floor_sqrt


def floor_sum(n: int) -> int:
    r"""Floor Sum.

    1 <= n <= 10 ^ 16
    return \sum_{i=1}^{n} n // i
    """
    s = 0
    i = 1
    while i <= n:
        x = n // i
        j = n // x + 1
        s += x * (j - i)
        i = j
    return s


def floor_sum_v2(n: int) -> int:
    r"""Floor Sum.

    1 <= n <= 10 ^ 16
    return \sum_{i=1}^{n} n // i
    """
    s = 0
    k = floor_sqrt(n)
    for i in range(1, n // (k + 1) + 1):
        s += n // i
    for x in range(1, k + 1):
        s += x * (n // x - n // (x + 1))
    return s
