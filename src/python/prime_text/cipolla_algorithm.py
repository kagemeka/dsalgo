import random

from legendre_symbol import legendre_symbol
from n_times import n_times


def cipolla_algorithm(a: int, p: int) -> int:
    """Cipollaのアルゴリズム。

    x^2 = a mod p
    となるようなxを求める。
    このようなxが存在する場合、x,-xの2つが解となる。

    Args:
        a (int): 整数で、pを法として平方剰余
        p (int): 奇素数

    Returns:
        x (int): x^2 = a mod pを満たすx。

    Examples:
        >>> cipolla_algorithm(2, 7) # 4も解であるが、小さいほうの3を返す
        3
    """

    def _mul(x, y):
        a, b = x
        c, d = y
        return (a * c + b * d * s) % p, (a * d + b * c) % p

    assert legendre_symbol(a, p) == 1
    while True:
        t = random.randrange(0, p - 1)
        s = (t**2 - a) % p
        if legendre_symbol(s, p) == -1:
            break

    x, _ = n_times((t, 1), (p + 1) // 2, _mul)
    return min(x, -x % p)
