import math

from lucas_sequence_v import lucas_sequence_v
from sympy import primerange


def p_plus_1_method(n: int, *, B: int, a: int = 5) -> int:
    """p+1法によって、nの素因数分解を行う。

    Args:
        n (int): 素因数分解を行う整数
        B (int): nの素因数をpとしたとき、p+1がB-smoothであることを仮定する。
                 一般論として、Bを大きくすれば素因数を見つけやすくなるが、計算時間がかかる。
        a (int): Lucas数列のパラメータ。delta=a**2-4, nの素因数をp としたとき、deltaはpを法として
                 平方非剰余でなければならない。もちろん、素因数が判明していない状況なので、
                 ランダムに選んで平方非剰余であることを祈る(失敗すればaを変更する)。
                 平方剰余の場合、因数分解できる数はp-1法に一致し、p-1法の劣化版になる。

    Returns:
        int: nの非自明な約数。素因数分解に失敗したときは、1

    Examples:
        >>> # 1062637 = 1013 * 1049
        >>> # 1049 + 1 = 2 * 3 * 5**2 * 7
        >>> p_plus_1_method(1062637, B=7, a=13)
        1049
    """
    v = a
    for prime in primerange(1, B + 1):
        l = math.floor(math.log(n) / math.log(prime))
        v = lucas_sequence_v(v, prime**l, n)
    d = math.gcd(v - 2, n)
    if 1 < d < n:
        return d
    return 1
