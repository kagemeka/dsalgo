import random

from jacobi_symbol import jacobi_symbol


def proth_test(m: int, s: int, k: int = 10) -> str:
    """ Prothテストを用いて、n = m * 2**s + 1が素数かを判定する。

    Args:
        m (int): 奇数
        s (int): m < 2**s を満たす
        k (int): 試行回数。既定値を10としたが、特に意味はない。

    Returns:
        string: 'prime number'       = nは素数
                'composite number'   = nは合成数
                'possibly composite' = nはおそらく合成数

    Examples:
        >>> proth_test(5, 3) # 5 * 2**3 + 1 = 41 is prime
        'prime number'
        >>> proth_test(5, 8) # 5 * 2**8 + 1 = 1281 is composite
        'composite number'
        >>> proth_test(3, 4) # 3 * 2**4 + 1 = 49 is composite
        'possibly composite'
    """
    n = m * 2**s + 1
    for _ in range(k):
        a = random.randrange(2, n)  # 2 <= a < n を満たす乱数を生成する
        if jacobi_symbol(a, n) == -1:
            if pow(a, (n - 1) // 2, n) == n - 1:
                return 'prime number'
            else:
                return 'composite number'
    return 'possibly composite'
