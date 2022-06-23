import typing

import numba as nb
import numpy as np

from dsalgo.numba.algebra.modular import cumprod, factorial, factorial_inverse


@nb.njit
def mod_choose(
    mod: int, fact: np.ndarray, ifact: np.ndarray, n: int, k: int
) -> int:
    ok = (0 <= k) & (k <= n)
    return fact[n] * ifact[n - k] % mod * ifact[k] % mod * ok


@nb.njit
def mod_choose_inverse(
    mod: int, fact: np.ndarray, ifact: np.ndarray, n: int, k: int
) -> int:
    ok = (0 <= k) & (k <= n)
    return ifact[n] * fact[n - k] % mod * fact[k] % mod * ok


@nb.njit
def mod_nHk(
    mod: int, fact: np.ndarray, ifact: np.ndarray, n: int, k: int
) -> int:
    return mod_choose(n + k - 1, k, mod, fact, ifact)


# nonlocal
def __solve():
    mod = 10**9 + 7
    n = 100
    fact = factorial(mod, n)
    ifact = factorial_inverse(mod, n)

    def mod_choose(n, k):
        nonlocal mod, fact, ifact
        ok = (0 <= k) & (k <= n)
        return fact[n] * ifact[k] % mod * ifact[n - k] % mod * ok

    def mod_choose_inverse(n, k):
        nonlocal mod, fact, ifact
        ok = (0 <= k) & (k <= n)
        return ifact[n] * fact[n - k] % mod * fact[k] % mod * ok

    def mod_nHk(n, k):
        return mod_choose(n + k - 1, k)


@nb.njit
def pascal_triangle(
    op: typing.Callable[[int, int], int], n: int
) -> np.ndarray:
    choose = np.zeros((n + 1, n + 1), np.int64)
    choose[:, 0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            choose[i, j] = op(choose[i - 1, j], choose[i - 1, j - 1])
    return choose


@nb.njit
def choose_pascal(n: int) -> np.ndarray:
    op = lambda a, b: a + b
    return pascal_triangle(op, n)


@nb.njit
def mod_nchoose_table(mod: int, n: int, k: int) -> np.ndarray:
    a = np.arange(n + 1, n - k, -1)
    a[0] = 1
    cumprod(mod, a)
    return a * inv_factorial(mod, r + 1) % mod


@nb.njit
def nchoose2(n: int) -> int:
    return n * (n - 1) // 2 if n >= 2 else 0


@nb.njit
def next_combination(s: int) -> int:
    """Next Combination.

    Args:
        s (int): represent a bit set.

    Returns:
        int: the bit set of next combination.
    """
    i = s & -s
    j = s + i
    return (s & ~j) // i >> 1 | j


@nb.njit
def combinations(n: int, r: int) -> np.ndarray:
    a = np.arange(n)
    ls: list[list[int]] = []
    if r < 0 or r > n:
        return np.array(ls)
    rng = np.arange(r)[::-1]
    i = np.arange(r)
    ls.append(list(a[:r]))
    while 1:
        for j in rng:
            if i[j] != j + n - r:
                break
        else:
            return np.array(ls)
        i[j] += 1
        for j in range(j + 1, r):
            i[j] = i[j - 1] + 1
        b = []
        for j in i:
            b.append(a[j])
        ls.append(b)


@nb.jit
def combinations_with_next_comb(n: int, r: int) -> np.ndarray:
    ls: list[list[int]] = []
    if r < 0 or r > n:
        return np.array(ls)
    lim = 1 << n
    s = (1 << r) - 1
    i = np.arange(n)
    while s < lim:
        j = np.flatnonzero(s >> i & 1)
        ls.append(list(j))
        if s == 0:
            break
        s = next_combination(s)
    return np.array(ls)


@nb.njit
def permutations(
    n: int,
    r: typing.Optional[int] = None,
) -> np.array:
    if r is None:
        r = n
    ls = []
    if r < 0 or r > n:
        return np.array(ls)
    i = np.arange(n)
    rng = np.arange(r)[::-1]
    c = np.arange(r)
    ls.append(list(i[:r]))
    while 1:
        for j in rng:
            c[j] += 1
            if c[j] == n:
                x = i[j]
                i[j:-1] = i[j + 1 :]
                i[-1] = x
                c[j] = j
                continue
            k = c[j]
            i[j], i[k] = i[k], i[j]
            ls.append(list(i[:r]))
            break
        else:
            return np.array(ls)


@nb.njit
def permutations_with_next_perm(
    n: int,
) -> np.array:
    a = np.arange(n)
    m = np.prod(a + 1)
    b = np.zeros(
        shape=(m, n),
        dtype=np.int64,
    )
    for i in range(m):
        b[i] = a
        a = next_permutation(a)
    return b


@nb.njit((nb.i8[:],))
def next_permutation(arr: np.ndarray) -> typing.Optional[np.ndarray]:
    n, a = arr.size, arr.copy()
    i = -1
    for j in range(n - 1, 0, -1):
        if a[j - 1] >= a[j]:
            continue
        i = j - 1
        break
    if i == -1:
        return None
    a[i + 1 :] = a[-1:i:-1]
    for j in range(i + 1, n):
        if a[i] >= a[j]:
            continue
        a[i], a[j] = a[j], a[i]
        break
    return a


@nb.njit
def repeated_combinations_bfs(n: int, k: int) -> np.ndarray:
    assert k >= 1
    res = np.empty((1 << 20, k), np.int64)
    idx_to_add = 0

    def add_result(a):
        nonlocal idx_to_add
        res[idx_to_add] = a
        idx_to_add += 1

    que = [(np.zeros(k, np.int64), 0)]
    for a, i in que:
        if i == k:
            add_result(a)
            continue
        for j in range(a[i - 1], n):
            b = a.copy()
            b[i] = j
            que.append((b, i + 1))
    return res[:idx_to_add]


@nb.njit((nb.i8, nb.i8))
def repeated_permutations_bfs(n: int, k: int) -> np.ndarray:
    res = np.empty((n**k, k), np.int64)
    idx_to_add = 0

    def add_result(a):
        nonlocal idx_to_add
        res[idx_to_add] = a
        idx_to_add += 1

    que = [(np.empty(k, np.int64), 0)]
    for a, i in que:
        if i == k:
            add_result(a)
            continue
        for j in range(n):
            b = a.copy()
            b[i] = j
            que.append((b, i + 1))
    return res


@nb.njit((nb.i8, nb.i8))
def repeated_permutations_dfs(n: int, k: int) -> np.ndarray:
    res = np.empty((n**k, k), np.int64)
    idx_to_add = 0

    def add_result(a):
        nonlocal idx_to_add
        res[idx_to_add] = a
        idx_to_add += 1

    st = [(np.empty(k, np.int64), 0)]
    while st:
        a, i = st.pop()
        if i == k:
            add_result(a)
            continue
        for j in range(n):
            b = a.copy()
            b[i] = j
            st.append((b, i + 1))
    return res[::-1]


@nb.njit((nb.i8, nb.i8[:]))
def next_repeated_permutation(
    n: int,
    a: np.ndarray,
) -> typing.Optional[np.ndarray]:
    for i in range(a.size - 1, -1, -1):
        a[i] += 1
        if a[i] < n:
            return a
        a[i] = 0
    return None
