def lucas_lehmer_primality_test(q: int) -> str:
    """ Lucas-Lehmerテストによって、Mersenne数M_q = 2**q - 1が素数かを判定する。

    Args:
        q (int): 素数

    Returns:
        string: 'prime number'     = M_qは素数
                'composite number' = M_qは合成数

    Examples:
        >>> lucas_lehmer_primality_test(11)
        'composite number'
        >>> lucas_lehmer_primality_test(107)
        'prime number'
    """
    v = 4
    M_q = 2**q - 1
    for _ in range(q - 2):
        v = (v**2 - 2) % M_q
    if v == 0:
        return 'prime number'
    else:
        return 'composite number'
