from __future__ import annotations

import typing

import dsalgo.abstract_structure
import dsalgo.modular
from dsalgo.type import T


def pascal_triangle(
    monoid: dsalgo.abstract_structure.Monoid[T],
    default: typing.Callable[[], T],
    size: int,
) -> list[list[T]]:
    p = [[monoid.identity() for _ in range(size)] for _ in range(size)]
    for i in range(size):
        p[i][0] = default()
    for i in range(1, size):
        for j in range(1, i + 1):
            p[i][j] = monoid.operation(p[i - 1][j - 1], p[i - 1][j])
    return p


def define_caching_pascal_triangle(
    monoid: dsalgo.abstract_structure.Monoid[T],
    default: typing.Callable[[], T],
) -> typing.Callable[[int, int], T]:
    import functools

    @functools.lru_cache(maxsize=None)
    def pascal(n: int, k: int) -> T:
        if k < 0 or n < k:
            return monoid.identity()
        if k == 0:
            return default()
        return monoid.operation(pascal(n - 1, k), pascal(n - 1, k - 1))

    return pascal


def make_choose(p: int, n: int) -> typing.Callable[[int, int], int]:
    fact = dsalgo.modular.factorial(p, n)
    ifact = dsalgo.modular.factorial_inverse(p, n)

    def choose(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k:
            return 0
        return fact[n] * ifact[n - k] % p * ifact[k] % p

    return choose


def make_caching_pascal_choose(
    mod: int | None = None,
) -> typing.Callable[[int, int], int]:
    import functools
    import sys

    sys.setrecursionlimit(1 << 20)
    if mod is not None:
        assert mod >= 1

    @functools.lru_cache(maxsize=None)
    def choose(n: int, k: int) -> int:
        if k < 0 or n < k:
            return 0
        if k == 0:
            return 1
        res = choose(n - 1, k) + choose(n - 1, k - 1)
        if mod is not None:
            res %= mod
        return res

    return choose


def n_choose_table(p: int, n: int, kmax: int) -> list[int]:
    assert 0 <= kmax <= n
    a = list(range(n + 1, n - kmax, -1))
    a[0] = 1
    a = dsalgo.modular.cumprod(p, a)
    b = dsalgo.modular.factorial_inverse(p, kmax + 1)
    for i in range(kmax + 1):
        a[i] *= b[i]
        a[i] %= p
    return a


def make_count_permutation(p: int, n: int) -> typing.Callable[[int, int], int]:
    fact = dsalgo.modular.factorial(p, n)
    ifact = dsalgo.modular.factorial_inverse(p, n)

    def count_perm(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k:
            return 0
        return fact[n] * ifact[n - k] % p

    return count_perm


def combinations(
    n: int,
    k: int,
) -> typing.Generator[tuple[int, ...], None, None]:
    a = tuple(range(n))
    n = len(a)
    if k < 0 or n < k:
        return
    rng = range(k)
    res = list(rng)
    yield a[:k]
    while True:
        for j in reversed(rng):
            if res[j] != j + n - k:
                break
        else:
            return
        res[j] += 1
        for j in range(j + 1, k):
            res[j] = res[j - 1] + 1
        yield tuple(a[j] for j in res)


def combinations_next_comb(
    n: int,
    k: int,
) -> typing.Generator[tuple[int, ...], None, None]:
    a = tuple(range(n))
    n = len(a)
    if k < 0 or n < k:
        return
    if k == 0:
        yield ()
        return
    limit = 1 << n
    s = (1 << k) - 1
    while s < limit:
        yield tuple(a[i] for i in range(n) if s >> i & 1)
        s = next_combination(s)


def next_combination(s: int) -> int:
    lsb = s & -s
    i = s + lsb
    return (s & ~i) // lsb >> 1 | i


def repeated_combinations(
    n: int,
    k: int,
) -> typing.Generator[tuple[int, ...], None, None]:
    """Repeated Combinations.

    Args:
        n (int): n of nHk
        k (int): k of nHk

    Returns:
        typing.Generator[tuple[int, ...], None, None]: [description]
    """
    ...


def next_permutation(
    arr: list[int],
) -> typing.Optional[list[int]]:
    n, arr = len(arr), arr.copy()
    last_asc_idx = n
    for i in range(n - 2, -1, -1):
        if arr[i] >= arr[i + 1]:
            continue
        last_asc_idx = i
        break
    if last_asc_idx == n:
        return None
    arr[last_asc_idx + 1 :] = arr[-1:last_asc_idx:-1]
    for i in range(last_asc_idx + 1, n):
        if arr[last_asc_idx] >= arr[i]:
            continue
        arr[last_asc_idx], arr[i] = arr[i], arr[last_asc_idx]
        break
    return arr


def permutations(
    n: int,
    k: typing.Optional[int] = None,
) -> typing.Iterator[tuple[int, ...]]:
    if k is None:
        k = n
    if k < 0 or n < k:
        return
    indices = list(range(n))
    cycles = list(range(k))
    yield tuple(indices[:k])
    while True:
        for i in reversed(range(k)):
            cycles[i] += 1
            if cycles[i] == n:
                indices[i:] = indices[i + 1 :] + indices[i : i + 1]
                cycles[i] = i
                continue
            j = cycles[i]
            indices[i], indices[j] = indices[j], indices[i]
            yield tuple(indices[:k])
            break
        else:
            return


def permutations_dfs(
    n: int,
    k: typing.Optional[int] = None,
) -> typing.Iterator[tuple[int, ...]]:
    if k is None:
        k = n
    indices = list(range(n))

    def dfs(left: int) -> typing.Iterator[tuple[int, ...]]:
        nonlocal indices, n, k
        if left == k:
            yield tuple(indices[:k])
            return
        for i in range(left, n):
            indices[left], indices[i] = indices[i], indices[left]
            yield from dfs(left + 1)
            indices[left], indices[i] = indices[i], indices[left]

    return dfs(0)


def permutations_next_perm(n: int) -> typing.Iterator[tuple[int, ...]]:
    arr: typing.Optional[list[int]] = list(range(n))
    while arr is not None:
        yield tuple(arr)
        arr = next_permutation(arr)


def repeated_permutations_dfs(
    n: int,
    repeat: int,
) -> typing.Iterator[tuple[int, ...]]:
    p: list[int] = [n] * repeat

    def dfs(fixed_count: int) -> typing.Iterator[tuple[int, ...]]:
        nonlocal p
        if fixed_count == repeat:
            yield tuple(p)
            return
        for i in range(n):
            p[fixed_count] = i
            yield from dfs(fixed_count + 1)

    return dfs(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
