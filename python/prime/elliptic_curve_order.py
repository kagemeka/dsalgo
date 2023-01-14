from legendre_symbol import legendre_symbol


def elliptic_curve_order(a: int, b: int, p: int) -> int:
    """楕円曲線 y**2 = x**3 + a*x + b (mod p) の群の位数を計算する。

    Args:
        a: int, b: int: 楕円曲線のパラメータ。y**2 = x**3 + a * x + b
        p (int): p > 3となる素数。

    Return:
        int: 群の位数

    Examples:
        >>> elliptic_curve_order(1, 3, 5)
        4
        >>> elliptic_curve_order(1, 1, 5)
        9
    """
    assert (4 * a**3 + 27 * b**2) % p != 0
    return (
        p + 1 + sum(legendre_symbol(x**3 + a * x + b, p) for x in range(p))
    )
