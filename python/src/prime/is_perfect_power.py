import math

from nth_root_int import nth_root_int


def is_perfect_power(n: int) -> bool:
    """nが累乗数（n = a^bの形）かを判定する。

    bが取り得る範囲の2 <= b <= lg(n) を全探索する

    Args:
        n (int): 累乗数かを判定する対象の自然数

    Returns:
        bool: True  = 累乗数である
              False = 累乗数ではない

    Examples:
        >>> is_perfect_power(27)
        True
        >>> is_perfect_power(26)
        False
    """
    for b in range(2, int(math.log2(n)) + 1):
        a = nth_root_int(n, b)
        if a**b == n:
            return True
    return False
