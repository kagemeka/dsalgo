from sympy.ntheory import factorint


def primitive_root(p: int, e: int) -> int:
    """p^eを法とする原始根を返す。

    Args:
        p (int): 奇素数
        e (int): 1以上の整数

    Returns:
        g (int): p^eを法とする原始根

    Examples:
        >>> primitive_root(7, 2)
        3
    """
    qs = [*factorint(p - 1)]  # p - 1の素因数リスト
    g = 2
    while not all(map(lambda q: pow(g, (p - 1) // q, p) != 1, qs)):
        g += 1
    if e == 1:
        return g
    if pow(g, p - 1, p**2) == 1:
        return g + p
    return g
