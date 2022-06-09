def pepin_test(k: int) -> str:
    """Pepinテストによって、Fermat数F_k = 2^{2^k}+1が素数であるかを判定する

    Args:
        k (int): 素数判定する対象の整数Fermat数

    Returns:
        string: 'composite number' = F_kは合成数
                'prime number'     = F_kは素数
    """
    F_k = 2 ** (2**k) + 1
    if pow(3, (F_k - 1) // 2, F_k) == F_k - 1:
        return "prime number"
    else:
        return "composite number"
