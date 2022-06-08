import math


def dickman_function(u: float) -> float:
    """ dickman関数を計算する。(u > 2においては近似値)

    Args:
        u (float): 正の実数

    Returns:
        float: dickman関数 rho(u)を返す

    Examples:
        >>> dickman_function(1)
        1
        >>> dickman_function(2)
        0.3068528194400547
        >>> dickman_function(3)
        0.037037037037037035
    """
    if u <= 1:
        return 1
    if u <= 2:
        return 1 - math.log(u)
    return pow(u, -u)
