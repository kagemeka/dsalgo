import math

from sympy import primerange


def p_minus_1_method(n: int, *, B: int, a: int = 2) -> int:
    """p-1法によって、nの素因数分解を行う。

    Args:
        n (int): 素因数分解を行う整数
        B (int): nの素因数をpとしたとき、p-1がB-smoothであることを仮定する。
                 一般論として、Bを大きくすれば素因数を見つけやすくなるが、計算時間がかかる。
        a (int): 底。nによって得手不得手があるので、失敗するようならば変更し、
                 再度実行する等が考えられる。

    Returns:
        int: nの非自明な約数。素因数分解に失敗したときは、1

    Examples:
        >>> # 464808857 = 229 * 967 * 2099, 221443 = 229 * 967
        >>> # 229 - 1 = 2**3 * 3 * 19
        >>> # 967 - 1 = 2 * 3* 7 * 23
        >>> p_minus_1_method(464808857, B=22)
        229
        >>> p_minus_1_method(464808857, B=23)
        221443
    """
    for prime in primerange(1, B + 1):
        l = math.floor(math.log(n) / math.log(prime))
        a = pow(a, prime**l, n)
    d = math.gcd(a - 1, n)
    if 1 < d < n:
        return d
    return 1
