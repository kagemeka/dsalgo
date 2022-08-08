from __future__ import annotations

import typing

import dsalgo.modular_int
import python.src.dsalgo.algebraic_structure
from dsalgo.type import T


def n_choose_table(p: int, n: int, kmax: int) -> list[int]:
    assert 0 <= kmax <= n
    a = list(range(n + 1, n - kmax, -1))
    a[0] = 1
    a = dsalgo.modular_int.cumprod(p, a)
    b = dsalgo.modular_int.factorial_inverse(p, kmax + 1)
    for i in range(kmax + 1):
        a[i] *= b[i]
        a[i] %= p
    return a


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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
