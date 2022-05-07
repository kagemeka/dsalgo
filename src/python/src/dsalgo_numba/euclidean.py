import numba as nb


@nb.njit
def extgcd_recurse(a: int, b: int) -> tuple[int, int, int]:
    if not b:
        return a, 1, 0
    g, s, t = extgcd_recurse(b, a % b)
    return g, t, s - a // b * t


@nb.njit
def extgcd(a: int, b: int) -> tuple[int, int, int]:
    x0, x1, x2, x3 = 1, 0, 0, 1

    while b:
        q, r = divmod(a, b)
        x0, x1 = x1, x0 - x1 * q
        x2, x3 = x3, x2 - x3 * q
        a, b = b, r
    return a, x0, x2


@nb.njit
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@nb.njit
def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b
