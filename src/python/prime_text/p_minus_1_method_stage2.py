import math

from sympy import primerange


def p_minus_1_method_stage2(n: int, *, B1: int, B2: int, a: int = 2) -> int:
    """ p-1法によって、nの素因数分解を行う。

    Args:
        n  (int): 素因数分解を行う整数
        B1 (int): nの素因数をpとしたとき、p-1がB1-smoothであることを仮定する。
                  一般論として、Bを大きくすれば素因数を見つけやすくなるが、計算時間がかかる。
        B2 (int): 第1段階の後、実行される第2の上限。
                  B1からB2にある素数をQiとするとき、(p-1)/QiがB1-smoothならば成功する。
        a  (int): 底。nによって得手不得手があるので、失敗するようならば変更し、
                  再度実行する等が考えられる。

    Returns:
        int: nの非自明な約数。素因数分解に失敗したときは、1

    Examples:
        >>> # 193707721 - 1 = 2**3 * 3**3 * 5 * 67 * 2677
        >>> p_minus_1_method_stage2(2**67 - 1, B1=67, B2=2677, a=3)
        193707721
    """
    # 第1段階
    for prime in primerange(1, B1 + 1):
        l = math.floor(math.log(n) / math.log(prime))
        a = pow(a, prime**l, n)
    # 第2段階の初期化
    diff_dict = {}
    stage2_prime_list = list(primerange(B1 + 1, B2 + 1))
    for idx in range(len(stage2_prime_list) - 1):
        prime_pair = stage2_prime_list[idx:idx + 2]
        diff = prime_pair[1] - prime_pair[0]
        if diff not in diff_dict:
            diff_dict[diff] = pow(a, diff, n)
    # 第2段階
    a = pow(a, stage2_prime_list[0], n)
    d = a - 1
    for idx in range(len(stage2_prime_list) - 1):
        prime_pair = stage2_prime_list[idx:idx + 2]
        diff = prime_pair[1] - prime_pair[0]
        a = (a * diff_dict[diff]) % n
        d = (d * (a - 1)) % n
    d = math.gcd(d, n)
    if 1 < d < n:
        return d
    return 1
