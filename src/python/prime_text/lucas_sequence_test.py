import math

from legendre_symbol import legendre_symbol
from lucas_sequence import lucas_sequence


def lucas_sequence_test(n: int, a: int, b: int) -> int:
    """Lucas数列の性質を用いて、素数判定を行う。

    Args:
        n    (int): 素数判定を行う対象の整数
        a, b (int): Lucas数列のパラメータ

    Returns:
        string: 'composite number' = nは合成数
                'probable prime'   = nはおそらく素数

    Examples:
        >>> lucas_sequence_test(101, 2, -3) # 101は素数
        'probable prime'
        >>> lucas_sequence_test(323, 2, -3) # 323 = 17 * 19
        'composite number'
        >>> # パラメータによっては、合成数でも'probable prime'と出力する
        >>> lucas_sequence_test(323, -10, -5)
        'probable prime'
    """
    delta = a**2 - 4 * b
    condition = math.gcd(n, 2 * b * delta)
    assert condition != n
    if condition != 1:
        return "composite number"
    if lucas_sequence(n - legendre_symbol(delta, n), a, b) % n != 0:
        return "composite number"
    return "probable prime"
