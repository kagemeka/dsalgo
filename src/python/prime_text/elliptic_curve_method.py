import math
import random

from EllipticCurveAffine import EllipticCurveAffine
from sympy.ntheory import primerange


def elliptic_curve_method(n: int, B: int) -> int:
    """楕円曲線法を用いて素因数分解を行う。

    Args:
        n (int): 素因数分解する整数。ただし、gcd(n,6)=1かつ累乗数でないとする。

    Returns:
        int: nの非自明な約数
             失敗した場合は、1

    Examples:
        >>> elliptic_curve_method(101 * 211, B=20)
        101
    """
    x, y = random.randint(0, n - 1), random.randint(0, n - 1)
    a = random.randint(0, n - 1)
    b = (y**2 - x**3 - a * x) % n
    ec = EllipticCurveAffine(a, b, n)
    P = (x, y, 1)
    for prime in primerange(2, B + 1):
        l = math.floor(math.log(B) / math.log(prime))
        try:
            P = ec.times(P, prime**l)
        except ValueError as e:
            return e.args[1]
    return 1
