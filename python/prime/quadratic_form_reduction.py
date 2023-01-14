import math


def quadratic_form_reduction(a, b, c):
    """2次形式(a,b,c)の簡約形式を返す。

    Args:
        a, b, c (int): 2次形式のパラメータ。ただし、判別式Dは平方数でないとする。

    Returns:
        a, b, c (int): 簡約形式
    """
    D = b**2 - 4 * a * c
    while True:
        if abs(a) < abs(b):
            u = math.floor((abs(a) - b) / (2 * a))
            a, b, c = a, b + 2 * u * a, c + u * b + u**2 * a
        if abs(a) <= abs(c):
            break
        else:
            a, b, c = c, -b, a
    return a, b, c
