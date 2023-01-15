from typing import Generator, Tuple

from legendre_symbol import legendre_symbol
from tonelli_shanks_algorithm import tonelli_shanks_algorithm


def elliptic_curve_points(
    a: int, b: int, p: int
) -> Generator[Tuple[int, int], None, None]:
    """楕円曲線 y**2 = x**3 + a*x + b (mod p) の点を枚挙する。

    Args:
        a: int, b: int: 楕円曲線のパラメータ。y**2 = x**3 + a * x + b
        p (int): p > 3となる素数。

    Yields:
        x, y (int, int): 楕円曲線上の点(無限遠点を除く)

    Examples:
        >>> list(elliptic_curve_points(1, 3, 5))
        [(1, 0), (4, 1), (4, 4)]
        >>> list(elliptic_curve_points(1, 1, 5))
        [(0, 1), (0, 4), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3)]
    """
    assert (4 * a**3 + 27 * b**2) % p != 0
    for x in range(p):
        y2 = (x**3 + a * x + b) % p
        legendre = legendre_symbol(y2, p)
        if legendre == 0:
            yield x, 0
        elif legendre == 1:
            y = tonelli_shanks_algorithm(y2, p)
            yield x, y
            yield x, -y % p
