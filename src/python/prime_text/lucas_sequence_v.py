def lucas_sequence_v(v_j: int, k: int, n: int) -> int:
    """ Lucas数列 V_j mod nから、V_jk mod nを計算する。

    ここで、V_0 = 2, V_1 = a, V_j = aV_{j-1} - V_{j-2} (注: b=1)

    Args:
        v_j (int): Lucas数列のj番目
        k (int): 正整数
        n (int): 正整数

    Returns:
        int: jk 番目のLucas数列 V_jk mod n

    Examples:
        >>> lucas_sequence_v(5, 3, 100) # V_1 = 5, V_2 = 23, V_3 = 110
        10
        >>> lucas_sequence_v(47, 2, 1000) # (V_1 = 7,) V_2 = 47, V_3 = 322, V_4 = 2207
        207
    """
    x, y = v_j, (v_j**2 - 2) % n
    # kの2進数表記の上位ビットから下位ビットに向かって回す
    # ただし、最上位ビットの1は見ない
    for bit in bin(k)[3:]:
        if bit == '1':
            x, y = (x * y - v_j) % n, (y**2 - 2) % n
        else:
            x, y = (x**2 - 2) % n, (x * y - v_j) % n
    return x
